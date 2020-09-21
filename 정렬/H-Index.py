def solution(citations):

    h_index = []
    for count in citations:
        h_count = list(filter(lambda x: x >= count, citations))
        if len(h_count) < count:
            h_index.append(len(h_count))
        else:
            h_index.append(count)

    return max(h_index)
