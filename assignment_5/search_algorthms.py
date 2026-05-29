import math
import random

class TicTacToe:
    def __init__(self, board=None, current_player=1):
        self.board = board if board else [0] * 9
        self.current_player = current_player

    def get_legal_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == 0]

    def make_move(self, move):
        new_board = list(self.board)
        new_board[move] = self.current_player
        return TicTacToe(new_board, -self.current_player)

    def is_terminal(self):
        return self.get_winner() is not None or len(self.get_legal_moves()) == 0

    def get_winner(self):
        win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_conds:
            if self.board[a] != 0 and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def evaluate(self):
        winner = self.get_winner()
        if winner is not None:
            return winner * 100
        score = 0
        win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_conds:
            line = [self.board[a], self.board[b], self.board[c]]
            if line.count(1) == 2 and line.count(0) == 1: score += 10
            if line.count(-1) == 2 and line.count(0) == 1: score -= 10
        return score

    def display(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        for i in range(0, 9, 3):
            print(f" {symbols[self.board[i]]} | {symbols[self.board[i+1]]} | {symbols[self.board[i+2]]} ")
            if i < 6:
                print("---+---+---")
        print()

def minimax(state, depth, is_maximizing):
    if state.is_terminal():
        winner = state.get_winner()
        return (winner * 10 if winner else 0), None

    best_move = None
    if is_maximizing:
        max_eval = -math.inf
        for move in state.get_legal_moves():
            eval_val, _ = minimax(state.make_move(move), depth + 1, False)
            if eval_val > max_eval:
                max_eval, best_move = eval_val, move
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in state.get_legal_moves():
            eval_val, _ = minimax(state.make_move(move), depth + 1, True)
            if eval_val < min_eval:
                min_eval, best_move = eval_val, move
        return min_eval, best_move

def alpha_beta(state, depth, alpha, beta, is_maximizing):
    if state.is_terminal():
        winner = state.get_winner()
        return (winner * 10 if winner else 0), None

    best_move = None
    if is_maximizing:
        max_eval = -math.inf
        for move in state.get_legal_moves():
            eval_val, _ = alpha_beta(state.make_move(move), depth + 1, alpha, beta, False)
            if eval_val > max_eval:
                max_eval, best_move = eval_val, move
            alpha = max(alpha, eval_val)
            if beta <= alpha: break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in state.get_legal_moves():
            eval_val, _ = alpha_beta(state.make_move(move), depth + 1, alpha, beta, True)
            if eval_val < min_eval:
                min_eval, best_move = eval_val, move
            beta = min(beta, eval_val)
            if beta <= alpha: break
        return min_eval, best_move

def heuristic_alpha_beta(state, depth, alpha, beta, is_maximizing, max_depth=3):
    if depth == max_depth or state.is_terminal():
        return state.evaluate(), None

    best_move = None
    if is_maximizing:
        max_eval = -math.inf
        for move in state.get_legal_moves():
            eval_val, _ = heuristic_alpha_beta(state.make_move(move), depth + 1, alpha, beta, False, max_depth)
            if eval_val > max_eval:
                max_eval, best_move = eval_val, move
            alpha = max(alpha, eval_val)
            if beta <= alpha: break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in state.get_legal_moves():
            eval_val, _ = heuristic_alpha_beta(state.make_move(move), depth + 1, alpha, beta, True, max_depth)
            if eval_val < min_eval:
                min_eval, best_move = eval_val, move
            beta = min(beta, eval_val)
            if beta <= alpha: break
        return min_eval, best_move

class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0
        self.visits = 0
        self.untried_moves = state.get_legal_moves()

    def uct_select_child(self):
        return max(self.children, key=lambda c: c.wins / c.visits + math.sqrt(2 * math.log(self.visits) / c.visits))

    def expand(self):
        move = self.untried_moves.pop()
        next_state = self.state.make_move(move)
        child_node = MCTSNode(next_state, parent=self, move=move)
        self.children.append(child_node)
        return child_node

    def simulate(self):
        current_state = self.state
        while not current_state.is_terminal():
            possible_moves = current_state.get_legal_moves()
            move = random.choice(possible_moves)
            current_state = current_state.make_move(move)
        return current_state.get_winner()

    def backpropagate(self, result):
        self.visits += 1
        if result == self.state.current_player * -1:
            self.wins += 1
        elif result == 0:
            self.wins += 0.5
        if self.parent:
            self.parent.backpropagate(result)

def mcts(root_state, iterations=1000):
    root = MCTSNode(root_state)
    for _ in range(iterations):
        node = root
        while not node.untried_moves and node.children:
            node = node.uct_select_child()
        if node.untried_moves:
            node = node.expand()
        result = node.simulate()
        node.backpropagate(result)
    return max(root.children, key=lambda c: c.visits).move

def test_algorithms():
    print("=== TEST 1: FINDING THE WINNING MOVE ===")
    print("Player X's turn. X has two in a row on the top. O has two in a row in the middle.")
    board_win = [1, 1, 0, -1, -1, 0, 0, 0, 0]
    state_win = TicTacToe(board=board_win, current_player=1)
    state_win.display()

    _, move_mm = minimax(state_win, 0, True)
    print(f"-> Minimax chose position: {move_mm}")
    state_win.make_move(move_mm).display()

    _, move_ab = alpha_beta(state_win, 0, -math.inf, math.inf, True)
    print(f"-> Alpha-Beta chose position: {move_ab}\n")


    print("=== TEST 2: BLOCKING THE OPPONENT ===")
    print("Player X's turn. O is threatening to win on the top row.")
    board_block = [-1, -1, 0, 1, 0, 0, 0, 0, 0]
    state_block = TicTacToe(board=board_block, current_player=1)
    state_block.display()

    _, move_hab = heuristic_alpha_beta(state_block, 0, -math.inf, math.inf, True, max_depth=2)
    print(f"-> Heuristic Alpha-Beta chose position to block: {move_hab}")
    state_block.make_move(move_hab).display()


    print("=== TEST 3: MONTE-CARLO TREE SEARCH ===")
    print("Empty board. Let MCTS play 1000 simulated games to pick the best starting move.")
    state_mcts = TicTacToe()
    state_mcts.display()

    move_mcts = mcts(state_mcts, iterations=1000)
    print(f"-> MCTS chose position: {move_mcts}")
    state_mcts.make_move(move_mcts).display()

if __name__ == "__main__":
    test_algorithms()
