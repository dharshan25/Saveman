# Save man Game Essential Project Files

# Modules Required
import time, os                      #countdown - this module used when necessary
from platform import system


# Game Logo Before Show
def animation_logo_a():

    # start time for constant time et point
    start_time = time.time()

    step1 = r"""
            ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
            ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
            ╟┤                                                                                        ├╢
            ╟┤                                                                                        ├╢
            ╟┤       ___         ___        ___         ___         ___         ___         ___       ├╢
            ╟┤      /\  \       /\  \      /\__\       /\  \       /\__\       /\  \       /\__\      ├╢
            ╟┤     /::\  \     /::\  \    /:/  /      /::\  \     /::|  |     /::\  \     /::|  |     ├╢
            ╟┤    /:/\ \  \   /:/\:\  \  /:/  /      /:/\:\  \   /:|:|  |    /:/\:\  \   /:|:|  |     ├╢
            ╟┤   _\:\~\ \  \ /::\~\:\  \/:/__/  ___ /::\~\:\  \ /:/|:|__|__ /::\~\:\  \ /:/|:|  |__   ├╢
            ╟┤  /\ \:\ \ \__/:/\:\ \:\__|:|  | /\__/:/\:\ \:\__/:/ |::::\__/:/\:\ \:\__/:/ |:| /\__\  ├╢
            ╟┤  \:\ \:\ \/__\/__\:\/:/  |:|  |/:/  \:\~\:\ \/__\/__/~~/:/  \/__\:\/:/  \/__|:|/:/  /  ├╢
            ╟┤   \:\ \:\__\      \::/  /|:|__/:/  / \:\ \:\__\       /:/  /     \::/  /    |:/:/  /   ├╢
            ╟┤    \:\/:/  /      /:/  /  \::::/__/   \:\ \/__/      /:/  /      /:/  /     |::/  /    ├╢
            ╟┤     \::/  /      /:/  /    ~~~~        \:\__\       /:/  /      /:/  /      /:/  /     ├╢
            ╟┤      \/__/       \/__/                  \/__/       \/__/       \/__/       \/__/      ├╢
            ╟┤                                                                                        ├╢
            ╟┤                                                                                        ├╢
            ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
            ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
        """

    step2 = r"""
            ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
            ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
            ╟┤                                                                                        ├╢
            ╟┤                                                                                        ├╢
            ╟┤       ___         ___                    ___         ___         ___         ___       ├╢
            ╟┤      /\__\       /\  \        ___       /\__\       /\  \       /\  \       /\  \      ├╢
            ╟┤     /:/ _/_     /::\  \      /\  \     /:/ _/_     |::\  \     /::\  \      \:\  \     ├╢
            ╟┤    /:/ /\  \   /:/\:\  \     \:\  \   /:/ /\__\    |:|:\  \   /:/\:\  \      \:\  \    ├╢
            ╟┤   /:/ /::\  \ /:/ /::\  \     \:\  \ /:/ /:/ _/_ __|:|\:\  \ /:/ /::\  \ _____\:\  \   ├╢
            ╟┤  /:/_/:/\:\__/:/_/:/\:\__\___  \:\__/:/_/:/ /\__/::::|_\:\__/:/_/:/\:\__/::::::::\__\  ├╢
            ╟┤  \:\/:/ /:/  \:\/:/  \/__/\  \ |:|  \:\/:/ /:/  \:\~~\  \/__\:\/:/  \/__\:\~~\~~\/__/  ├╢
            ╟┤   \::/ /:/  / \::/__/    \:\  \|:|  |\::/_/:/  / \:\  \      \::/__/     \:\  \        ├╢
            ╟┤    \/_/:/  /   \:\  \     \:\__|:|__| \:\/:/  /   \:\  \      \:\  \      \:\  \       ├╢
            ╟┤      /:/  /     \:\__\     \::::/__/   \::/  /     \:\__\      \:\__\      \:\__\      ├╢
            ╟┤      \/__/       \/__/      ~~~~        \/__/       \/__/       \/__/       \/__/      ├╢
            ╟┤                                                                                        ├╢
            ╟┤                                                                                        ├╢
            ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
            ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
            
    """

    while time.time() - start_time < 2:
        # print frame 1
        print(f"{step1}")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

        # print frame 2
        print(f"{step2}", end= '\r')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

# Constructing the actual logo into the list

def animation_logo_b():
    a1 = r"╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗"
    a2 = r"╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢"
    a3 = r"╟┤                                                                                    ├╢"
    a4 = r"╟┤                                                                                    ├╢"
    a5 = r"╟┤    █████████                                                                       ├╢"
    a6 = r"╟┤   ███░░░░░███                                                                      ├╢"
    a7 = r"╟┤  ░███    ░░░   ██████   █████ █████  ██████  █████████████    ██████   ████████    ├╢"
    a8 = r"╟┤  ░░█████████  ░░░░░███ ░░███ ░░███  ███░░███░░███░░███░░███  ░░░░░███ ░░███░░███   ├╢"
    a9 = r"╟┤   ░░░░░░░░███  ███████  ░███  ░███ ░███████  ░███ ░███ ░███   ███████  ░███ ░███   ├╢"
    a10 = r"╟┤   ███    ░███ ███░░███  ░░███ ███  ░███░░░   ░███ ░███ ░███  ███░░███  ░███ ░███   ├╢"
    a11 = r"╟┤  ░░█████████ ░░████████  ░░█████   ░░██████  █████░███ █████░░████████ ████ █████  ├╢"
    a12 = r"╟┤   ░░░░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░   ├╢"
    a13 = r"╟┤                                                                                    ├╢"
    a14 = r"╟┤                                                                                    ├╢"
    a15 = r"╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢"
    a16 = r"╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝"

    # adding 'a' frames to the list
    logo = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16]

    # Printing the frame with delay time of 0.1
    for frame in logo:
        print(f"\t\t{frame}",end='\n')
        time.sleep(0.1)
    else:
        b3 = "                                             ;;;;;"
        b4 = "                                             ;;;;;"
        b5 = "                                           ..;;;;;.."
        b6 = "                                            ':::::'"
        b7 = "                                              ':`"
        arr = [b3,b4,b5,b6,b7]
        for i in arr:
            print('\t',i)
            time.sleep(0.1)

# Start with Clear Screen
os.system('cls')


