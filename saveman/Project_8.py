# 2/10/2023
# Save man Game

# Module Required
import logo_animation ,countdown ,scenes ,random ,Endcards ,game_menu ,Data_name

# Names and inputs for game
name = random.choice(Data_name.south_indian_names)   # original name
encrypted = list('_'*len(name))                             # encrypting the name with underscores
temp_name = list(name)                                      # temporary name for evaluating and replacing already occurred char with '-'

# Effects for the game
def css(message,chances):
    heart = ''
    match chances:
        case 3: heart = '❤❤❤ '
        case 2: heart = '❤❤ '
        case 1: heart = '❤ '
    tell = f"You are left with {heart} life's"
    effect_1 = rf"""
                     __| |____________________________________________| |__
                    (__   ____________________________________________   __)
                       | |                                            | |
                       | |                                            | |
{'| |':>26}{message:^44}{'| |':<}
{'| |':>26}{tell:^44}{'| |':<}                                           
                       | |                                            | |
                       | |                                            | |
                     __| |____________________________________________| |__
                    (__   ____________________________________________   __)
                       | |                                            | |
"""
    print(effect_1)

# method to display animations
def display_animation():
    # Printing Logo
    logo_animation.animation_logo_a()
    countdown.count_time()
    logo_animation.animation_logo_b()

# method to decide the looser
def decide_loss(user_name):
    scenes.game_dis(7,user_name)
    print(f"\n\t\t\t╰┈➤ The boy dead {user_name}...\n\t\t\t╰┈➤ The secret name was - [ {name} ]")
    Endcards.w_l(user_name,flag=1)
    Endcards.game_over()
    exit()

# method to decide the winner
def decide_winner(user_name):
    scenes.game_dis(1,user_name)
    print(f"\n\t\t\t╰┈➤ You Guessed the name correctly\n\t\t\t╰┈➤ you won the game Dear {user_name}")
    Endcards.fire_work()
    Endcards.w_l(user_name, flag=0)
    Endcards.game_over()
    exit()

# method for actual game
def start_game(user_name):
    critical_range = 2           # variable for deciding scene's
    flag = 0                     # Flag variable for decision
    chances = 3                  # chance variable for showing left life's
    tracker = 0
    while True:
        # Taking input from user
        if tracker == 0:
            char = input("\n\t\t\t╰┈➤ Guess a first letter from the name: ").replace(' ', "").casefold()
        else:
            char = input("\n\t\t\t╰┈➤ Guess a another letter from the name: ").replace(' ', "").casefold()
        if char in temp_name:
            index = temp_name.index(char)                       # finds the index of letter if its present
            temp_name[index] = "-"                              # replaces the letter with '-' to avoid the conflicts
            encrypted[index] = char                             # replaces the _ with actual letter
            critical_range -= 1
            if critical_range <= 2: critical_range = 2
            css("Good guess",chances)
            print(f"{'╰┈➤  Your Guess = [':>50}", end="")
            for n in encrypted:                                 # prints the word with entered letter along with _ if present
                print(n, end=' ')
            print(f"{']'}")
            scenes.game_dis(critical_range,user_name)
        else :
            critical_range += 1
            flag += 1
            chances -= 1
            if critical_range >= 6: critical_range = 6
            css("[ invalid input ] - Boy is drowning deep",chances)  # displays if entered invalid choice
            scenes.game_dis(critical_range,user_name)
        # Winning condition
        if '_' not in encrypted:
            decide_winner(user_name)
        # Loosing Condition
        if flag == 3:
            decide_loss(user_name)
        tracker += 1

def main():
        display_animation()
        game_menu.menu()
        user_name = input("\n\t\t\t╰┈➤ Enter your name please: ").casefold()
        start_game(user_name)
if __name__ == "__main__":
        main()


