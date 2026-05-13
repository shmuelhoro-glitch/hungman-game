import random
# הגדרת תנאי המשחק
level_1 = ["apple", "water", "house", "smile", "bread"]
level_2 = ["python", "puzzle", "guitar", "castle", "planet"]
level_3 = ["developer", "algorithm", "xylophone", "cryptography", "jazz"]



def print_welcome_screen():
     # 1. הודעת פתיחה מהצ'אט
    width = 50
    print("=" * width)
    print("W E L C O M E   T O".center(width))
    print("H A N G M A N   G A M E".center(width))
    print("=" * width)
    print("\n") 
    hangman_art = r"""
           _________
          |/        |
          |        (_)
          |        \|/
          |         |
          |        / \
          |
         _|_
    """

    for line in hangman_art.split('\n'):
        print(" " * 12 + line)
        
    print("\n") 

    
    print("-" * width)
    print("Created by: SHMUEL".center(width))
    print("Have Fun & Good Luck!".center(width))
    print("-" * width)
    print("\n") 

def get_name_and_level():
    user_name = input("please enter your name: ")
    is_level = False
    while not is_level:
        user_level = input(f"please choose level" 
                        f"1 (easy) "
                        f"2 (medium) "
                        f"3 (hard)")
        if user_level == "1" or user_level == "2" or user_level == "3":
            is_level = True
            break
        else:
            print("there is a problem. your answer have to or '1' or '2' or '3' " )
    return [user_name,user_level]

def get_word(level):
    list_from_level = globals()[f"level_{level}"]
    random_word = random.choice(list_from_level)
    return random_word

def is_proper_input(char):
    pass

def add_correct_letter():
    pass

def show_current_mode():
    pass

def check_for_over_game():
    pass

def main_menu():
   print_welcome_screen()
   name_and_level = get_name_and_level()
   start_game(name_and_level[1])



def start_game():
    current_word = get_word()
    NUM_CHANCE = 10
    left_try = 0
    checked_letters = []


def status_menu():
    pass




