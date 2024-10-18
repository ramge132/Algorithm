def d(n):
    return n + sum(map(int, str(n)))

max_num = 10000
self_numbers = set(range(1, max_num+1))

for i in range(1, max_num+1):
    generated =  d(i)
    if generated <= max_num:
        self_numbers.discard(generated)

for self_number in sorted(self_numbers):
    print(self_number)