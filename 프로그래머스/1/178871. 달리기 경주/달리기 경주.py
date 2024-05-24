def solution(players, callings):
    player_positions = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        current_position = player_positions[calling]
        if current_position > 0:
            previous_player = players[current_position - 1]
            players[current_position - 1], players[current_position] = players[current_position], players[current_position - 1]
            player_positions[calling] -= 1
            player_positions[previous_player] += 1
            
    return players
