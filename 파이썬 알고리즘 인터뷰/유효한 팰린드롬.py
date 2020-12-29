# 영어, 숫자만 판별하기 때문에 따로 전처리 해줘야함
# 책에서는 isalnum() 사용함 -> 영문자 숫자 여부 판별함수
# 정규식을 통해 조회 없이 바로 처리 가능


def is_penlindrom(penlindrom: str) -> bool:
    penlindrom = penlindrom.lower()
    new_penlindrom = ""
    for string in penlindrom:
        if string.isalnum():
            new_penlindrom += string
    return new_penlindrom == new_penlindrom[::-1]


if __name__ == "__main__":
    penlindrom = "race a car"
    print(is_penlindrom(penlindrom))

