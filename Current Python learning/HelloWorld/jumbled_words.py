import random


def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water'
             , 'board']
    word_picked = random.choice(words)
    return word_picked


def jumble(word):
    return "".join(random.sample(word, len(word)))


def thankyou(player1, player2, p1, p2):
    print(f"{player1} your score is {p1}\n"
          f"{player2} your score is {p2}\n"
          "Thank you for playing.\nHave a nice day.")


def play():
    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")
    p1 = 0
    p2 = 0
    turn = 0

    while True:
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)

        # Player 1
        if turn % 2 == 0:
            print(player1, 'Your turn.')
            ans = input("What is on my mind?")
            if ans == picked_word:
                p1 += 1
                print("Your score,", p1)
            else:
                print("Better luck next time, I thought", ans)
            c = int(input('press 1 to continue and 0 to quit.'))
            if c == 0:
                thankyou(player1, player2, p1 ,p2)
                break

            # Player 2
        else:
            print(player2, 'Your turn.')
            ans = input("What is on my mind? ")
            if ans == picked_word:
                p2 += 1
                print("Your score,", p2)
            else:
                print("Better luck next time, I thought", ans)
            c = int(input('press 1 to continue and 0 to quit.'))
            if c == 0:
                thankyou(player1, player2, p1 ,p2)
                break

        turn += 1


play()
