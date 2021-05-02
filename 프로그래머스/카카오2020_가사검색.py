import collections


class Node(object):
    def __init__(self, key, passnum=None):
        self.key = key  # character
        self.passnum = collections.defaultdict(int)  # 문장의 길이를 파악하기 위한 용도
        self.children = {}  # 각 char의 연결을 확인하는 용도
        self.isEnd = False


class Trie(object):
    def __init__(self):
        self.head = Node(key=None)

    def insert(self, input_string):
        # Trie에 input_string을 넣어줌
        cur_node = self.head  # 시작
        cur_node.passnum[len(input_string)] += 1  # 길이에 대한 정보
        for c in input_string:
            if c not in cur_node.children:  # char가 없으면 추가
                cur_node.children[c] = Node(key=c)  # 새로운 node 생성
            cur_node = cur_node.children[c]  # 현재 노드를 다음으로 변경
            cur_node.passnum[len(input_string)] += 1  # 해당 노드의 길이 정보 저장
        cur_node.isEnd = True

    def search(self, query):
        # query에 맞는 단어 수 반환
        cur_node = self.head
        for q in query:
            if q == "?":  # ?가 나오면 그 이상으로 탐색 하지 않음
                break
            if q in cur_node.children:  # 있으면 계속 탐색 진행
                cur_node = cur_node.children[q]
            else:
                return 0  # 없으면 0으로 변환

        return cur_node.passnum[len(query)]  # 최종적으로 해당 길이의 정보 확인


def solution(words, queries):
    ans = []
    trie = Trie()  # ?가 뒤에 있을 때
    r_trie = Trie()  # ?가 앞에 있을 때
    for word in words:
        trie.insert(word)
        r_trie.insert(word[::-1])
    tmp_res = {}  # 중복 쿼리있을 때 사용

    for idx, query in enumerate(queries):
        if query in tmp_res:
            ans.append(tmp_res[query])

        elif query[-1] == "?":
            res = trie.search(query)
            ans.append(res)
            tmp_res[query] = res

        else:
            res = r_trie.search(query[::-1])
            ans.append(res)
            tmp_res[query] = res

    return ans


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
query = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, query))
