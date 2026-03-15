# HANGMAN GAME 
import random
import time
import os
hangman_art={
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/|  ",
        "   "),
    4: ("  O ",
        "/ | \\",
        "   "),
    5: ("  O ",
        "/ | \\",
        " /  "),
    6: ("  O ",
        "/ | \\",
        " / \\"),
}

words=["python","developer","coding","apple","orange","pineapple","venice","india","jazz", "quiz", "puzzle", "jinx", "haphazard", "xylophone", "juxtapose",
    "blizzard", "zigzag", "jackpot", "quartz", "microwave", "jukebox","developer", "algorithm", "universe", "dinosaur", "elephant", "kangaroo",
    "butterfly", "chocolate", "pyramid", "volcano", "waterfall", "orchestra",
    "adventure", "boulevard", "cathedral", "detective", "encyclopedia",]


print("------------wlecome------------")
print("--------to the hangman---------")
print("-------------game--------------")
def clear_screen():
    os.system('cls')
def hangman_display(wrong_guesses):
    clear_screen()
    print("------------ HANGMAN GAME ------------")
    for i in hangman_art[wrong_guesses]:
        time.sleep(0.3)
        print(i)
def hints_display(hints):
    print("  ".join(hints))
def game():
    wrong_guesses=0
    
    answer=random.choice(words)
    hints= ["_"] * len(answer)
    answer=list(answer)
    while wrong_guesses<6 and "_" in hints:
        user=input("enter your letter: ").lower()
        if user.isdigit() or len(user)>1:
            print("enter a valid choice")
            break
        elif user == "exit":
            print("thank you for playing")
            break
        else:
            if user in answer:
                for i, letter in enumerate(answer):
                    if letter == user:
                        hints[i] = user
            
            else:
                wrong_guesses+=1
            hangman_display(wrong_guesses)
            hints_display(hints)
    if "_" in hints:
        clear_screen()
        print("you lost!!!!")
        print(f"the correct answer was {"".join(answer)}")
    else:
        clear_screen()
        print("you won!!!")
        print(f"the correct answer was {"".join(answer)}")
    
game()
