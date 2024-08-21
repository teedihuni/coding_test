from collections import deque

def solution(bridge_length, weight, truck_weights):
    # truck은 초기에 주어진 순서대로 pass
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)  
    time = 0
    
    current_bridge_weight = 0
    
    while len(truck_weights) > 0 : # 모든 트럭이 지나갈때까지 while
        time += 1
        current_bridge_weight = current_bridge_weight - bridge.popleft() # 한칸씩 땡기기
        
        if current_bridge_weight + truck_weights[0] <= weight : # 현재 무게 측정
            current_bridge_weight = current_bridge_weight + truck_weights[0] # 현재 무게에 트럭 무게 추가
            bridge.append(truck_weights.popleft()) # 현재 다리에 트럭 추가
        else:
            bridge.append(0) # 무게 초과된거면 현재 트럭 지나갈때까지는 못올라오도록 
        
    time = time + bridge_length # 마지막 트럭이 지나갈때까지의 시간도 생각
    
    return time
    

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
solution(bridge_length, weight, truck_weights)