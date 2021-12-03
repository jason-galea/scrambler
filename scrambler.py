from random import randint

MOVES = ["U", "D", "L", "R", "F", "B"]
OPPOSITES = ["D", "U", "R", "L", "B", "F"] # Wasteful, but simplifies logic/data restructuring

def main():
    try:
        n = int(input("\nEnter the scramble length: "))
    except:
        exit("ERROR: Please enter a numerical value\n")

    previousMove1 = ""
    previousMove2 = ""
    showWarnings = True
    # showWarnings = False
    warningBuffer = []

    for _ in range(n):
        while True:
            r1 = randint(0, 5)
            move = MOVES[r1]

            # Ensure moves are not repeated
            if (move is previousMove1):
                warningBuffer.append(f"WARNING: Duplicate move found: {move}")
                continue

            # Ensure moves are not redundant, such as U D U'
            if (move is previousMove2) and (previousMove1 is OPPOSITES[r1]):
                warningBuffer.append(f"WARNING: Redundant moves found: {move} {previousMove1} {previousMove2}")
                continue

            previousMove2 = previousMove1
            previousMove1 = move
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
    main()
