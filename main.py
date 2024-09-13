from .core import Game
from .config import num_cols, num_rows


def start():
    for row in range(num_rows):
        Game.grid.append([0] * num_cols)

    # printing controls for user
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    Game.add_new_2()
    Game.arrange()


if __name__ == '__main__':
    start()
    # loop until game is over
    while True:
        command = input("Enter the command: ").lower()
        if command == 'w':
            # user wants to move up
            Game.move_up()
            # get the current state of the game
            # if game is not over, generate a new 2
            if Game.get_state() == "GAME NOT OVER":
                Game.add_new_2()
            else:
                break
        elif command == 's':
            # user wants to move down
            Game.move_down()
            # if game is not over, generate a new 2
            if Game.get_state() == "GAME NOT OVER":
                Game.add_new_2()
            else:
                break
        elif command == 'a':
            # user wants to move left
            Game.move_left()
            # if game is not over
            if Game.get_state() == "GAME NOT OVER":
                Game.add_new_2()
            else:
                break
        elif command == 'd':
            # user wants to move right
            Game.move_right()
            # if game is not over
            if Game.get_state() == "GAME NOT OVER":
                Game.add_new_2()
            else:
                break
        else:
            print("Invalid Command")
        Game.arrange()