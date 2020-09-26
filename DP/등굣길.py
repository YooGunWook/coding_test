def solution(m, n, puddles):
    route = [[0] * (m + 1) for _ in range(n + 1)]
    route[1][1] = 1

    for n_route in range(1, n + 1):
        for m_route in range(1, m + 1):
            if m_route == 1 and n_route == 1:
                continue
            if [m_route, n_route] in puddles:
                route[n_route][m_route] = 0
            else:
                route[n_route][m_route] = route[n_route - 1][m_route] + route[n_route][m_route - 1]
    return route[n][m] % 1000000007