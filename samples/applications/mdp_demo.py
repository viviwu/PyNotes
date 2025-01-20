# 马尔可夫决策模型（Markov Decision Process, MDP）
import numpy as np

# 定义网格世界的尺寸
GRID_SIZE = 4
NUM_STATES = GRID_SIZE * GRID_SIZE
NUM_ACTIONS = 4  # 上、下、左、右

# 定义动作
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上、下、左、右
ACTION_NAMES = ['上', '下', '左', '右']

# 定义奖励函数
REWARDS = np.zeros((GRID_SIZE, GRID_SIZE))
REWARDS[GRID_SIZE-1, GRID_SIZE-1] = 1  # 终点奖励

# 定义转移概率
TRANSITION_PROB = 0.8  # 成功概率
RANDOM_PROB = 0.2 / 3  # 随机移动到其他方向的概率

# 初始化价值函数
V = np.zeros((GRID_SIZE, GRID_SIZE))

# 折扣因子
GAMMA = 0.9

# 值迭代算法
def value_iteration(V, REWARDS, ACTIONS, TRANSITION_PROB, RANDOM_PROB, GAMMA, THRESHOLD=1e-6):
    while True:
        delta = 0
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i, j) == (GRID_SIZE-1, GRID_SIZE-1):  # 终点
                    continue
                v = V[i, j]
                max_v = float('-inf')
                for a_idx, (di, dj) in enumerate(ACTIONS):
                    total = 0
                    for a_prime_idx, (di_prime, dj_prime) in enumerate(ACTIONS):
                        if a_prime_idx == a_idx:
                            prob = TRANSITION_PROB
                        else:
                            prob = RANDOM_PROB
                        ni, nj = i + di_prime, j + dj_prime
                        if ni < 0 or ni >= GRID_SIZE or nj < 0 or nj >= GRID_SIZE:
                            ni, nj = i, j  # 撞墙，留在原地
                        total += prob * (REWARDS[ni, nj] + GAMMA * V[ni, nj])
                    if total > max_v:
                        max_v = total
                V[i, j] = max_v
                delta = max(delta, abs(v - V[i, j]))
        if delta < THRESHOLD:
            break
    return V

# 执行值迭代
V = value_iteration(V, REWARDS, ACTIONS, TRANSITION_PROB, RANDOM_PROB, GAMMA)

# 打印最终的价值函数
print("最终的价值函数：")
print(V)

# 根据价值函数提取最优策略
def extract_policy(V, REWARDS, ACTIONS, TRANSITION_PROB, RANDOM_PROB, GAMMA):
    policy = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == (GRID_SIZE-1, GRID_SIZE-1):  # 终点
                continue
            max_v = float('-inf')
            best_action = 0
            for a_idx, (di, dj) in enumerate(ACTIONS):
                total = 0
                for a_prime_idx, (di_prime, dj_prime) in enumerate(ACTIONS):
                    if a_prime_idx == a_idx:
                        prob = TRANSITION_PROB
                    else:
                        prob = RANDOM_PROB
                    ni, nj = i + di_prime, j + dj_prime
                    if ni < 0 or ni >= GRID_SIZE or nj < 0 or nj >= GRID_SIZE:
                        ni, nj = i, j  # 撞墙，留在原地
                    total += prob * (REWARDS[ni, nj] + GAMMA * V[ni, nj])
                if total > max_v:
                    max_v = total
                    best_action = a_idx
            policy[i, j] = best_action
    return policy

# 提取最优策略
policy = extract_policy(V, REWARDS, ACTIONS, TRANSITION_PROB, RANDOM_PROB, GAMMA)

# 打印最优策略
print("\n最优策略：")
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if (i, j) == (GRID_SIZE-1, GRID_SIZE-1):
            print("终点", end=" ")
        else:
            print(ACTION_NAMES[policy[i, j]], end=" ")
    print()