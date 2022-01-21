data = input()
players_pool = {}
player_total_points = {}
sort_positions = {}
while data != "Season end":
    if "->" in data:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if player not in players_pool:
            players_pool[player] = {position: skill}
        if position not in players_pool[player]:
            players_pool[player].update({position: skill})
        else:
            if skill > players_pool[player][position]:
                players_pool[player][position] = skill
    for player, v in players_pool.items():
        total_points = 0
        for poss, pnt in v.items():
            total_points += pnt
        player_total_points[player] = total_points
    if "vs" in data:
        player_one, player_two = data.split(" vs ")
        if player_one and player_two in players_pool:
            for current_position, value in players_pool[player_one].items():
                if current_position in players_pool[player_two]:
                    if player_total_points[player_one] > player_total_points[player_two]:
                        del players_pool[player_two]
                        del player_total_points[player_two]
                        break
                    elif player_total_points[player_one] < player_total_points[player_two]:
                        del players_pool[player_one]
                        del player_total_points[player_one]
                        break

    data = input()

sort_total_points = sorted(player_total_points.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for player, v in players_pool.items():
    sort_positions[player] = sorted(v.items(), key=lambda kvp: (-kvp[1], kvp[1]))
for player in sort_total_points:
    print(f"{player[0]}: {player[1]} skill")
    for p, v in sort_positions.items():
        if p == player[0]:
            for i in v:
                print(f"- {i[0]} <::> {i[1]}")
