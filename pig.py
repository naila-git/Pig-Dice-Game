import random

def roll_die():
    return random.randint(1,6)

def update_score(player,rolled,scores):
    if rolled == 1:
        scores[player] = 0
        print(f"{player}'s score reset to 0 due to rolling a 1.\n")
    else:
        scores[player] += rolled
        print(f"{player}'s new total score is {scores[player]}\n")
    return scores[player]


def play_game():
    scores = {'first_player':0, 'second_player':0}
    repeat = True

    while repeat:
        player = input("Who is playing first_player or second_player?\n").strip()

        if player not in scores:
            print("Invalid player. Please choose again.\n")
            continue 

        roll_choice = input("\nWould you like to roll the die, yes or no?\n")
        if roll_choice == "yes":
            rolled = roll_die()
            print(f"You rolled {rolled}")


            new_score = update_score(player,rolled,scores)
            if new_score >= 50:
                repeat = False
                print(f"{player} won!")

        elif roll_choice == "no":
            print(f"{player} chose not to roll\n")
    

if __name__=="__main__":
    play_game()

        
