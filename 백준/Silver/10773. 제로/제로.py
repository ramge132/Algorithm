K = int(input())
lst = []

for _ in range(K):
    lst.append(int(input()))


def pop_num(lst, answer, mistake):
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

    return answer


print(pop_num(lst, 0, 0))
