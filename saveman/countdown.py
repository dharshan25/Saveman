# Program for designing the time animation

import os, time

def count_time():

    count1 = r"""
                                             ████ 
                                            ░░███ 
                                             ░███ 
                                             ░███ 
                                             ░███ 
                                             ░███ 
                                             █████
                                            ░░░░░ 
    """
    count2 = r"""
                                          ████████ 
                                         ███░░░░███
                                        ░░░    ░███
                                           ███████ 
                                          ███░░░░  
                                         ███      █
                                        ░██████████
                                        ░░░░░░░░░░ 
    """
    count3 = r"""
                                        
                                          ████████ 
                                         ███░░░░███
                                        ░░░    ░███
                                           ██████░ 
                                          ░░░░░░███
                                         ███   ░███
                                        ░░████████ 
                                         ░░░░░░░░  
    
    """
    start_o = """
                          █████████   █████                         █████   
                         ███░░░░░███ ░░███                         ░░███    
                        ░███    ░░░  ███████    ██████   ████████  ███████  
                        ░░█████████ ░░░███░    ░░░░░███ ░░███░░███░░░███░   
                         ░░░░░░░░███  ░███      ███████  ░███ ░░░   ░███    
                         ███    ░███  ░███ ███ ███░░███  ░███       ░███ ███
                        ░░█████████   ░░█████ ░░████████ █████      ░░█████ 
                         ░░░░░░░░░     ░░░░░   ░░░░░░░░ ░░░░░        ░░░░░  
    """

    counts = [count1,count2,count3,start_o]

    for frames in counts:
        os.system('cls')
        print(frames)
        time.sleep(0.8)
    else:
        os.system('cls')

