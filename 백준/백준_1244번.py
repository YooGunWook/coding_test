import copy

n = int(input())
light = list(map(str, input().split(" ")))
lights = {}
for i in range(0, len(light)):
    lights[i + 1] = light[i]

stus = int(input())
for _ in range(stus):
    sex, val = list(map(int, input().split(" ")))
    if sex == 1:
        tmp_val = copy.deepcopy(val)
        while val <= n:
            if lights[val] == "0":
                lights[val] = "1"
            elif lights[val] == "1":
                lights[val] = "0"
            val += tmp_val
            
    elif sex == 2:
        if lights[val] == '0':
            lights[val] = '1'
        elif lights[val] == '1':
            lights[val] = '0'
        right = val + 1
        left = val - 1
        while right <= n and left >= 1 and lights[right] == lights[left]:
            if lights[right] == '1' and lights[left] == '1':
                lights[right] = '0'
                lights[left] = '0'
            elif lights[right] == '0' and lights[left] == '0':
                lights[right] = '1'
                lights[left] = '1'
            right += 1
            left -= 1
            
light = list(lights.values())
for i, e in enumerate(light[0:]):
    if i and not(i % 20):
        print()
    print(e, end=" ")


