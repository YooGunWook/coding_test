def solution(X, A):
    leaf_list = set()
    for idx, leaf in enumerate(A):
        leaf_list.add(leaf)
        if len(leaf_list) == X:
            return idx
    return -1