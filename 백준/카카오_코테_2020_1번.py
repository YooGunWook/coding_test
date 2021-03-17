def solution(s):
    if len(s) == 1:
        return 1
    ans = 999999
    for danwi in range(1, (len(s) // 2) + 1):
        start = 0
        end = danwi
        numberCnt = 1
        danAns = 0
        while start < len(s):
            nextS = start + danwi
            nextE = end + danwi
            if s[start:end] == s[nextS:nextE]:
                numberCnt += 1
                start = nextS
                end = nextE
            elif s[start:end] != s[nextS:nextE]:
                if numberCnt != 1:
                    danAns += len(str(numberCnt))
                numberCnt = 1
                danAns += len(s[start:end])
                start = nextS
                end = nextE
        ans = min(ans, danAns)

    return ans
