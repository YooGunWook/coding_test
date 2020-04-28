from datetime import datetime
def full_melody_maker(new_musicinfos):
    
    # dict 형태로 노래별 얼마나 음이 나왔는지 체크한다. 
    full_melody = {}
    for i in range(0,len(new_musicinfos)):
        start = datetime.strptime(new_musicinfos[i][0],'%H:%M')
        end = datetime.strptime(new_musicinfos[i][1],'%H:%M')
        duration =int((end-start).total_seconds()/60)
        m = new_musicinfos[i][3]
        # #으로 구분된 음들은 소문자로 바꿔준다. 
        m = m.replace('C#','c')
        m = m.replace('D#','d')
        m = m.replace('F#','f')
        m = m.replace('G#','g')
        m = m.replace('A#','a')
        m = m*(duration//len(m))+m[0:duration%len(m)]
        full_melody.update({m:new_musicinfos[i][2]})
        
        
    return full_melody

# 이것도 마찬가지로 소문자로 바꿔준다. 
def melody_good(m):
    m = m.replace('C#','c')
    m = m.replace('D#','d')
    m = m.replace('F#','f')
    m = m.replace('G#','g')
    m = m.replace('A#','a')
    return m


def solution(m, musicinfos):
    
    # 초기 값
    result = None
    new_musicinfos = []
    for i in musicinfos:
        new_musicinfos.append(i.split(','))
        
    sing_melody = full_melody_maker(new_musicinfos)
    
    count_melody = {}
    m = melody_good(m)
    

    for i in sing_melody:
        if m in i:
            # 만약에 m이 i안에 있을 경우
            # 두가지로 나눈다 -> None인 경우와 아닌 경우
            if result == None:
                result = i
            # result의 길이와 i의 길이를 비교해서 더 긴 것으로 바꿔준다.
            else:
                if len(result) < len(i):
                    result = i

    # none이 아니면 sing_melody에 넣고 아니면 none으로 처리             
    if result != None:
        return sing_melody[result]
    else:
        return "(None)"