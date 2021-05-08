def biggerIsGreater(w):
    list_w = list(w)
    i = len(w) - 1
    while i > 0 and list_w[i - 1] >= list_w[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    j = len(w) - 1
    while list_w[j] <= list_w[i - 1]:
        j -= 1
    print(list_w)
    list_w[i - 1], list_w[j] = list_w[j], list_w[i - 1]
    list_w[i:] = list_w[len(w) - 1 : i - 1 : -1]
    return "".join(list_w)
