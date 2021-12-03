from random import randint
from sys import argv
import argparse

# Constants
MOVES = ["U", "D", "L", "R", "F", "B"]
OPPOSITES = ["D", "U", "R", "L", "B", "F"] # Wasteful, but simplifies logic/data structure

def main():
    # Local variables
    prevMove1 = ""
    prevMove2 = ""
    showWarnings = False
    if showWarnings:
        warningBuffer = []

    if (True): # TODO: Check if n is defined?
        try:
            n = int(input("\nEnter the scramble length: "))
        except:
            exit("ERROR: Please enter a numerical value\n")


    for _ in range(n):
        while True:
            r1 = randint(0, 5)
            move = MOVES[r1]

            # Ensure moves are not repeated
            if (move is prevMove1):
                if showWarnings:
                    warningBuffer.append(f"WARNING: Duplicate move found: {move}")
                continue

            # Ensure moves are not redundant, such as U D U'
            if (move is prevMove2) and (prevMove1 is OPPOSITES[r1]):
                if showWarnings:
                    warningBuffer.append(f"WARNING: Redundant moves found: {move} {prevMove1} {prevMove2}")
                continue
            
            prevMove2 = prevMove1
            prevMove1 = move
            break

        # Double/inverse/normal move
        r2 = randint(0, 2)
        if (r2 == 0):
            move += "2"
        elif (r2 == 1):
            move += "'"

        print(f"{move} ", end ="")
    print("\n")

    if showWarnings:
        for warning in warningBuffer:
            print(f"{warning}")
        print()

    exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("")
    #
    #
    #

    args = parser.parse_args()
    
    main(args.name)
