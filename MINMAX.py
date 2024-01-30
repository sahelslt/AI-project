import random

def get_children(board, players):
    children = []
    target = board[-1]
    for player in players:
        if player != target:
            new_players = players.copy()
            new_players[players.index(player)] = target
            new_players[players.index(target)] = player
            for i in range(1, 10001):
                if i not in new_players:
                    children.append((new_players[:], i))
    return children

def evaluate_board(board, target):
    players, last_player = board[:-1], board[-1]
    min_distance = min(abs(p - target) for p in players)
    if abs(last_player - target) < min_distance:
        return 1
    elif abs(last_player - target) > min_distance:
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing_player, alpha, beta, target):
    if depth == 0 or game_is_over(board):
        return evaluate_board(board, target)

    if is_maximizing_player:
        max_eval = float('-inf')
        for child_board in get_children(board, board[-1]):
            eval = minimax(child_board, depth - 1, False, alpha, beta, target)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for child_board in get_children(board, board[-1]):
            eval = minimax(child_board, depth - 1, True, alpha, beta, target)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def game_is_over(board):
    return len(board) == 2

def find_best_move(board, target, depth=5):
    best_eval = float('-inf')
    best_move = None
    for move in get_children(board, board[-1]):
        eval = minimax(move, depth, True, float('-inf'), float('inf'), target)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def play_game(num_players, depth=5):
    players = [(i+1, int(input(f"Enter the number for player {i+1}: "))) for i in range(num_players)]
    target = random.randint(1, 100)
    print(f"Target number: {target}")
    board = (players, random.choice(players))
    while not game_is_over(board):
        best_move = find_best_move(board, target, depth)
        board = best_move
    print(f"The winner is player {board[-1][0]}")

num_players = int(input("Enter the number of players: "))
play_game(num_players)
