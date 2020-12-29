def trapping_rain(heights: list) -> int:  # 투 포인터 활용 풀이
    volume = 0
    if not heights:
        return 0

    left, right = 0, len(heights) - 1  # 각 포인터를 지정해준다
    left_max, right_max = heights[left], heights[right]

    while left < right:
        left_max, right_max = (
            max(heights[left], left_max),
            max(heights[right], right_max),
        )  # 현재 왼쪽 오른쪽에서 가장 높은 값을 넣어준다.

        if left_max <= right_max:  # max값이 작은 것부터 옮겨서 가장 높은데 올라갈 때까지 진행한다.
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1
    return volume


def trapping_rain_stack(heights: list) -> int:  # 스택 풀이
    stack = []
    volume = 0

    for i_index in range(len(heights)):
        while stack and heights[i_index] > heights[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i_index - stack[-1] - 1
            waters = min(heights[i_index], heights[stack[-1]] - heights[top])
            volume += distance * waters

        stack.append(i_index)
    return volume


if __name__ == "__main__":
    print(trapping_rain_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

