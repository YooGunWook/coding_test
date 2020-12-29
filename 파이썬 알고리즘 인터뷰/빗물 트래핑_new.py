def solution(height: list) -> int:
    if not height:
        return 0

    volume = 0
    left_index, right_index = 0, len(height) - 1
    left_max, right_max = height[left_index], height[right_index]

    while left_index < right_index:
        left_max, right_max = (
            max(height[left_index], left_max),
            max(height[right_index], right_max),
        )
        if left_max <= right_max:
            volume += left_max - height[left_index]
            left_index += 1
        else:
            volume += right_max - height[right_index]
            right_index -= 1
    return volume


if __name__ == "__main__":
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution(nums)
    print(result)

