# 马尔可夫决策模型（Markov Decision Process, MDP）
import numpy as np

# 定义网格世界的尺寸
GRID_SIZE = 4
ACTIONS = ["up", "down", "left", "right"]
ACTION_PROB = 0.8  # 80%的概率按预期方向移动
GAMMA = 0.9  # 折扣因子
THETA = 1e-4  # 收敛阈值


# 定义奖励函数
def reward(state):
    if state == (GRID_SIZE - 1, GRID_SIZE - 1):  # 到达终点
        return 1
    return 0  # 其他情况


# 定义转移函数
def transition(state, action):
    x, y = state
    if action == "up":
        new_x, new_y = max(x - 1, 0), y
    elif action == "down":
        new_x, new_y = min(x + 1, GRID_SIZE - 1), y
    elif action == "left":
        new_x, new_y = x, max(y - 1, 0)
    elif action == "right":
        new_x, new_y = x, min(y + 1, GRID_SIZE - 1)
    return (new_x, new_y)


# 值迭代算法
def value_iteration():
    # 初始化价值函数
    value = np.zeros((GRID_SIZE, GRID_SIZE))

    while True:
        delta = 0
        new_value = np.zeros((GRID_SIZE, GRID_SIZE))

        # 遍历每个状态
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                state = (x, y)
                if state == (GRID_SIZE - 1, GRID_SIZE - 1):  # 终点状态
                    new_value[x, y] = 0
                    continue

                # 计算每个动作的期望价值
                action_values = []
                for action in ACTIONS:
                    # 预期方向的价值
                    new_state = transition(state, action)
                    expected_value = ACTION_PROB * (reward(new_state) + GAMMA * value[new_state])

                    # 随机方向的价值
                    random_value = 0
                    for a in ACTIONS:
                        if a != action:
                            new_state_random = transition(state, a)
                            random_value += (1 - ACTION_PROB) / (len(ACTIONS) - 1) * (
                                        reward(new_state_random) + GAMMA * value[new_state_random])

                    total_value = expected_value + random_value
                    action_values.append(total_value)

                # 选择最大价值
                new_value[x, y] = max(action_values)
                delta = max(delta, abs(new_value[x, y] - value[x, y]))

        # 判断是否收敛
        if delta < THETA:
            break
        value = new_value.copy()

    return value


# 提取最优策略
def extract_policy(value):
    policy = np.empty((GRID_SIZE, GRID_SIZE), dtype=str)

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            state = (x, y)
            if state == (GRID_SIZE - 1, GRID_SIZE - 1):  # 终点状态
                policy[x, y] = "G"
                continue

            action_values = []
            for action in ACTIONS:
                new_state = transition(state, action)
                expected_value = ACTION_PROB * (reward(new_state) + GAMMA * value[new_state])
                random_value = 0
                for a in ACTIONS:
                    if a != action:
                        new_state_random = transition(state, a)
                        random_value += (1 - ACTION_PROB) / (len(ACTIONS) - 1) * (
                                    reward(new_state_random) + GAMMA * value[new_state_random])
                total_value = expected_value + random_value
                action_values.append(total_value)

            # 选择最优动作
            best_action = ACTIONS[np.argmax(action_values)]
            policy[x, y] = best_action[0].upper()  # 取动作的首字母

    return policy


# 主程序
if __name__ == "__main__":
    # 运行值迭代算法
    value = value_iteration()
    print("价值函数：")
    print(value)

    # 提取最优策略
    policy = extract_policy(value)
    print("\n最优策略：")
    print(policy)