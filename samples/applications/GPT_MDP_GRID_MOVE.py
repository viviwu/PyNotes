import numpy as np
import random

# 网格世界大小
grid_size = 4
# 定义动作：上（0），右（1），下（2），左（3）
actions = ['up', 'right', 'down', 'left']


# 定义奖励函数：目标状态(3, 3)的奖励为1，其它状态的奖励为0
def reward(state):
    if state == (3, 3):
        return 1
    return 0


# 定义状态转移函数
def get_next_state(state, action):
    x, y = state
    if action == 0:  # 上
        return (max(x - 1, 0), y)
    if action == 1:  # 右
        return (x, min(y + 1, grid_size - 1))
    if action == 2:  # 下
        return (min(x + 1, grid_size - 1), y)
    if action == 3:  # 左
        return (x, max(y - 1, 0))


# 定义随机转移函数，考虑转移概率
def random_transition(state, action):
    # 80%的概率成功移动，20%的概率随机移动
    if random.random() < 0.8:
        return get_next_state(state, action)
    else:
        # 随机选择一个其它的方向
        random_action = random.choice([i for i in range(4) if i != action])
        return get_next_state(state, random_action)


# 初始化价值函数V，所有状态的初始价值为0
V = np.zeros((grid_size, grid_size))

# 折扣因子和迭代次数
gamma = 0.9
theta = 1e-6


# 价值迭代算法
def value_iteration():
    global V
    while True:
        delta = 0
        # 遍历所有状态
        for x in range(grid_size):
            for y in range(grid_size):
                # 不考虑目标状态(3, 3)，因为目标状态的价值是固定的
                if (x, y) == (3, 3):
                    continue
                v = V[x, y]
                # 计算当前状态下的最大价值
                max_value = float('-inf')
                for action in range(4):  # 对所有动作求最大值
                    next_state = random_transition((x, y), action)
                    reward_value = reward(next_state)
                    value = reward_value + gamma * V[next_state[0], next_state[1]]
                    max_value = max(max_value, value)
                V[x, y] = max_value
                delta = max(delta, abs(v - V[x, y]))

        # 如果价值变化非常小，停止迭代
        if delta < theta:
            break


# 提取最优策略
def extract_policy():
    policy = np.full((grid_size, grid_size), -1)
    for x in range(grid_size):
        for y in range(grid_size):
            # 不考虑目标状态(3, 3)
            if (x, y) == (3, 3):
                continue
            best_action = None
            max_value = float('-inf')
            for action in range(4):
                next_state = random_transition((x, y), action)
                reward_value = reward(next_state)
                value = reward_value + gamma * V[next_state[0], next_state[1]]
                if value > max_value:
                    max_value = value
                    best_action = action
            policy[x, y] = best_action
    return policy


# 运行价值迭代算法
value_iteration()

# 输出最终的价值函数
print("Value Function V:")
print(V)

# 提取最优策略
policy = extract_policy()

# 输出最优策略
print("\nOptimal Policy:")
policy_actions = [['' for _ in range(grid_size)] for _ in range(grid_size)]
for x in range(grid_size):
    for y in range(grid_size):
        if (x, y) == (3, 3):
            policy_actions[x][y] = 'Goal'
        else:
            policy_actions[x][y] = actions[policy[x, y]]

for row in policy_actions:
    print(row)
