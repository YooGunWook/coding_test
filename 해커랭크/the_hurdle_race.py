def hurdleRace(k, height):
    max_height = max(height)
    if max_height <= k:
        return 0
    return max_height - k