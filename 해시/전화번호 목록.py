# sorting을 해서 가장 짧은 번호를 접두사로 설정
# pop을 써서 쓴 번호를 삭제하고 진행
# startswith 함수를 써서 찾는다

def solution(phone_book):
    phone_book = sorted(phone_book)
    first_num = phone_book[0]
    phone_book.pop(0)
    for phone_num in phone_book:
        if phone_num.startswith(first_num):
            return False
    return True