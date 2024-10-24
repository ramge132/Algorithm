def is_group_word(word):
    seen = set()
    previous_char = ''
    for char in word:
        if previous_char != char:
            if char in seen:
                return 0
            seen.add(char)
        previous_char = char

    return 1

N = int(input())
group_word_count = sum(1 for word in [input().strip() for _ in range(N)] if is_group_word(word))
print(group_word_count)