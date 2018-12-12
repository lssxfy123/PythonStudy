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

marks = [[0 for j in range(columns)] for i in range(columns)]

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
x_start = robot_current_loc[0]
y_start = robot_current_loc[1]
marks[x_start][y_start] = 2
every_actions = []
total_actions = []
best_actions = []
actions_count = 0


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


## 深度优先搜索
def depth_first_search(env_data, loc):
    global best_actions
    global actions_count
    if loc == robot_destination_loc:  ## 如果行走到终点
        actions_count += 1
        total_actions.append(every_actions[:])
        ## 判断是否为最佳策略
        if len(best_actions) == 0:
            best_actions = every_actions[:]
        elif len(best_actions) > len(every_actions):
            best_actions = every_actions[:]
        return

    actions = valid_actions(env_data, loc)  ## 查找所有可行动作
    for action in actions:
        new_loc = move_robot(loc, action)  ## 新的位置点
        x = new_loc[0]
        y = new_loc[1]
        if marks[x][y] == 0:  ## 如果该点未走过
            marks[x][y] = 2  ## 将该点标记为已走过
            every_actions.append(action)  ## 将动作插入策略列表
            depth_first_search(env_data, new_loc)  ## 进行下一个点的尝试
            marks[x][y] = 0  ## 尝试结束，将该点标记为未走
            every_actions.pop()  ## 将该动作从策略列表弹出


depth_first_search(env_data, robot_current_loc)
print("总共有{}种行走策略".format(actions_count))
for i in range(actions_count):
    print("策略{}：".format(i + 1), "->".join(total_actions[i]))
print("最佳策略为：", "->".join(best_actions))

