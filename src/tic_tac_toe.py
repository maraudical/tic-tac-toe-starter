# Simple Tic-Tac-Toe in Python
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from random import randint

colorama_init(True)

player_symbols: dict[int, str] = {
    0: 'X',
    1: 'O'
}
player_colors: dict[int, str] = {
    0: Fore.RED,
    1: Fore.CYAN
}

board_size: int = 3
board_size_sq: int = board_size * board_size
position_str_size: int = len(str(board_size_sq))
board_value: list[int] = [-1 for _ in range(board_size_sq)]
board: list[str] = [f"{Style.DIM}{str(i + 1): >{position_str_size}}{Style.RESET_ALL}" for i in range(board_size_sq)]
min_players: int = 1
max_players: int = min(len(player_symbols), len(player_colors))

def print_board():
    row_separator: str = f"+{("-" * position_str_size + "--+") * board_size}"
    print(row_separator)
    for row in [board[i:i+board_size] for i in range(0,board_size_sq,board_size)]:
        print(f"| {" | ".join(row)} |")
        print(row_separator)

def check_win() -> int:
    # Check rows and columns
    for i in range(board_size):
        if board_value[i * board_size] != -1 and all(board_value[i * board_size + j] == board_value[i * board_size] for j in range(board_size)):
            return board_value[i * board_size]
        if board_value[i] != -1 and all(board_value[j * board_size + i] == board_value[i] for j in range(board_size)):
            return board_value[i]
    # Check diagonals
    if board_value[0] != -1 and all(board_value[i * (board_size + 1)] == board_value[0] for i in range(board_size)):
        return board_value[0]
    if board_value[board_size - 1] != -1 and all(board_value[(i + 1) * (board_size - 1)] == board_value[board_size - 1] for i in range(board_size)):
        return board_value[board_size - 1]
    return -1

def play_game():
    print(f"{Style.BRIGHT}Welcome to Tic-Tac-Toe!{Style.RESET_ALL}\n")
    # Validate player count
    player_count: int = -1
    while not min_players <= player_count <= max_players:
        player_count_str = input(f"Enter the number of {Style.BRIGHT}Players{Style.RESET_ALL} ({Fore.GREEN}{min_players}-{max_players}{Fore.RESET}): ")
        player_count = int(player_count_str) if player_count_str.isnumeric() else -1

    print(f"Starting the game with {Fore.GREEN}{player_count}{Fore.RESET} {Style.BRIGHT}Player{"s" if player_count > 1 else ""}{Style.RESET_ALL}!\n")

    current_player: int = 0
    while True:
        print_board()
        position: int = -1
        
        while not (0 < position <= board_size_sq) or board_value[position - 1] != -1:
            if player_count <= 1 and current_player == 1:
                position = randint(1, board_size_sq)
                continue
            position_str = input(f"{Style.BRIGHT}Player{Style.RESET_ALL} {player_colors[current_player]}{current_player + 1}{Fore.RESET}, enter position ({Fore.GREEN}1-{board_size_sq}{Fore.RESET}): ")
            position = int(position_str) if position_str.isnumeric() else -1
        
        if player_count <= 1 and current_player == 1:
            print(f"{Style.DIM}Computer chose position {position}{Style.RESET_ALL}")
        board[position - 1] = f"{player_colors[current_player]}{player_symbols[current_player]: >{position_str_size}}{Fore.RESET}"
        board_value[position - 1] = current_player
        
        # Check for win
        winner: int = check_win()
        if winner != -1:
            print_board()
            print(f"{Style.BRIGHT}Player {player_colors[winner]}{winner + 1}{Fore.RESET} wins! Congratulations!{Style.RESET_ALL}")
            break

        current_player = (current_player + 1) % max(player_count, 2)
play_game()