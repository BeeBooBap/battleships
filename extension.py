"""To visualise Battleships Game"""

from battleships import *


def generate_board(board):
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append("O")


def printer(board):
    print("    0 1 2 3 4 5 6 7 8 9")
    print("   --------------------")
    for r in range(0, 10):
        print(str(r) + " " + "|" + " " + " ".join(str(c) for c in board[r]))
    print()


def main():
    current_fleet = randomly_place_all_ships()
    current_board = []
    generate_board(current_board)
    game_over = False
    shots = 0
    check = False
    while not game_over:
        if check is False:
            print("\nWelcome to Battleships!\n")
            print("The aim of the game is to shoot down the enemy ships with as little shots as possible!\n")
            print("If you want to quit the game, press the 'Q' key.\n")
            print("If you want to view your shots, type 'shots'.\n")
            starter = input("Press enter to begin!")
            if starter.upper() == "Q":
                game_over = True
            check = True
        loc_str = input("\nEnter row and column to shoot (separated by space): ").split()
        if len(loc_str) != 2:
            if not loc_str:
                print("\nPlease input two numbers separated by a space. Try again.")
            else:
                if loc_str[0].upper() == "Q":
                    print("\nGame over! You required", shots, "shots.")
                    print("\nThank you for playing.")
                    game_over = True
                else:
                    print("\nPlease input two numbers separated by a space. Try again.")
        elif loc_str[0].isdigit() and loc_str[1].isdigit():
            if (9 >= int(loc_str[0]) >= 0) and (9 >= int(loc_str[1]) >= 0):
                current_row = int(loc_str[0])
                current_column = int(loc_str[1])
                shots += 1
                if check_if_hits(current_row, current_column, current_fleet):
                    current_board[current_row][current_column] = "X"
                    print("\n")
                    printer(current_board)
                    print("\nYou have a hit!")
                    (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                    if is_sunk(ship_hit):
                        for (row, column) in ship_hit[4]:
                            if ship_hit[3] == 4:
                                current_board[row][column] = "B"
                            if ship_hit[3] == 3:
                                current_board[row][column] = "C"
                            if ship_hit[3] == 2:
                                current_board[row][column] = "D"
                            if ship_hit[3] == 1:
                                current_board[row][column] = "S"
                        print("\n")
                        printer(current_board)
                        print("\nYou sank a " + ship_type(ship_hit) + "!")
                else:
                    if not check_if_already_hits(current_row, current_column, current_fleet):
                        current_board[current_row][current_column] = "-"
                    print("\n")
                    printer(current_board)
                    print("\nYou missed!")
            else:
                print("\nPlease input two numbers between 0 and 9. Try again.")
        else:
            print("\nPlease input two numbers between 0 and 9. Try again.")

        if not are_unsunk_ships_left(current_fleet):
            print("\nGame over! You required", shots, "shots.")
            print("\nThank you for playing.")
            end = input("\nPress any key to quit: ")
            if end.upper() == "Q":
                game_over = True
            else:
                game_over = True


if __name__ == '__main__':
    main()
