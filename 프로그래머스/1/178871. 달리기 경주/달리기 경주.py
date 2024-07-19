def solution(players, callings):
    # 선수 이름을 키, 순서를 값으로 하는 딕셔너리 생성
    player_dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_dict[call]
        # 추월한 선수와 자리 바꾸기
        if idx > 0:
            # 앞의 선수와 위치를 바꾸기
            player_dict[players[idx - 1]], player_dict[players[idx]] = player_dict[players[idx]], player_dict[players[idx - 1]]
            # 선수 배열도 갱신
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
    
    return players
