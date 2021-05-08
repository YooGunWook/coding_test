import collections


def organizingContainers(container):
    container_dict = collections.defaultdict(int)  # 컨테이너별 용량
    number_dict = collections.defaultdict(int)  # 각 공의 개수
    for idx, contain in enumerate(container):
        value = sum(contain)
        container_dict[idx] = value
        for idx, num in enumerate(contain):
            number_dict[idx] += num
    if sorted(container_dict.values()) == sorted(
        number_dict.values()
    ):  # 둘이 sorting할 때 같으면 어떻게 바꾸던 가능한거임
        return "Possible"
    else:
        return "Impossible"
