def atm_minimum_time(N, P):
    # Pi 리스트를 오름차순으로 정렬
    P.sort()
    
    # 각 사람이 돈을 인출하는데 걸리는 시간의 합을 저장할 변수
    total_time = 0
    accumulated_time = 0
    
    for time in P:
        accumulated_time += time  # 앞 사람까지의 대기 시간을 누적
        total_time += accumulated_time  # 누적된 시간을 총합에 더함
    
    return total_time

# 입력 처리
N = int(input())
P = list(map(int, input().split()))

# 결과 출력
print(atm_minimum_time(N, P))
