import random
print("--------------------------------------")
print("ROCK_PAPER_SCISSORS")
print("--------------------------------------")
inp = input("Do you want to play(Y/N) - ")
lst = ["r", "p", "s"]
if inp.upper() == "Y":
    print("--------------------------------------")
    strt = 0
    end = 3
    scr_ply = 0
    scr_ai = 0
    while True:
        for i in range(strt,end):
            print("--------------------------------------")
            print(f"round {i+1}")
            inp_u = input("Enter your choice(r/p/s) - ")
            print(f"Your choice was {inp_u}.")
            inp_ai = random.choice(lst)
            print(f"AI's choice was {inp_ai}.")
            if inp_u == inp_ai:
                print("Tie")
            elif inp_u == "s" and inp_ai == "r":
                print("You Lose")
                scr_ai+=1
            elif inp_u == "r" and inp_ai == "s":
                print("You Win")
                scr_ply+=1
            else:
                if lst.index(inp_u) > lst.index(inp_ai):
                    print("You Win")
                    scr_ply+=1
                else:
                    print("You Lose.")
                    scr_ai+=1
        print("--------------------------------------")
        resp1 = input("Do you want to exit(Y/N)- ")
        print("--------------------------------------")
        if resp1.upper() == "Y":
            if scr_ply == scr_ai:
                print(f"Your score was {scr_ply} and AI's score was {scr_ai}")
                print("It's a tie.")
                print("So close.")
            elif scr_ply > scr_ai:
                print(f"Your score was {scr_ply} and AI's score was {scr_ai}")
                print("You are the Winner.")
                print("Well Played.")
            else:
                print(f"Your score was {scr_ply} and AI's score was {scr_ai}")
                print("AI is the Winner.")
                print("Better luck next time.")
            print("--------------------------------------")
            break
        strt+=3
        end+=3