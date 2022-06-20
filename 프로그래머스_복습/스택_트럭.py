from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    passing = deque([])
    ans = 0
    sum_weight = 0
    passed = []
    
    for truck in truck_weights:
        
        while True:
            if not passing:
                sum_weight += truck
                passing.append(truck)
                ans += 1
                break
        
            elif len(passing) == bridge_length:
                tmp = passing.popleft()
                if truck != 0:
                    passed.append(tmp)
                    sum_weight -= tmp
            
            else:
                if truck + sum_weight <= weight:
                    sum_weight += truck
                    passing.append(truck)
                    ans += 1
                    break
        
                elif truck + sum_weight > weight:
                    passing.append(0)
                    ans += 1
    
    return ans + bridge_length

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))
    