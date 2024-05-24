def solution(name, yearning, photo):
    # 이름과 그리움 점수를 딕셔너리로 매핑
    yearning_dict = {n: y for n, y in zip(name, yearning)}
    
    # 각 사진의 추억 점수를 계산할 결과 리스트
    result = []
    
    # 각 사진에 대해 추억 점수를 계산
    for p in photo:
        score = 0
        for person in p:
            if person in yearning_dict:
                score += yearning_dict[person]
        result.append(score)
    
    return result
