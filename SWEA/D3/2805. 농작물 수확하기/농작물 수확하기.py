# 농장문제 시간 복잡도: O(N^2)
# N x N 크기의 농장을 순회하면서 마름모 형태로 농작물의 수익을 더함. 
# 모든 농장의 칸을 한 번씩 검사하기 때문에 시간 복잡도는 N x N, 즉 O(N^2).

def harvest_profit(test_cases):
    results = []
    
    for idx, (N, farm) in enumerate(test_cases):
        mid = N // 2
        profit = 0
        
        for i in range(N):
            start = abs(mid - i)
            end = N - start
            profit += sum(farm[i][start:end])
        
        results.append(f"#{idx+1} {profit}")
    
    return results
    
def main():
    T = int(input())
    test_cases = []
    
    for _ in range(T):
        N = int(input())
        farm = []
        for _ in range(N):
            row = list(map(int, list(input())))
            farm.append(row)
        test_cases.append((N, farm))
    
    results = harvest_profit(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

""" 
첫 번째 행 (i=0):
start = abs(2 - 0) = 2
end = 5 - 2 = 3
더할 값: (인덱스 2부터 3전까지)

두 번째 행 (i=1):
start = abs(2 - 1) = 1
end = 5 - 1 = 4
더할 값: (인덱스 1부터 4전까지)

세 번째 행 (i=2):
start = abs(2 - 2) = 0
end = 5 - 0 = 5
더할 값: (인덱스 0부터 5전까지)
네 번째 행 (i=3):

start = abs(2 - 3) = 1
end = 5 - 1 = 4
더할 값: (인덱스 1부터 4전까지)

다섯 번째 행 (i=4):
start = abs(2 - 4) = 2
end = 5 - 2 = 3
더할 값: (인덱스 2부터 3전까지)  
"""