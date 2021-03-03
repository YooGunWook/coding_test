n = int(input())
light = list(map(int, input().split(" ")))
lights = {}
for i in range(0, len(light)):
    lights[i + 1] = light[i]

stus = int(input())
for _ in range(stus):
    sex, val = list(map(int, input().split(" ")))
    if sex == 1:
        while val <= len(lights):
            print(val)
            if lights[val] == "0":
                lights[val] = "1"
            elif lights[val] == "1":
                lights[val] = "0"
            val *= 2
    elif sex == 2:
        print(sex)
        right = val + 1
        left = val - 1
        while lights[right] == lights[left]:
            if lights[right] == 1 and lights[left] == 1:
                lights[right] = 0
                lights[left] = 0
            elif lights[right] == 0 and lights[left] == 0:
                lights[right] = 1
                lights[left] = 1
            right += 1
            left -= 1
            if right not in lights or left not in lights:
                break
        if lights[val] == 0:
            lights[val] = 1
        elif lights[val] == 1:
            lights[val] = 0

"".join(lights.values())
