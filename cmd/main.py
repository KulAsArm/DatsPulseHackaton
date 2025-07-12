import os
from typing import List
import requests
import time
from dotenv import load_dotenv


load_dotenv("../config/.env")
sess = requests.session()
token = os.getenv("TOKEN")
url = os.getenv("URL")
url_register = url + '/register'
url_arena = url + "/arena"
url_move = url + "/move"
url_logs = url + "/logs"
print(url)
headers = {"X-Auth-Token": token}

count_ants = 0

ANT_TYPE = {0: "рабочий", 1: "боец", 2: "разведчик"}
FOOD_TYPE = {1: 'яблоко', 2:'хлеб', 3:'нектар'}
HEX_TYPE = {1: 1, 2: 1, 3: 2, 4: 1, 5: False}


class BaseEntity:
    def to_dict(self):
        """
        Create dict from model.
        :return: dict
        """
        return {x: getattr(self, x) for x in dir(self) if not callable(x) and not x.startswith(('__', 'to_dict', 'from_dict', 'set_attr'))}

class Ant(BaseEntity):
    def __init__(self, q, r, type, health, id, food, **kwargs):
        self.hex = Hex(q, r).to_dict()
        self._type = ANT_TYPE[type]
        self.health = health
        self._id = id
        self.food = food

class Hex(BaseEntity):
    def __init__(self, q, r, cost=None, type=None):
        self.vertical = q
        self.horizontal = r
        self.cost = cost
        self._type = type

class Map(BaseEntity):
    def __init__(self, hexs, home, food):
        self.hexs = hexs
        self.home = home
        self.food = food

    def create_map(self):
        if self.hexs:
            _map = sorted(self.hexs, key=lambda x: (x['q'], x['r']))
            coord = []
            for hex in _map:
                coord.append((hex['q'], hex['r']))
            max_vert = max(coord, key=lambda x: x[0])[0]
            min_vert = min(coord, key=lambda x: x[0])[0]
            max_hor = min(coord, key=lambda x: x[1])[1]
            min_hor = max(coord, key=lambda x: x[1])[1]
            food = [(d['q'], d['r']) for d in self.food]
            home = [(d['q'], d['r']) for d in self.home]

            print(f"Максимум по вертикале {max_vert}")
            print(f"Минимум по вертикале {min_vert}")
            print(f"Максимум по горизонтале {max_hor}")
            print(f"Минимум по горизонтале {max_vert}")
            abs_max = abs(max([max_hor, min_hor, min_vert, max_vert], key=lambda x: abs(x)))
            print(abs_max)
            main_hex = [(9, -20), (10, -22)]
            rows = ''
            for i in range(-abs_max, abs_max):
                cols = ''
                for j in range(-abs_max, abs_max):
                    if (i, j) in coord:
                        if (i, j) in home:
                            cols += f'\thh {(i, j)}'
                        elif (i, j) in food:
                            cols += f'\tff {(i, j)}'
                        else:
                            cols += f'\t^^ {(i, j)}'
                rows += cols + '\n'
            print(rows)
        print('')



def get_enemies_near_home(enemies):
    enems = []
    for enemy in enemies:
        enems.append(Ant(**enemy))
    return len(enemies), enems

def get_ants(ants) -> List[Ant]:
    process_ants = []
    for ant in ants:
        process_ants.append(Ant(**ant))
    return process_ants

def process_ant(ant):
    info = {"columns": ant['q'],
            "rows": ant['r'],
            "horizontal": ant['r'],
            "vertical": ant['q'],
            }

def get_home_hex(resp):
    print(f"Дом: {resp['home']}")
    return resp['home']

def get_count_ants(ants):
    return len(ants)

def get_food_hex(resp):
    print(f"Еда: {resp['food']}")
    return resp['food']

def round_info():
    resp = None
    success = False
    ants = None
    try:
        resp = sess.get(url_arena, headers=headers)
    except Exception as e:
        print(e)
        print(resp.json())
    if resp.ok:
        success = True
        resp = resp.json()
        print(resp)
        print(f"Количество муравьев: {get_count_ants(resp['ants'])}")
        ants = [x for x in get_ants(resp['ants'])]
        print(f"Количество врагов: {get_enemies_near_home(resp['enemies'])}")
        time.sleep(10)
        MAP = Map(resp['map'], get_home_hex(resp), get_food_hex(resp))
        MAP.create_map()
        return ants, resp, success


def register():
    info = None
    try:
        info = sess.post(url_register, headers=headers)
        print(info.json())
    except Exception as e:
        print(e)
        print(info.json())
    if info.ok:
        print(info.json()['nextTurn'] / 60)

def move_ant(ant, home):
    current_hex = (ant.hex['horizontal'], ant.hex['vertical'])
    data = {}
    if current_hex in home:
        ind = home.index(current_hex)
        data = {
            "moves": [
                {
                    "ant": ant.id,
                    "path": [
                        {
                            "q": home[ind + 1]['q'],
                            "r": home[ind + 1]['r']
                        }
                    ]
                }
            ]
        }
    sess.post(url_move, json=data, headers=headers)


while True:
    register()
    ants, resp, suc = round_info()
    if ants:
        for ant in ants:
            move_ant(ant, get_home_hex(resp))
    try:
        print(sess.get(url_logs, headers=headers))
    except Exception as e:
        print(e)
    if not suc:
        time.sleep(60)