from random import randint
import argparse

# Constants
MOVES = ["U", "D", "L", "R", "F", "B"]
OPPOSITES = ["D", "U", "R", "L", "B", "F"] # Wasteful, but fast & simple

def main(args):
    # Local variables
    prevMove1 = prevMove2 = ""
    if args.v:
        warningBuffer = []
    n = args.l
a
    # Main loop
    for _ in range(n):
        while True:
            r1 = randint(0, 5) # Necessary for checking redundancy 
            move = MOVES[r1]

            # Ensure moves are not repeated (U U)
            if (move is prevMove1):
                if args.v: # Not necessary, but saves memory when not running verbosely
                    warningBuffer.append(f"WARNING: Regenerating duplicate move: {move}")
                continue

            # Ensure moves are not redundant (U D U)
            if (move is prevMove2) and (prevMove1 is OPPOSITES[r1]):
                if args.v:
                    warningBuffer.append(f"WARNING: Regenerating redundant moves: {move} {prevMove1} {prevMove2}")
                continue
            
            # Success, store move
            prevMove2 = prevMove1
            prevMove1 = move
            break

        # Double/inverse/normal move
        r2 = randint(0, 2)
        if (r2 == 0):
            move += "2"
        elif (r2 == 1):
            move += "'"

        # Print
        print(f"{move} ", end ="")
    print()

    # Print warnings if verbose
    if args.v:
        for warning in warningBuffer:
            print(f"{warning}")

    exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", type=int, default=18,
        help="Give length as argument, instead of during execution")
    parser.add_argument("-v", action="store_true", # Eg. default=False
        help="Show warnings when invalid moves are regenerated")
    args = parser.parse_args()

    main(args)
