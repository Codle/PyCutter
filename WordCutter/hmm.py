
PrevStatus = {
    'B': ('E', 'S'),
    'M': ('M', 'B'),
    'S': ('S', 'E'),
    'E': ('B', 'M')
}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    for y in states:
        V[0][y] = start_p[y]+emit_p[y].get(obs[0], MIN_FLOAT)
        path[y] = [y]
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        for y in states:
            em_p = emit_p[y].get(obs[t], MIN_FLOAT)
        # t时刻状态为y的最大概率(从t-1时刻中选择到达时刻t且状态为y的状态y0)
            (prob, state) = max([(V[t - 1][y0] + trans_p[y0].get(y, MIN_FLOAT) + em_p, y0) for y0 in PrevStatus[y]])
            V[t][y] = prob
            new_path[y] = path[state] + [y] # 只保存概率最大的一种路径
        path = new_path
        # 求出最后一个字哪一种状态的对应概率最大，最后一个字只可能是两种情况：E(结尾)和S(独立词)  
    prob, state = max((V[len(obs) - 1][y], y) for y in 'ES')

    return prob, path[state]
