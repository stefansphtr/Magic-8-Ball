# Import the random module to generate random numbers
import random

# Start an infinite loop to keep the program running until the user decides to quit
while True:

    # Ask the user for their name
    name = input("Enter your name: ")

    # Ask the user for their question
    question = input("Ask your question: ")

    # If the user didn't ask a question, print a message and continue with the next iteration
    if not question:
        print("You didn't ask anything.")
        continue

    # Initialize the answer variable
    answer = ""

    # Generate a random number between 1 and 15
    random_number = random.randint(1, 15)

    # Depending on the random number, set the answer to a different string
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "May God of fortune be with you"
    elif random_number == 11:
        answer = "Not sure, but be brave"
    elif random_number == 12:
        answer = "Sure you will, if you lucky by the way."
    elif random_number == 13:
        answer = "Looks like you can do it"
    elif random_number == 14:
        answer = "Just roll the dice, you will see it"
    elif random_number == 15:
        answer = "I bet you will"
    else:
        answer = "Error"

    # If the user entered their name, print the name and question
    if name:
        print(f"{name} asks: {question}")
    # If the user didn't enter their name, just print the question
    else:
        print(f"Question: {question}")

    # Print the answer from the Magic 8-Ball
    print(f"Magic 8-Ball's answer: {answer}")

    # Ask the user if they want to ask another question
    play_again = input("Do you want to ask another question? (yes/no): ")

    # If the user doesn't want to play again, break the loop
    if play_again.lower() != "yes":
        break