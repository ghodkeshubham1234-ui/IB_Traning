import random 

# ---------- COLORS ----------
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"


# ---------- GAME TITLE ----------
print(CYAN + BOLD + "=" * 45 + RESET)
print(MAGENTA + BOLD + "        🎮 NUMBER GUESSING GAME 🎮" + RESET)
print(CYAN + BOLD + "=" * 45 + RESET)

print(YELLOW + "\n📋 Game Rules:" + RESET)
print("1️⃣ You have only 3 attempts.")
print("2️⃣ Guess a number between 1 and 10.")
print("3️⃣ 🥇 1st attempt  = 100 points")
print("4️⃣ 🥈 2nd attempt  = 80 points")
print("5️⃣ 🥉 3rd attempt  = 60 points")

print("\n" + BLUE + "-" * 45 + RESET)


while True:

    print(CYAN + "\n🎮 Game loading.......!" + RESET)

    ip1 = input(YELLOW + "▶ Can you start the game? (Y/N): " + RESET)

    if ip1.lower() == 'n':
        print(RED + "\n❌ Game cancelled. See you next time! 👋" + RESET)
        break

    if ip1.lower() != 'y':
        print(RED + "⚠️ Please enter only Y or N!" + RESET)
        continue

    name = input(CYAN + "👤 Enter player name: " + RESET)

    # Generate random number between 1 and 10
    act_num = random.randint(1, 10)

    score = 0
    won = False

    print("\n" + MAGENTA + BOLD + "=" * 45 + RESET)
    print(GREEN + BOLD + f"🔥 Welcome {name}! 🔥" + RESET)
    print(YELLOW + "🎯 Guess a number between 1 and 10" + RESET)
    print(MAGENTA + "❤️ You have 3 attempts!" + RESET)
    print(MAGENTA + BOLD + "=" * 45 + RESET)

    # ---------- 3 ATTEMPTS ----------
    for i in range(1, 4):

        print(BLUE + f"\n🔹 Attempt {i}/3" + RESET)

        try:
            guess = int(input(YELLOW + "👉 Enter your guess (1-10): " + RESET))
        except ValueError:
            print(RED + "❌ Please enter a valid number!" + RESET)
            continue

        if guess < 1 or guess > 10:
            print(RED + "⚠️ Please enter a number between 1 and 10!" + RESET)
            continue

        # ---------- CORRECT GUESS ----------
        if act_num == guess:

            won = True

            if i == 1:
                score = 100
                print(GREEN + BOLD + "\n🎉🎉 CONGRATULATIONS! 🎉🎉" ,name + RESET)
                print(GREEN + "🏆 You won in the 1st attempt!" + RESET)

            elif i == 2:
                score = 80
                print(YELLOW + "\n🎉 CONGRATULATIONS! 🎉" ,name + RESET)
                print(GREEN + "🏆 You won in the 2nd attempt!" + RESET)

            else:
                score = 60
                print(YELLOW + "\n🎉 CONGRATULATIONS! 🎉" ,name + RESET)
                print(GREEN + "🏆 You won in the 3rd attempt!" + RESET)

            print(CYAN + BOLD + f"💰 Your Score: {score}" + RESET)
            break

        # ---------- WRONG GUESS ----------
        else:

            print(RED + "❌ Wrong guess!" + RESET)

            if guess < act_num:
                print(BLUE + "💡 Hint: Try a HIGHER number ⬆️" + RESET)
            else:
                print(BLUE + "💡 Hint: Try a LOWER number ⬇️" + RESET)

            if i == 1:
                print(YELLOW + "⚠️ 2 attempts remaining!" + RESET)

            elif i == 2:
                print(YELLOW + "⚠️ Last attempt! 😰" + RESET)

    # ---------- GAME OVER ----------
    if not won:
        print(RED + BOLD + "\n💀 GAME OVER! 💀" + RESET)
        print(RED + f"😔 You couldn't guess the number." + RESET)
        print(YELLOW + f"🎯 The correct number was: {act_num}" + RESET)
        print(CYAN + "💰 Your Score: 0" + RESET)

    # ---------- PLAY AGAIN ----------
    print("\n" + MAGENTA + "=" * 45 + RESET)

    res = input(YELLOW + "🔄 Do you want to play again? (Y/N): " + RESET)

    if res.lower() == 'n':
        print(GREEN + "\n🙏 Thanks for playing!" + RESET)
        print(CYAN + "👋 See you again! 🎮" + RESET)
        print(MAGENTA + "=" * 45 + RESET)
        break

    print(GREEN + "\n🚀 Starting a new game..." + RESET)


# import random

# # ---------- COLORS ----------
# GREEN = "\033[32m"
# RED = "\033[31m"
# YELLOW = "\033[33m"
# BLUE = "\033[34m"
# CYAN = "\033[36m"
# MAGENTA = "\033[35m"
# WHITE = "\033[37m"
# RESET = "\033[0m"
# BOLD = "\033[1m"


