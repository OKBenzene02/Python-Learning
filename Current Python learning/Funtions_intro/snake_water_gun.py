import random

chances = 10
player_score = 0
system_score = 0
print("""Player choices:
 S --> Snake
 W --> Water
 G --> Gun""")
while chances != 0:
    chances -= 1
    lst = ["Snake", "Water", "Gun"]
    system_bot = random.choice(lst)
    player = input("Snake, Water, Gun: ")
    if player == "S".casefold() and system_bot == "snake":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Snake")
        print(f"{system_score}      |  {player_score}")
        continue
    elif player == "S".casefold() and system_bot == "water":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Snake")
        player_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "S".casefold() and system_bot == "gun":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Snake")
        system_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "W".casefold() and system_bot == "snake":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Water")
        system_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "W".casefold() and system_bot == "water":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Water")
        print(f"{system_score}      |  {player_score}")
        continue
    elif player == "W".casefold() and system_bot == "gun":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Water")
        player_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "G".casefold() and system_bot == "snake":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Gun")
        player_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "G".casefold() and system_bot == "water":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Gun")
        system_score += 1
        print(f"{system_score}      |  {player_score}")
    elif player == "G".casefold() and system_bot == "gun":
        print("SYSTEM | PLAYER")
        print(system_bot, "    Gun")
        print(f"{system_score}      |  {player_score}")
        continue

if player_score > system_score:
    print(f"Player --> WINS with {player_score} points")
elif system_score == player_score:
    print("System and Player --> Draw")
else:
    print(f"System --> WINS with {system_score} points")
