import string


def designerPdfViewer(h, word):
    alpha = list(string.ascii_lowercase)
    value = 0
    for i in word:
        index = alpha.index(i)
        value = max(value, h[index])
    return value * len(word)