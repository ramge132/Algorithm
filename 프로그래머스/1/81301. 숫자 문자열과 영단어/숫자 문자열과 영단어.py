sheet = {
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

def solution(s):
    lst = []
    result = []
    for char in s:
        if char.isalpha():
            lst.append(char)
            word = ''.join(lst)
            if word in sheet:
                result.append(sheet[word])
                lst = []
        else:
            result.append(int(char))

    return int(''.join(map(str, result)))
