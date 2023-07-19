board = [' '] * 9


def check_win(board_, player):
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in winning_patterns:
        if all(board_[i] == player for i in pattern):
            return True
    return False


def get_available_moves(board_):
    return [i for i in range(len(board_)) if board_[i] == ' ']


def evaluate(board_):
    ai_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pattern in ai_patterns:
        if board_[pattern[0]] == board_[pattern[1]] == 1 and board_[pattern[2]] == ' ':
            return 1

    for pattern in ai_patterns:
        if board_[pattern[0]] == board_[pattern[1]] == -1 and board_[pattern[2]] == ' ':
            return -1

    return 0


def minimax(board_, maximizing_player, alpha, beta):
    if check_win(board_, 1):
        return 1
    elif check_win(board_, -1):
        return -1
    elif len(get_available_moves(board_)) == 0:
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board_):
            board_[move] = 1
            eval = minimax(board_, False, alpha, beta)
            board_[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board_):
            board_[move] = -1
            eval = minimax(board_, True, alpha, beta)
            board_[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def ai_move(board_):
    best_eval = float('-inf')
    best_move = None
    for move in get_available_moves(board_):
        board_[move] = 1
        eval = minimax(board_, False, float('-inf'), float('inf'))
        board_[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    board_[best_move] = 1
    return best_move // 3, best_move % 3
