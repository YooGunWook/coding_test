import itertools

def find_all_possible_number():
    # 3자리 수로 만들 수 있는 모든 경우의 수를 뽑는다. 
    all_number = list(itertools.permutations(range(1,10),3))
    return all_number

# 하나씩 비교하면서 최적의 값을 찾아낸다.
def check_guess(guess, num):
    # baseball에 있는 값을 하나씩 빼준다. 
    guess_number = [int(i) for i in str(guess[0])]
    # strike와 ball 값을 뺴준다.
    guess_strike = guess[1] 
    guess_ball = guess[2]
    strike = 0
    ball = 0
    
    # 3자리 수이기 때문에 range(3)으로 해서 search를 한다. 
    for i in range(3):
        # i번쨰 숫자끼리 정확히 일치하면 strike에 +1을 해준다.
        if guess_number[i] == num[i]:
            strike += 1
            continue
        # i번째 숫자가 num 안에 있으면 ball에 +1을 해준다
        if guess_number[i] in num:
            ball += 1
    
    # 그래서 두개의 값이 같으면 True를 return 해준다. 
    if guess_strike == strike and guess_ball == ball:
        return True
    else:
        return False
    
def solution(baseball):
    all_number = find_all_possible_number()
    answer = 0
    # for문을 통해 전체를 조회한다. 
    for num in all_number:
        ans = True
        # False값이 나오면 ans에 False로 할당해준다.
        for guess in baseball:
            if check_guess(guess,num) == False:
                ans = False
        # True일 경우 answer에 1을 더해준다. 
        if ans == True:
            answer += 1
            print(num)
            
    return answer