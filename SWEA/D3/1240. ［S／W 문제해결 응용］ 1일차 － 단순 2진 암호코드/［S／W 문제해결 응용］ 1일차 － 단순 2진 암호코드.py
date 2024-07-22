# 단순2진암호코드 시간복잡도 O(T * N * M)
# T개의 테스트 케이스가 있을 때, 각 테스트 케이스마다 O(N * M) 
# O(N*M) = 매트릭스의 모든 행에 대해 오른쪽에서 왼쪽으로 56개의 비트를 찾는 작업


def decode_digit(bit_string):
    bit_patterns = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9,
    }
    return bit_patterns.get(bit_string, -1)  # 주어진 bit_string에 해당하는 숫자를 반환, 없으면 -1 반환

def check_valid_code(code):
    odd_sum = sum(code[i] for i in range(0, 8, 2))
    even_sum = sum(code[i] for i in range(1, 8, 2))

    return (odd_sum * 3 + even_sum) % 10 == 0  # 유효한 코드인지 확인, 10의 배수이면 True 반환, 아니면 False 반환

def find_code(matrix, M):
    for row in matrix:
        for j in range(M - 1, 55, -1):  # 오른쪽에서 왼쪽으로 암호코드 끝부분 찾기
            if row[j] == '1':  # 1을 찾으면
                return row[j-55:j+1]  # 56비트를 추출하여 반환

def process_code(bit_string):
    code = []
    for i in range(0, 56, 7): # 7비트 단위로 나누어 숫자로 변환
        digit = decode_digit(bit_string[i:i+7])
        if digit == -1:
            return []  # 유효하지 않은 패턴이면 빈 리스트 반환
        code.append(digit)  # 변환된 숫자를 코드 리스트에 추가
    return code

def main():
    T = int(input())
    
    for t in range(1, T + 1):
        N, M = map(int, input().split())
        matrix = [input().strip() for _ in range(N)]  # N개의 줄에 걸쳐 배열 입력 받기
        
        bit_string = find_code(matrix, M)  # 암호코드 부분을 추출

        if not bit_string:  # 암호코드를 찾지 못하면 0 출력
            print(f"#{t} 0")
            continue
        
        code = process_code(bit_string)  # 암호코드 56비트를 숫자 리스트로 변환
    
        if not code or not check_valid_code(code):  # 코드가 유효하지 않으면 0 출력
            print(f"#{t} 0")
        else:
            print(f"#{t} {sum(code)}")  # 코드가 유효하면 숫자의 합을 출력

if __name__ == "__main__":
    main()
