def solution(triangle):
    for i_index in range(1, len(triangle)):
        for j_index in range(i_index + 1):
            if j_index == 0:
                triangle[i_index][j_index] += triangle[i_index - 1][j_index]
            elif j_index == i_index:
                triangle[i_index][j_index] += triangle[i_index - 1][j_index - 1]
            else:
                triangle[i_index][j_index] += max(
                    triangle[i_index - 1][j_index], triangle[i_index - 1][j_index - 1]
                )
    return max(triangle[-1])