# # ---------- GAME TITLE ----------
# print(CYAN + BOLD + "=" * 45 + RESET)
# print(MAGENTA + BOLD + "        🎮 NUMBER GUESSING GAME 🎮" + RESET)
# print(CYAN + BOLD + "=" * 45 + RESET)

# print(YELLOW + "\n📋 Game Rules:" + RESET)
# print("1️⃣ You have only 3 attempts.")
# print("2️⃣ Guess a number between 1 and 10.")
# print("3️⃣ 🥇 1st attempt  = 100 points")
# print("4️⃣ 🥈 2nd attempt  = 80 points")
# print("5️⃣ 🥉 3rd attempt  = 60 points")

# print("\n" + BLUE + "-" * 45 + RESET)


# while True:

#     print(CYAN + "\n🎮 Game loading.......!" + RESET)

#     ip1 = input(YELLOW + "▶ Can you start the game? (Y/N): " + RESET)

#     if ip1.lower() == 'n':
#         print(RED + "\n❌ Game cancelled. See you next time! 👋" + RESET)
#         break

#     if ip1.lower() != 'y':
#         print(RED + "⚠️ Please enter only Y or N!" + RESET)
#         continue

#     name = input(CYAN + "👤 Enter player name: " + RESET)

#     # Generate random number between 1 and 10
#     act_num = random.randint(1, 10)

#     score = 0
#     won = False

#     print("\n" + MAGENTA + BOLD + "=" * 45 + RESET)
#     print(GREEN + BOLD + f"🔥 Welcome {name}! 🔥" + RESET)
#     print(YELLOW + "🎯 Guess a number between 1 and 10" + RESET)
#     print(MAGENTA + "❤️ You have 3 attempts!" + RESET)
#     print(MAGENTA + BOLD + "=" * 45 + RESET)

#     # ---------- 3 ATTEMPTS ----------
#     for i in range(1, 4):

#         print(BLUE + f"\n🔹 Attempt {i}/3" + RESET)

#         try:
#             guess = int(input(YELLOW + "👉 Enter your guess (1-10): " + RESET))
#         except ValueError:
#             print(RED + "❌ Please enter a valid number!" + RESET)
#             continue

#         if guess < 1 or guess > 10:
#             print(RED + "⚠️ Please enter a number between 1 and 10!" + RESET)
#             continue

#         # ---------- CORRECT GUESS ----------
#         if act_num == guess:

#             won = True

#             if i == 1:
#                 score = 100
#                 print(GREEN + BOLD + "\n🎉🎉 CONGRATULATIONS! 🎉🎉" + RESET)
#                 print(GREEN + "🏆 You won in the 1st attempt!" + RESET)

#             elif i == 2:
#                 score = 80
#                 print(YELLOW + "\n🎉 CONGRATULATIONS! 🎉" + RESET)
#                 print(GREEN + "🏆 You won in the 2nd attempt!" + RESET)

#             else:
#                 score = 60
#                 print(YELLOW + "\n🎉 CONGRATULATIONS! 🎉" + RESET)
#                 print(GREEN + "🏆 You won in the 3rd attempt!" + RESET)

#             print(CYAN + BOLD + f"💰 Your Score: {score}" + RESET)
#             break

#         # ---------- WRONG GUESS ----------
#         else:

#             print(RED + "❌ Wrong guess!" + RESET)

#             if guess < act_num:
#                 print(BLUE + "💡 Hint: Try a HIGHER number ⬆️" + RESET)
#             else:
#                 print(BLUE + "💡 Hint: Try a LOWER number ⬇️" + RESET)

#             if i == 1:
#                 print(YELLOW + "⚠️ 2 attempts remaining!" + RESET)

#             elif i == 2:
#                 print(YELLOW + "⚠️ Last attempt! 😰" + RESET)

#     # ---------- GAME OVER ----------
#     if not won:
#         print(RED + BOLD + "\n💀 GAME OVER! 💀" + RESET)
#         print(RED + f"😔 You couldn't guess the number." + RESET)
#         print(YELLOW + f"🎯 The correct number was: {act_num}" + RESET)
#         print(CYAN + "💰 Your Score: 0" + RESET)

#     # ---------- PLAY AGAIN ----------
#     print("\n" + MAGENTA + "=" * 45 + RESET)

#     res = input(YELLOW + "🔄 Do you want to play again? (Y/N): " + RESET)

#     if res.lower() == 'n':
#         print(GREEN + "\n🙏 Thanks for playing!" + RESET)
#         print(CYAN + "👋 See you again! 🎮" + RESET)
#         print(MAGENTA + "=" * 45 + RESET)
#         break

#     print(GREEN + "\n🚀 Starting a new game..." + RESET)