def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_idx = 0
        flag = True
        for s in skill_tree:
            if s not in skill:
                continue
            if skill[skill_idx] != s:
                flag = False
                break
            else:
                skill_idx += 1
        if skill_idx == len(skill) or flag == True:
            answer += 1

    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))
