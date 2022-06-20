from string import ascii_uppercase
import heapq


def solution(name):
    """
    heapq 기반 접근 (tree 기반)
    가장 작은 값을 기준으로 계속 추출해서 원하는 단어가 나올 때까지 수행
    모든 경우의 수를 전부 고려하면서도 짧은 시간 안에 만들어낼 수 있음.
    """
    move = [(-1, 1), (-1, -1), (0, 1), (0, -1), (1, 1), (1, -1)]
    alpha_list = list(ascii_uppercase)
    tmp = "A" * len(name)
    queue = [(0, 0, tmp)]
    heapq.heapify(queue)
    answer = 1e9
    idx = 0
    while queue:
        count, t_index, tmp_name = heapq.heappop(queue)
        if tmp_name == name:
            answer = min(answer, count)
            break

        for m_lr, m_ud in move:
            m_index = t_index + m_lr
            if m_lr != 0:
                if m_index < 0:
                    m_index = len(name) - 1
                elif m_index >= len(name):
                    m_index = 0
                m_count = count + 1
            elif m_lr == 0 and idx == 0:
                m_count = count
                if m_ud == -1:
                    idx += 1
            else:
                continue

            if tmp_name[m_index] == name[m_index]:
                if (m_count, m_index, tmp_name) in queue:
                    continue
                heapq.heappush(queue, (m_count, m_index, tmp_name))
            else:
                t_name = list(tmp_name)
                t_alpha_idx = alpha_list.index(tmp_name[m_index])
                m_alpha_idx = alpha_list.index(name[m_index])
                if m_ud == 1:
                    while t_alpha_idx != m_alpha_idx:
                        t_alpha_idx += 1
                        if t_alpha_idx == len(alpha_list):
                            t_alpha_idx = 0
                        m_count += 1
                else:
                    while t_alpha_idx != m_alpha_idx:
                        t_alpha_idx -= 1
                        if t_alpha_idx == -1:
                            t_alpha_idx = len(alpha_list) - 1
                        m_count += 1
                t_name[m_index] = alpha_list[m_alpha_idx]
                t_name = "".join(t_name)
                if (m_count, m_index, t_name) in queue:
                    continue
                heapq.heappush(queue, (m_count, m_index, t_name))

    return answer


if __name__ == "__main__":
    name = "ABAAAAAAAAABB"
    print(solution(name))
