from ConnectState import ConnectState
from mcts import MCTS
import os


def play():
    state = ConnectState()
    mcts = MCTS(state)
    
    user = os.environ.get('USER', os.environ.get('USERNAME'))
    os.system('color')
    print("#########################################")
    print("Hello {}, this is a Connect4 game exploiting".format(user))
    print("a Monte Carlo Tree Search method.")
    print("Please enjoy the game!")
    print("#########################################")

    print("\n")
    print("Do you want to play as first or second? [1 or 2]")
    istart = int(input("Choose: "))

    if istart == 1:
        print("Ok, you decided to go first!")
        print("\n")

        while not state.game_over():
            print("Current state:")
            state.print()

            user_move = int(input("Enter a move: "))
            while user_move not in state.get_legal_moves():
                print("Illegal move")
                user_move = int(input("Enter a move: "))

            state.move(user_move)
            mcts.move(user_move)

            state.print()

            if state.game_over():
                #state.print()
                print("Player one won!")
                print("\n")

                input("Press enter to close...")
                break

            print("Thinking...")

            mcts.search(8)
            num_rollouts, run_time = mcts.statistics()
            print("Statistics: ", num_rollouts, "rollouts in", run_time, "seconds")
            move = mcts.best_move()

            print("MCTS chose move: ", move)

            state.move(move)
            mcts.move(move)

            if state.game_over():
                state.print()
                print("Player two won!")
                print("\n")

                input("Press enter to close...")
                break

    elif istart == 2:
        print("Ok, you decided to go as second!")
        print("\n")

        while not state.game_over():

            print("Thinking...")

            mcts.search(8)
            num_rollouts, run_time = mcts.statistics()
            print("Statistics:", num_rollouts, "rollouts in", run_time, "seconds")
            move = mcts.best_move()

            print("MCTS chose move :", move)

            state.move(move)
            mcts.move(move)

            print("Current state:")
            state.print()

            if state.game_over():
                state.print()
                print("Player one won!")
                print("\n")

                input("Press enter to close...")
                break

            user_move = int(input("Enter a move: "))
            while user_move not in state.get_legal_moves():
                print("Illegal move")
                user_move = int(input("Enter a move: "))

            state.move(user_move)
            mcts.move(user_move)

            state.print()

            if state.game_over():
                #state.print()
                print("Player two won!")
                print("\n")

                input("Press enter to close...")
                break

    else:
        print("Please enter 1 or 2.")
        return



if __name__ == "__main__":
    play()
