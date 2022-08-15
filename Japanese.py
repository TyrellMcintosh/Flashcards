import random

# Open textfile and read the lines into a list
txtfile = open('romaji.txt').read().splitlines()

# Variables to keep track of correct answers
correct = incorrect = count = 0

# Loop that prints each line
while True:
    count += 1
    randline = random.choice(txtfile)
    japanese = randline.partition("-")[0]
    print("\nWhat does {} mean in English?".format(japanese))
    answer = input()
    english = randline.partition("-")[2]
    if (answer == english):
        correct += 1
        print("Correct! So far you have {} correct answers and {} incorrect answers."
              .format(correct, incorrect))
    else:
        incorrect += 1
        print("Incorrect, {} is the correct answer".format(english))

    print("Hit the enter key to continue or n to exit")
    answer2 = input()
    if (answer2 == 'n'):
        break

score = "{:.0%}".format(correct / count)
print("You finished with a score of:",score)

    
    

    





