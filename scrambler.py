from random import randint

MOVES = ["U", "D", "L", "R", "F", "B"]

def main():
    try:
        n = int(input("\nEnter the scramble length: "))
    except:
        exit("ERROR: Please enter a numerical value\n")
    previousMove = ""

    for _ in range(n):
        while True: # Ensure moves are not repeated
            move = MOVES[randint(0, 5)]
            if (move is not previousMove):
                previousMove = move
                break

        r = randint(0, 2) # Double/inverse/normal move
        if (r == 0):
            move += "2"
        elif (r == 1):
            move += "'"

        print(f"{move} ", end ="")

    print("\n")
    exit(1)

if __name__ == "__main__":
    main()
