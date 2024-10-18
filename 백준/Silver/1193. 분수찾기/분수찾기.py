X = int(input())

sum = 0
count = 0

while sum < X:
    count += 1
    sum += count

position_in_line = X - (sum - count)

if count % 2 == 0:
    # 짝수 대각선
    numerator = position_in_line
    denominator = count - position_in_line +1

else:
    numerator = count - position_in_line +1
    denominator = position_in_line


print(f"{numerator}/{denominator}")