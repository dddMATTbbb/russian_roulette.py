import random
import os

alive = 1

amount_reroll = 2
amount_opponent = 1

bullet_num_case = random.randint(1, 6)
current_bullet_case = random.randint(1, 6)

def check_bullet(case):
        global current_bullet_case
        global bullet_num_case
        global alive
        global amount_reroll
        global amount_opponent

        if case == "SHOOT_YOURSELF":
                current_case = current_bullet_case
                if current_bullet_case == bullet_num_case:
                        alive = 0
                        return("you shot yourself...")
                else:
                        amount_opponent = 1
                        if current_bullet_case >= 6:
                                current_bullet_case = 1
                        else:
                                current_bullet_case += 1

                        return("there wasn't a bullet in case", current_case)
        elif case == "SHOOT_OPPONENT":
                if amount_opponent < 1:
                        print("you can't do that anymore")
                else:
                        if current_bullet_case == bullet_num_case:
                                alive = 0
                                print("your opponent is shot dead")
                                os.system("pause")
                                return("your opponent is shot dead")
                        else:
                                if current_bullet_case >= 6:
                                        current_case = current_bullet_case
                                        current_bullet_case = 1
                                        amount_opponent -= 1
                                        return("there wasn't a bullet in case", current_case)
                                else:
                                        current_case = current_bullet_case
                                        current_bullet_case += 1
                                        amount_opponent -= 1
                                        return("there wasn't a bullet in case", current_case)
        elif case == "REROLL":
                if amount_reroll < 1:
                        print("you cant use this again")
                else:
                        current_bullet_case = random.randint(1, 6)
                        amount_reroll -= 1
                        print("rerolled to case", current_bullet_case)
        else:
                print("a error oncured bye the function")
                alive = 0

#rules
#1 you can 1 time shoot at your opponent
#2 you can 1 time reroll the case
print("rules")
print("after you shoot your opponent you NEED TO SHOOT YOUR SELF OR REROLL")
print("you can roll the magazine twice", "\n")


while alive == 1:
        answer = input("whats your choice? write SHOOT_YOURSELF, SHOOT_OPPONENT or REROLL: " )

        if answer == "SHOOT_YOURSELF":
                outcome = check_bullet(answer)
                print(outcome, "\n")
        elif answer == "SHOOT_OPPONENT":
                outcome = check_bullet(answer)
                print(outcome, "\n")
        elif answer == "REROLL":
                check_bullet(answer)
                print("\n")
        elif answer == "debug":
                print(current_bullet_case, bullet_num_case, alive)
        elif answer == "exit":
                alive = 0
        else:
                print("invalid option")