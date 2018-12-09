# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.12.7
# python练习测试9：深度优先搜索与“机器人迷宫”项目测试
import sys
# env_data = [[3, 2, 2, 2, 2, 2, 2, 2, 1],
#  [0, 0, 2, 2, 2, 2, 2, 0, 0],
#  [2, 0, 0, 2, 2, 2, 0, 0, 2],
#  [2, 2, 0, 0, 2, 0, 0, 2, 2],
#  [2, 2, 2, 0, 0, 0, 2, 2, 2]]

sys.setrecursionlimit(1000000)

env_data = [[3, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 2, 2, 2, 2, 2, 0, 0],
 [2, 0, 0, 2, 2, 2, 0, 0, 2],
 [2, 2, 0, 0, 2, 0, 0, 2, 2],
 [2, 2, 2, 0, 0, 0, 2, 2, 2]]

rows = len(env_data)
columns = len(env_data[0])

loc_map = {}
has_start = False
has_destination = False
for row in range(rows):
    if 1 in env_data[row]:
        loc_map['start'] = (row, env_data[row].index(1))
        has_start = True
    if 3 in env_data[row]:
        loc_map['destination'] = (row, env_data[row].index(3))
        has_destination = True
    if has_start and has_destination:
        break

robot_current_loc = loc_map['start']
robot_destination_loc = loc_map['destination']
x_destination = robot_destination_loc[0]
y_destination = robot_destination_loc[1]
current_path = []
best_path = []
paths = 0


def is_move_valid(env_data, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    # TODO 9
    result = False
    new_loc = (-1, -1)
    if act == 'u':
        new_loc = (loc[0] - 1, loc[1])
    elif act == 'd':
        new_loc = (loc[0] + 1, loc[1])
    elif act == 'l':
        new_loc = (loc[0], loc[1] - 1)
    elif act == 'r':
        new_loc = (loc[0], loc[1] + 1)

    if 0 <= new_loc[0] < rows and 0 <= new_loc[1] < columns and env_data[new_loc[0]][new_loc[1]] != 2:
        result = True

    return result


def move_robot(loc, act):
    row = loc[0]
    column = loc[1]
    if is_move_valid(env_data, loc, act):
        if act == 'u':
            row = loc[0] - 1
        elif act == 'd':
            row = loc[0] + 1
        elif act == 'l':
            column = loc[1] - 1
        elif act == 'r':
            column = loc[1] + 1
    new_loc = (row, column)
    return new_loc


def valid_actions(env_data, loc):
    actions = []
    for action in ['u', 'd', 'l', 'r']:
        if is_move_valid(env_data, loc, action):
            actions.append(action)

    return actions


def depth_first_search(env_data, loc):
    global best_path
    global paths
    if loc == robot_destination_loc:
        paths += 1
        current_path.append(robot_destination_loc)
        if len(best_path) == 0:
            best_path = current_path[:]
        elif len(best_path) > len(current_path):
            best_path = current_path[:]
        return

    actions = valid_actions(env_data, loc)
    for action in actions:
        x = loc[0]
        y = loc[1]
        env_data[x][y] = 2
        current_path.append(loc)
        loc = move_robot(loc, action)
        depth_first_search(env_data, loc)
        env_data[x][y] = 0
        current_path.pop()


depth_first_search(env_data, robot_current_loc)
print(best_path)
print(paths)
