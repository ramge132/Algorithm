# 초심자의 회문 (재귀) 시간 복잡도: O(N)
# 문자열의 양 끝에서 중앙으로 이동하면서 문자를 비교.
# 문자열의 길이가 N일 때, 최대 N/2번의 비교가 필요하므로 시간 복잡도는 O(N).

def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start+1, end-1)
    

def main():
    T = int(input())

    for t in range(1, T+1):
        string = input().strip()
        if is_palindrome(string, 0, len(string)-1):
            result = 1
        else:
            result = 0
        print(f"#{t} {result}")

if __name__ == "__main__":
    main()