def solution(cacheSize, cities):
    # 정보를 담을 캐시 리스트 생성
    cache = []
    count = 0
    # 우선 대소문자 구분을 안하기 때문에 모두 소문자로 바꿔준다.
    for i in cities:
        i = i.lower()
        
        # 만약 캐시사이즈가 0이면 캐시 안에 들어갈 수 없기 때문에 바로 count에 5를 더해준다.
        # continue를 통해 다음으로 넘어간다.
        if cacheSize == 0:
            count += 5
            continue
        
        # 특정 지역이 캐시 안에 없을 때
        if i not in cache:
            # 캐시가 제한된 캐시 사이즈보다 작으면 캐시에 저장하고 5를 더해준다
            if len(cache) < cacheSize:
                cache.append(i)
                count += 5
            # 캐시가 제한된 캐시 사이즈보다 크면 제일 처음에 있던 캐시를 지워주고 새로 갱신한 후 5 더해준다.
            else:
                cache.pop(0)
                cache.append(i)
                count += 5
        # 특정 지역이 캐시 안에 있을 경우
        # 캐시 안에 있는 특정 지역의 인덱스를 통해 뺀 후
        # 캐시에 업데이트 한 후 1을 더해준다. 
        else:
            cache.pop(cache.index(i))
            cache.append(i)
            count += 1
            
    return count