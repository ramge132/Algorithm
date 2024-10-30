def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = bin(a | b)[2:].zfill(n)
        row = row.replace('1','#').replace('0',' ')
        answer.append(row)

    return answer