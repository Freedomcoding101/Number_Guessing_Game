high_score = 0

def start_game():
  
    import random
    global high_score
    x=2
    guesses = 0
    guess_list = []
    number = int(random.randint(1, 10))
    print ("-----Welcome to The Number Guessing Game-----\n")
    print ("-----Your Mission Is To Guess The Number-----\n")
    user_name = input("-----Please enter your name to begin-----   \n")
    print ("\nOkay {}, today we are going to guess a number between 1-10\n In the end I will tell you how many tries you took!!\n\n".format (user_name)) 
    if high_score == 0:
        print("--There has been no high score set yet! Be the first to set a new High Score!--\n")
    else:
        print(f"------The current high score is {high_score}------\n")
    
    while x == 2:
        try:
            user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
            if user_guess > 10 or user_guess <=0:
                raise ValueError
            elif user_guess < number:
                guesses += 1
                guess_list.append(user_guess) 
                print("\nThe Number is Higher!\n")
            elif user_guess > number:
                guesses += 1
                guess_list.append(user_guess)
                print("\nThe Number is Lower!\n")
            elif user_guess == number:
                guesses += 1
                guess_list.append(user_guess)
                print("You Got It!!\n")
                print(f"You guessed it in {guesses} tries!\n")
                if high_score == 0 or high_score > guesses:
                    high_score = guesses
                elif high_score < guesses:
                    high_score = high_score
                print(f"The high score is {high_score}!\n")
                break
        except ValueError:
            print("That is not a valid number! Enter a number between 1-10!!\n")
            continue
    
    print("The game is now over!! Would you like to play again?\n")
    
    try:
        new_game = input("Type YES or NO  \n").lower()
        if new_game == "yes":
            start_game()
        elif new_game == "no":
            print("\nOkay thanks for playing!")
        else:
            raise NameError("That is not a valid answer\n")
            new_game = input("Type YES or NO  \n").lower()
            if new_game == "yes":
                start_game()
            elif new_game == "no":
                print("\nOkay thanks for playing!")
    except NameError:
        print("That is not a valid answer!\n")
        new_game = input("Type YES or NO \n").lower()
        if new_game == "yes":
            start_game()
        elif new_game == "no":
            print("\nOkay thanks for playing!")
            
start_game()        
            
            