
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.

    to_Player1 = [[['-']*10 for i in range(10)] for r in range(2)]  # used list comprehension to form two different 3d lists: one to show player1 and the other for player2 until the end of the game
    to_Player2 = [[['-']*10 for i in range(10)] for r in range(2)]
    turn = 0
    for i in range(1,3):  # placement phase
        Remaining_Ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        while i == 1:
            print_3d_list(to_Player1)
            while len(Remaining_Ships) == 0:  # this block will ask the player if they confirm the placement when they have no more ships to place
                print_confirm_placement()
                ans = input()
                if ans.lower() == 'y':
                    break
                elif ans.lower() == 'n':
                    Remaining_Ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']  # first, set the Remaining_Ships back to its original value
                    to_Player1 = [[['-'] * 10 for i in range(10)] for r in range(2)]  # then, set the 3d list that the player will place the new set of ships back to the empty grid
                    print_3d_list(to_Player1)
            if len(Remaining_Ships) == 0:  # after the while loop that repeatedly asks the player if they confirm the placement, if they still have no ships to place, i.e. they answered 'y', it is now player2's turn. So we break the loop
                break
            print_ships_to_be_placed()
            for el in Remaining_Ships:  # since print_single_element() takes one input and prints it, we should run it multiple times to print the ships one by one
                print_single_element(el)
            print_empty_line()
            print_player_turn_to_place(i)
            print_to_place_ships()
            x = input().split()  # input will be a single string containing 4 values, seperated by whitespaces. We should separate them and put each value in a container separately.
            if len(x) < 4:
                print_incorrect_input_format()
                continue
            try:  # if the second and third elements are not ints, this will cause the except part to run.
                x[1] = int(x[1])
                x[2] = int(x[2])
            except:
                print_incorrect_input_format()
                continue
            if x[1] > 10 or x[1] < 1 or x[2] > 10 or x[2] < 1:  # the grid is 10x10, and the player cannot place the ships outside.
                print_incorrect_coordinates()
                continue
            if x[0].lower() == 'carrier':  # case insensitive input, so we need to use .lower() to compare it with the desired values.
                if x[3] == 'h':
                    if 'Carrier' not in Remaining_Ships:
                        print_ship_is_already_placed('Carrier')
                    elif x[2] > 10 or x[1] > 6:  # the ship is 5 units long, so x[1] should not exceed 6.
                        print_ship_cannot_be_placed_outside('Carrier')
                    else:
                        if to_Player1[0][x[2] - 1][x[1]-1:x[1] + 5 - 1] != ['-' for i in range(5)]:  # took a part of player1's grid, then compared it to a list of five '-'s to see if the locations are occupied.
                            print_ship_cannot_be_placed_occupied('Carrier')
                            continue  # continue is placed here to dodge the part that removes the ship from Remaining_Ships
                        else:
                            to_Player1[0][x[2] - 1][x[1]-1:x[1] + 5 - 1] = ['#' for i in range(5)]  # if there are no obstacles on the way, change the relevant parts to # (place the ship there)
                        Remaining_Ships.remove('Carrier')  # we also need to remove the ship if we managed to place it.
                elif x[3] == 'v':
                    if 'Carrier' not in Remaining_Ships:
                        print_ship_is_already_placed('Carrier')
                    elif x[2] > 6 or x[1] > 10:  # the ship is 5 units long, so x[2] should not exceed 6.
                        print_ship_cannot_be_placed_outside('Carrier')
                    else:
                        if [to_Player1[0][x[2] - 1 + i][x[1] - 1] for i in range(5)] != ['-' for i in range(5)]:  # take the x[1] - 1 indexed value of each row, then form a list of them and compare the list with a 5 units long list of '-'
                            print_ship_cannot_be_placed_occupied('Carrier')
                            continue
                        else:
                            for gru in range(5):
                                to_Player1[0][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Carrier')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'battleship':  # case insensitive input, so we need to use .lower() to compare it with the desired values.
                if x[3] == 'h':
                    if 'Battleship' not in Remaining_Ships:
                        print_ship_is_already_placed('Battleship')
                    elif x[2] > 10 or x[1] > 7:  # the ship is 4 units long, so x[1] should not exceed 7.
                        print_ship_cannot_be_placed_outside('Battleship')
                    else:
                        if to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 4 - 1] != ['-' for i in range(4)]:  # took a part of player1's grid, then compared it to a list of four '-'s to see if the locations are occupied.
                            print_ship_cannot_be_placed_occupied('Battleship')
                            continue  # continue is placed here to dodge the part that removes the ship from Remaining_Ships
                        else:
                            to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 4 - 1] = ['#' for i in range(4)] # if there are no obstacles on the way, change the relevant parts to # (place the ship there)
                        Remaining_Ships.remove('Battleship')  # we also need to remove the ship if we managed to place it.
                elif x[3] == 'v':
                    if 'Battleship' not in Remaining_Ships:
                        print_ship_is_already_placed('Battleship')
                    elif x[2] > 7 or x[1] > 10:  # the ship is 4 units long, so x[2] should not exceed 7.
                        print_ship_cannot_be_placed_outside('Battleship')
                    else:
                        if [to_Player1[0][x[2] - 1 + i][x[1] - 1] for i in range(4)] != ['-' for i in range(4)]:  # take the x[1] - 1 indexed value of each row, then form a list of them and compare the list with a 4 units long list of '-'
                            print_ship_cannot_be_placed_occupied('Battleship')
                            continue
                        else:
                            for gru in range(4):
                                to_Player1[0][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Battleship')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'cruiser':  # case insensitive input, so we need to use .lower() to compare it with the desired values.
                if x[3] == 'h':
                    if 'Cruiser' not in Remaining_Ships:
                        print_ship_is_already_placed('Cruiser')
                    elif x[2] > 10 or x[1] > 8:  # the ship is 3 units long, so x[1] should not exceed 8.
                        print_ship_cannot_be_placed_outside('Cruiser')
                    else:
                        if to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 3 - 1] != ['-' for i in range(3)]:  # took a part of player1's grid, then compared it to a list of three '-'s to see if the locations are occupied.
                            print_ship_cannot_be_placed_occupied('Cruiser')
                            continue  # continue is placed here to dodge the part that removes the ship from Remaining_Ships
                        else:
                            to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 3 - 1] = ['#' for i in range(3)]  # if there are no obstacles on the way, change the relevant parts to # (place the ship there)
                        Remaining_Ships.remove('Cruiser')  # we also need to remove the ship if we managed to place it.
                elif x[3] == 'v':
                    if 'Cruiser' not in Remaining_Ships:
                        print_ship_is_already_placed('Cruiser')
                    elif x[2] > 8 or x[1] > 10:  # the ship is 3 units long, so x[2] should not exceed 8.
                        print_ship_cannot_be_placed_outside('Cruiser')
                    else:
                        if [to_Player1[0][x[2] - 1 + i][x[1] - 1] for i in range(3)] != ['-' for i in range(3)]:  # take the x[1] - 1 indexed value of each row, then form a list of them and compare the list with a 3 units long list of '-'
                            print_ship_cannot_be_placed_occupied('Cruiser')
                            continue
                        else:
                            for gru in range(3):
                                to_Player1[0][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Cruiser')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'submarine':  # case insensitive input, so we need to use .lower() to compare it with the desired values.
                if x[3] == 'h':
                    if 'Submarine' not in Remaining_Ships:
                        print_ship_is_already_placed('Submarine')
                    elif x[2] > 10 or x[1] > 8:  # the ship is 3 units long, so x[1] should not exceed 8.
                        print_ship_cannot_be_placed_outside('Submarine')
                    else:
                        if to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 3 - 1] != ['-' for i in range(3)]:  # took a part of player1's grid, then compared it to a list of three '-'s to see if the locations are occupied.
                            print_ship_cannot_be_placed_occupied('Submarine')
                            continue  # continue is placed here to dodge the part that removes the ship from Remaining_Ships
                        else:
                            to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 3 - 1] = ['#' for i in range(3)]  # if there are no obstacles on the way, change the relevant parts to # (place the ship there)
                        Remaining_Ships.remove('Submarine')  # we also need to remove the ship if we managed to place it.
                elif x[3] == 'v':
                    if 'Submarine' not in Remaining_Ships:
                        print_ship_is_already_placed('Submarine')
                    elif x[2] > 8 or x[1] > 10:  # the ship is 3 units long, so x[2] should not exceed 8.
                        print_ship_cannot_be_placed_outside('Submarine')
                    else:
                        if [to_Player1[0][x[2] - 1 + i][x[1] - 1] for i in range(3)] != ['-' for i in range(3)]:  # take the x[1] - 1 indexed value of each row, then form a list of them and compare the list with a 3 units long list of '-'
                            print_ship_cannot_be_placed_occupied('Submarine')
                            continue
                        else:
                            for gru in range(3):
                                to_Player1[0][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Submarine')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'destroyer':  # case insensitive input, so we need to use .lower() to compare it with the desired values.
                if x[3] == 'h':
                    if 'Destroyer' not in Remaining_Ships:
                        print_ship_is_already_placed('Destroyer')
                    elif x[2] > 10 or x[1] > 9:  # the ship is 2 units long, so x[1] should not exceed 9.
                        print_ship_cannot_be_placed_outside('Destroyer')
                    else:
                        if to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 2 - 1] != ['-' for i in range(2)]:  # took a part of player1's grid, then compared it to a list of two '-'s to see if the locations are occupied.
                            print_ship_cannot_be_placed_occupied('Destroyer')
                            continue  # continue is placed here to dodge the part that removes the ship from Remaining_Ships
                        else:
                            to_Player1[0][x[2] - 1][x[1] - 1:x[1] + 2 - 1] = ['#' for i in range(2)]  # if there are no obstacles on the way, change the relevant parts to # (place the ship there)
                        Remaining_Ships.remove('Destroyer')  # we also need to remove the ship if we managed to place it.
                elif x[3] == 'v':
                    if 'Destroyer' not in Remaining_Ships:
                        print_ship_is_already_placed('Destroyer')
                    elif x[2] > 9 or x[1] > 10:  # the ship is 2 units long, so x[2] should not exceed 9.
                        print_ship_cannot_be_placed_outside('Destroyer')
                    else:
                        if [to_Player1[0][x[2] - 1 + i][x[1] - 1] for i in range(2)] != ['-' for i in range(2)]:  # take the x[1] - 1 indexed value of each row, then form a list of them and compare the list with a 2 units long list of '-'
                            print_ship_cannot_be_placed_occupied('Destroyer')
                            continue
                        else:
                            for gru in range(2):
                                to_Player1[0][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Destroyer')
                else:
                    print_incorrect_orientation()
            else:
                print_incorrect_ship_name()
# everything for the next while loop is the same as the previous one, player2 forms the grid in the same way.
        while i == 2:
            print_3d_list(to_Player2)
            while len(Remaining_Ships) == 0:
                print_confirm_placement()
                ans = input()
                if ans.lower() == 'y':
                    break
                elif ans.lower() == 'n':
                    Remaining_Ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine','Destroyer']
                    to_Player2 = [[['-'] * 10 for i in range(10)] for r in range(2)]
                    print_3d_list(to_Player2)
            if len(Remaining_Ships) == 0:
                break
            print_ships_to_be_placed()
            for el in Remaining_Ships:
                print_single_element(el)
            print_empty_line()
            print_player_turn_to_place(i)
            print_to_place_ships()
            x = input().split()
            if len(x) < 4:
                print_incorrect_input_format()
                continue
            try:
                x[1] = int(x[1])
                x[2] = int(x[2])
            except:
                print_incorrect_input_format()
                continue
            if x[1] > 10 or x[1] < 1 or x[2] > 10 or x[2] < 1:
                print_incorrect_coordinates()
                continue
            if x[0].lower() == 'carrier':
                if x[3] == 'h':
                    if 'Carrier' not in Remaining_Ships:
                        print_ship_is_already_placed('Carrier')
                    elif x[2] > 10 or x[1] > 6:
                        print_ship_cannot_be_placed_outside('Carrier')
                    else:
                        if to_Player2[1][x[2] - 1][x[1]-1:x[1] + 5 - 1] != ['-' for i in range(5)]:
                            print_ship_cannot_be_placed_occupied('Carrier')
                            continue
                        else:
                            to_Player2[1][x[2] - 1][x[1]-1:x[1] + 5 - 1] = ['#' for i in range(5)]
                        Remaining_Ships.remove('Carrier')
                elif x[3] == 'v':
                    if 'Carrier' not in Remaining_Ships:
                        print_ship_is_already_placed('Carrier')
                    elif x[2] > 6 or x[1] > 10:
                        print_ship_cannot_be_placed_outside('Carrier')
                    else:
                        if [to_Player2[1][x[2] - 1 + i][x[1] - 1] for i in range(5)] != ['-' for i in range(5)]:
                            print_ship_cannot_be_placed_occupied('Carrier')
                            continue
                        else:
                            for gru in range(5):
                                to_Player2[1][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Carrier')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'battleship':
                if x[3] == 'h':
                    if 'Battleship' not in Remaining_Ships:
                        print_ship_is_already_placed('Battleship')
                    elif x[2] > 10 or x[1] > 7:
                        print_ship_cannot_be_placed_outside('Battleship')
                    else:
                        if to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 4 - 1] != ['-' for i in range(4)]:
                            print_ship_cannot_be_placed_occupied('Battleship')
                            continue
                        else:
                            to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 4 - 1] = ['#' for i in range(4)]
                        Remaining_Ships.remove('Battleship')
                elif x[3] == 'v':
                    if 'Battleship' not in Remaining_Ships:
                        print_ship_is_already_placed('Battleship')
                    elif x[2] > 7 or x[1] > 10:
                        print_ship_cannot_be_placed_outside('Battleship')
                    else:
                        if [to_Player2[1][x[2] - 1 + i][x[1] - 1] for i in range(4)] != ['-' for i in range(4)]:
                            print_ship_cannot_be_placed_occupied('Battleship')
                            continue
                        else:
                            for gru in range(4):
                                to_Player2[1][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Battleship')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'cruiser':
                if x[3] == 'h':
                    if 'Cruiser' not in Remaining_Ships:
                        print_ship_is_already_placed('Cruiser')
                    elif x[2] > 10 or x[1] > 8:
                        print_ship_cannot_be_placed_outside('Cruiser')
                    else:
                        if to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 3 - 1] != ['-' for i in range(3)]:
                            print_ship_cannot_be_placed_occupied('Cruiser')
                            continue
                        else:
                            to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 3 - 1] = ['#' for i in range(3)]
                        Remaining_Ships.remove('Cruiser')
                elif x[3] == 'v':
                    if 'Cruiser' not in Remaining_Ships:
                        print_ship_is_already_placed('Cruiser')
                    elif x[2] > 8 or x[1] > 10:
                        print_ship_cannot_be_placed_outside('Cruiser')
                    else:
                        if [to_Player2[1][x[2] - 1 + i][x[1] - 1] for i in range(3)] != ['-' for i in range(3)]:
                            print_ship_cannot_be_placed_occupied('Cruiser')
                            continue
                        else:
                            for gru in range(3):
                                to_Player2[1][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Cruiser')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'submarine':
                if x[3] == 'h':
                    if 'Submarine' not in Remaining_Ships:
                        print_ship_is_already_placed('Submarine')
                    elif x[2] > 10 or x[1] > 8:
                        print_ship_cannot_be_placed_outside('Submarine')
                    else:
                        if to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 3 - 1] != ['-' for i in range(3)]:
                            print_ship_cannot_be_placed_occupied('Submarine')
                            continue
                        else:
                            to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 3 - 1] = ['#' for i in range(3)]
                        Remaining_Ships.remove('Submarine')
                elif x[3] == 'v':
                    if 'Submarine' not in Remaining_Ships:
                        print_ship_is_already_placed('Submarine')
                    elif x[2] > 8 or x[1] > 10:  # check
                        print_ship_cannot_be_placed_outside('Submarine')
                    else:
                        if [to_Player2[1][x[2] - 1 + i][x[1] - 1] for i in range(3)] != ['-' for i in range(3)]:
                            print_ship_cannot_be_placed_occupied('Submarine')
                            continue
                        else:
                            for gru in range(3):
                                to_Player2[1][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Submarine')
                else:
                    print_incorrect_orientation()
            elif x[0].lower() == 'destroyer':
                if x[3] == 'h':
                    if 'Destroyer' not in Remaining_Ships:
                        print_ship_is_already_placed('Destroyer')
                    elif x[2] > 10 or x[1] > 9:  # check
                        print_ship_cannot_be_placed_outside('Destroyer')
                    else:
                        if to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 2 - 1] != ['-' for i in range(2)]:
                            print_ship_cannot_be_placed_occupied('Destroyer')
                            continue
                        else:
                            to_Player2[1][x[2] - 1][x[1] - 1:x[1] + 2 - 1] = ['#' for i in range(2)]
                        Remaining_Ships.remove('Destroyer')
                elif x[3] == 'v':
                    if 'Destroyer' not in Remaining_Ships:
                        print_ship_is_already_placed('Destroyer')
                    elif x[2] > 9 or x[1] > 10:
                        print_ship_cannot_be_placed_outside('Destroyer')
                    else:
                        if [to_Player2[1][x[2] - 1 + i][x[1] - 1] for i in range(2)] != ['-' for i in range(2)]:
                            print_ship_cannot_be_placed_occupied('Destroyer')
                            continue
                        else:
                            for gru in range(2):
                                to_Player2[1][x[2] - 1 + gru][x[1] - 1] = '#'
                        Remaining_Ships.remove('Destroyer')
                else:
                    print_incorrect_orientation()
            else:
                print_incorrect_ship_name()

    struck_P1 = 0  # keeps track of how many tiles player1
    struck_P2 = 0
    while 1:  # battle phase
        turn = (turn+1) % 2  # this will keep track of whose turn it is and since the value is always set to modula 2 of the incremented value, it will oscillate between 0 and 1 for the whole game.
        while turn == 1:  # player 1's turn
            print_3d_list(to_Player1)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            coord = input().split()  # input will be a single string containing 2 values, seperated by whitespaces. We should separate them and put each value in a container separately.
            if len(coord) < 2:
                print_incorrect_input_format()
                continue
            try:
                x = int(coord[0])-1  # if the second and third elements are not ints, this will cause the except part to run.
                y = int(coord[1])-1  # also, x and y are 0-indexed. So we need to decrease the input by 1
            except:
                print_incorrect_input_format()
                continue
            if x > 9 or y > 9 or x < 0 or y < 0:  # the grid is 10x10, and the player cannot shoot a tile on the outside.
                print_incorrect_coordinates()
            elif to_Player2[1][y][x] == '#':  # if there is a ship piece in the chosen tile, we will change the tiles values to '!' for both of the 3d lists that are shown to player1 and player2
                print_hit()
                to_Player1[1][y][x] = '!'
                to_Player2[1][y][x] = '!'
                struck_P1 += 1  # we also need to increment the number of shot pieces
            elif to_Player2[1][y][x] == '-':  # if there is no ship piece in the chosen tile, we will change the tiles values to 'O' for both of the 3d lists that are shown to player1 and player2
                print_miss()
                to_Player1[1][y][x] = 'O'
                to_Player2[1][y][x] = 'O'
                print_type_done_to_yield(2)
                ans = input()
                while ans.lower() != 'done':  # this while loop will keep running until the player yields
                    print_type_done_to_yield(2)
                    ans = input()
                break
            else:
                print_tile_already_struck()  # if the chosen tile is neither '#' or '-', it will be either '!' or 'O'. This would mean that the tile has been shot before.
            if struck_P1 == 17:  # there are 17 pieces of ships in total, so when the number of shot tiles reaches 17, the game will end.
                break
        if struck_P1 == 17:  # end of the game, announcing the winner, etc
            print_3d_list(to_Player1)
            print_player_won(1)
            print_thanks_for_playing()
            break
        while turn == 0:  # player 2's turn is identical with the player1's turn.
            print_3d_list(to_Player2)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            coord = input().split()
            if len(coord) < 2:
                print_incorrect_input_format()
                continue
            try:
                x = int(coord[0]) - 1
                y = int(coord[1]) - 1
            except:
                print_incorrect_input_format()
                continue
            if x > 9 or y > 9 or x < 0 or y < 0:
                print_incorrect_coordinates()
            elif to_Player1[0][y][x] == '#':
                print_hit()
                to_Player2[0][y][x] = '!'
                to_Player1[0][y][x] = '!'
                struck_P2 += 1
            elif to_Player1[0][y][x] == '-':
                print_miss()
                to_Player2[0][y][x] = 'O'
                to_Player1[0][y][x] = 'O'
                print_type_done_to_yield(1)
                ans = input()
                while ans.lower() != 'done':
                    print_type_done_to_yield(1)
                    ans = input()
                break
            else:
                print_tile_already_struck()
            if struck_P2 == 17:
                break
        if struck_P2 == 17:
            print_3d_list(to_Player2)
            print_player_won(2)
            print_thanks_for_playing()
            break
except:
    f.close()

