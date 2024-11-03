import time

def menu():
    menu1 = rf"""
                ╔─────────────────────────────────────────────────────────────────────────╗
                │                              GAME MENU                                  │
                │                                                                         │
                │        [ Your Task is to save the Boy who is Drowning in the water ]    │
                │           【 You will have ❤❤❤  life's to guess the name 】           👈
                │                                                                         │
                │  1. You will be asked to Enter your name                                │
                │  2. System Automatically chooses your best Friend names                 │
                │  3. you will be asked to guess each letter from your friend name        │
                │  4. for each wrong guess 1 life will be taken away                      │
                │     and boy will drown deeper and deeper                                │
                │  5. for each right guess life will be preserved                         │
                │     and boy will start to come out of the water slowly                  │
                │  6. consecutive 3 wrong guesses results in game over                    │
                │                                                                         │
                ╚─────────────────────────────────────────────────────────────────────────╝
"""
    for i in menu1:
        print(i,end='')
        time.sleep(0.001)

