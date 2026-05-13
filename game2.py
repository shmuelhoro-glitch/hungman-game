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

def is_proper_input(char)->bool:
    pass #בדיקה האם התו הוא אות באנגלית

def check_if_correct():
    pass

def add_correct_letter():
    pass

def show_current_mode():
    pass

def check_for_over_game():
    pass

def main_menu():
    pass

def start_game():
    pass
    
def status_menu():
    pass
   

print_welcome_screen()
name_and_level = get_name_and_level()
current_word = get_word(name_and_level[1])

split_word = current_word.split()
silhouette_word = "_"*len(split_word)
left_chance = 10
print(f"you need guess this word: {silhouette_word}"
      f"you have {left_chance} chances ")

while True:
    user_try = input("please try find the charter: ")
    if not is_proper_input(user_try):
        print("this valid input. try again ")
        continue
    check_if_correct(user_try)

    print(f"your status is: ")
    