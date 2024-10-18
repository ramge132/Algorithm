
K = int(input())
lst = []
result = 0

for _ in range(K):
    lst.append(int(input()))

mistake = 0
answer = 0

def pop_num(lst):
    global mistake
    global answer

    while lst:
        num = lst.pop()

        if num != 0 and mistake > 0:
            mistake -= 1

        elif num == 0 and mistake > 0:
            mistake += 1

        elif num != 0 and mistake == 0 :
            answer += num

        elif num == 0 and mistake == 0:
            mistake += 1



pop_num(lst)

print(answer)
