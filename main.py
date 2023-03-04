import pyttsx3
import random

engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 2.0)    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

List = ['>8', '|-|', 'O']

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def random_generator(List):
    p = random.choice(List)
    return p
def win():
    print("Wohoo!!!  You win\n")
    #speak("Congratulations User, You Win the Game")

def loss():
    print("Oh no!!!  You Loss")
    #speak("Fortunately You Lossed User")

def main():
    
    n = int(input("Enter number of sets to play:"))
    print("\n")

    win_count = 0
    loss_count = 0
    match_tied = 0

    for i in range(0,n):
        user_input = input("Enter your choice:")
        computer_input = random_generator(List)
        print("Computer's Choice: " + str(computer_input))
        print("----------\n")

        if(user_input == ">8" and computer_input == "|-|"):
            print("Result: User Wins\n")
            win_count = win_count + 1
        elif(user_input == "O" and computer_input == ">8"):
            print("Result: User Wins\n")
            win_count = win_count + 1
        elif(user_input == "|-|" and computer_input == "O"):
            print("Result: User Wins\n")
            win_count = win_count + 1
        elif(user_input == computer_input):
            print("Result: Match Tied\n")
            match_tied = match_tied + 1
        else:
            print("Result: Computer Wins\n")
            loss_count = loss_count + 1

    print("Number of times user wins: " + str(win_count) + "\n")
    print("Number of times user losses: " + str(loss_count) + "\n")
    print("Number of tied matches: " + str(match_tied) + "\n")

    if (win_count > loss_count):
        win()
    elif (win_count < loss_count):
        loss()
    else:
        print("Game Tied\n")

if __name__ == "__main__":
    print("\n ### Welcome User ### \n")
    #speak("Welcome User")
    main()