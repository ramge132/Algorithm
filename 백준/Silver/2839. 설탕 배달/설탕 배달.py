def min_sugar_bags(N):
    for x in range(N // 5, -1, -1):  # 5킬로그램 봉지를 최대한 많이 사용
        remainder = N - 5 * x
        if remainder % 3 == 0:  # 나머지가 3으로 나누어 떨어지면
            return x + (remainder // 3)  # 총 봉지 수 (5킬로그램 봉지 수 + 3킬로그램 봉지 수)
    return -1  # 정확하게 N킬로그램을 만들 수 없는 경우

# 예제 입력
N = int(input())
print(min_sugar_bags(N))
