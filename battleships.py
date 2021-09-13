"""Implementation for Battleships Game against computer"""

import random

board = []

for i in range(10):
    """Generates the board but does not print, required for use of get_board()"""
    board.append([])
    for j in range(10):
        board[i].append("O")


def is_sunk(ship):  # (row, column, horizontal, length, {hits})
    """Checks if a ship is sunk by looking at the elements in the set and comparing them to the initial
    coordinates with length and horizontal"""
    count = 0
    length = ship[3]
    horizontal = ship[2]
    check = True
    while count < length:
        if horizontal:
            if (ship[0], ship[1] + count) in ship[4]:
                check = True
                count += 1
            else:
                return False
        else:
            if (ship[0] + count, ship[1]) in ship[4]:
                check = True
                count += 1
            else:
                return False
    return check


def ship_type(ship):
    if ship[3] == 4:
        return "battleship"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3] == 1:
        return "submarine"


def get_board(fleet):
    """Generates a board to compare fleet on, required for use of is_open_sea() and ok_to_place_ship_at()"""
    if not fleet:
        return board
    else:
        i = 0
        while i < len(fleet):
            row = fleet[i][0]
            col = fleet[i][1]
            horizontal = fleet[i][2]
            length = fleet[i][3]
            if horizontal:
                for j in range(col, col + length):
                    board[row][j] = "X"
            else:
                for j in range(row, row + length):
                    board[j][col] = "X"
            i += 1
    return board


def is_open_sea(row, column, fleet):
    """checks if the square and surrounding squares given by row and column are empty on board where fleet is"""
    get_board(fleet)  # generates board with current fleet marked
    x = row - 1
    y = row + 2
    m = column - 1
    n = column + 2
    if row == 9:
        y = row + 1
    if row == 0:
        x = row
    if column == 9:
        n = column + 1
    if column == 0:
        m = column
    for i in range(x, y):
        for j in range(m, n):
            if board[i][j] != "O":
                return False
    return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """checks if squares on and surrounding some ship in fleet are empty"""
    i = 1
    if length == 2:
        i = 2
    if length == 3:
        i = 3
    if length == 4:
        i = 4
    if horizontal:
        if column + (length - 1) > 9:  # checks the ship does not fall off the board
            return False
        else:
            for num in range(0, i):
                if is_open_sea(row, column + num, fleet) is False:
                    return False
    else:
        if row + (length - 1) > 9:
            return False
        else:
            for num in range(0, i):
                if is_open_sea(row + num, column, fleet) is False:
                    return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    """Builds a fleet with specified coordinates"""
    ship = (row, column, horizontal, length, set())
    fleet.append(ship)
    return fleet


def random_num():
    """Generates a random coordinate"""
    return random.randint(0, 9)


def random_bool():
    """Generates a random boolean for horizontal"""
    return bool(random.getrandbits(1))


def randomly_place_all_ships():
    """Uses the random functions to build a legal fleet with random coordinates"""
    fleet = []
    i = 0
    while i < 1:
        row = random_num()
        col = random_num()
        h = random_bool()
        if ok_to_place_ship_at(row, col, h, 4, fleet) is True:
            place_ship_at(row, col, h, 4, fleet)
            i += 1
    j = 0
    while j < 2:
        row = random_num()
        col = random_num()
        h = random_bool()
        if ok_to_place_ship_at(row, col, h, 3, fleet) is True:
            place_ship_at(row, col, h, 3, fleet)
            j += 1
    k = 0
    while k < 3:
        row = random_num()
        col = random_num()
        h = random_bool()
        if ok_to_place_ship_at(row, col, h, 2, fleet) is True:
            place_ship_at(row, col, h, 2, fleet)
            k += 1
    l = 0
    while l < 4:
        row = random_num()
        col = random_num()
        h = random_bool()
        if ok_to_place_ship_at(row, col, h, 1, fleet) is True:
            place_ship_at(row, col, h, 1, fleet)
            l += 1
    return fleet


def check_if_hits(row, column, fleet):
    """checks if row and column entered by human hits any of the ships in fleet"""
    check = False
    for ship in fleet:
        if (row, column) in ship[4]:
            return False
        if (ship[0], ship[1]) == (row, column):
            check = True
        elif ship[2] is True:
            for i in range(ship[3]):
                if row == ship[0] and column == ship[1] + i:
                    check = True
        elif ship[2] is False:
            for i in range(ship[3]):
                if row == ship[0] + i and column == ship[1]:
                    check = True
    return check


def check_if_already_hits(row, column, fleet):
    """Checks if row and column have already been input and have hit a ship in fleet"""
    for ship in fleet:
        if (row, column) in ship[4]:
            return True


def hit(row, column, fleet):
    """Returns new fleet with hits for the ship that was hit,also returns which ship was hit"""
    for ship in fleet:
        if (ship[0], ship[1]) == (row, column):
            x = ship
        elif ship[2] is True:
            for i in range(ship[3]):
                if row == ship[0] and column == ship[1] + i:
                    x = ship
        elif ship[2] is False:
            for i in range(ship[3]):
                if row == ship[0] + i and column == ship[1]:
                    x = ship
    x[4].add((row, column))
    fleet1 = []
    for el in fleet:
        if el != x:
            fleet1.append(el)
        else:
            fleet1.append(x)
    return fleet1, x


def are_unsunk_ships_left(fleet):
    """Checks if there are any remaining ships in fleet not sunk"""
    for ship in fleet:
        if len(ship[4]) < ship[3]:
            return True
    return False


def main():
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0
    check = False
    while not game_over:
        if check is False:
            print("\nWelcome to Battleships!\n")
            print("The aim of the game is to shoot down the enemy ships with as little shots as possible!\n")
            print("If you want to quit the game, press the 'Q' key.\n")
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
                    print("\nYou have a hit!")
                    (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                    if is_sunk(ship_hit):
                        print("\nYou sank a " + ship_type(ship_hit) + "!")
                else:
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
