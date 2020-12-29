def sum_largest(nums: list) -> int:
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    print(sum_largest([1, 4, 3, 2]))

