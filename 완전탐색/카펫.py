def solution(brown, yellow):
    brown_yellow = brown+yellow
    for height in range(3, int(brown_yellow/2) + 1):
        width = brown_yellow // height
        if width * height == brown_yellow:
            if width < height:
                continue
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
