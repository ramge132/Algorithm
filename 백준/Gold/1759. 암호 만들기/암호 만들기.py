vowels = ['a','e','i','o','u']

def password(string, start):
    if len(string) == L:
        vowels_count = 0
        const_count = 0
        for char in string:
            if char in vowels:
                vowels_count += 1
            else:
                const_count += 1

        if vowels_count >= 1 and const_count >= 2:
            print(''.join(map(str, string)))
            return
        else:
            return

    for i in range(start, C):
        string.append(chars[i])
        password(string, i+1)
        string.pop()

L, C = map(int,input().split())
chars = input().split()
chars.sort()
visited = []
password([], 0)