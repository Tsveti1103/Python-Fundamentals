def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_side = ticket[:10]
    right_side = ticket[10:]
    win_symbols = ['@', '#', '$', '^']
    for win in win_symbols:
        for num in range(10, 0, -1):
            you_win = win * num
            if you_win in left_side and you_win in right_side:
                if num == 10:
                    return f'ticket "{ticket}" - {num}{win} Jackpot!'
                elif 6 <= num <= 9:
                    return f'ticket "{ticket}" - {num}{win}'
    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]
tickets_state = []
for ticket in tickets:
    tickets_state.append(is_winning(ticket))
for result in tickets_state:
    print(result)
