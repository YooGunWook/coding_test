def summation(nums: list) -> list:
    nums.sort()
    result = []
    for i_index in range(len(nums) - 2):
        if i_index > 0 and nums[i_index] == nums[i_index - 1]:
            continue
        left, right = i_index + 1, len(nums) - 1
        while left < right:
            sum = nums[i_index] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i_index], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


if __name__ == "__main__":
    print(summation([-1, 0, 1, 2, -1, -4]))

