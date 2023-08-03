"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

def start_game():
    import random
    guesses = []
    number = int(random.randint(1, 10))
    print ("-----Welcome to The Number Guessing Game-----\n")
    print ("-----Your Mission Is To Guess The Number-----\n")
    user_name = input("-----Please enter your name to begin-----   \n")
    print ("\nOkay {}, today we are going to guess a number between 1-10\n In the end I will tell you how many tries you took!!\n\n".format (user_name)) 
    
    try:
        user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
        if user_guess <=10 and user_guess >0:
                guesses.append(user_guess)
        while user_guess >10 or user_guess <0:
            raise ValueError("Your number is outside of the range, please enter a number between 1 and 10\n\n")
            user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
            if user_guess <=10 and user_guess >0:
                guesses.append(user_guess)
                break
    except ValueError:
        print("Your number is outside of the range, please enter a number between 1 and 10\n\n")
        user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
    
                
        
    while user_guess != number:
        try:
            while user_guess >10 or user_guess <=0:
                print("\nYour number is outside of the range, please enter a number between 1 and 10\n\n")
                user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
                if user_guess <=10 and user_guess >0:
                    guesses.append(user_guess)
                    break
                
            if user_guess < number:
                user_guess = int(input ("\nIt's Higher!! Please Try again!  \n"))
                if user_guess <=10:
                    guesses.append(user_guess)
                
                
            elif user_guess > number:
                user_guess = int(input ("\nIt's Lower!! Please Try Again!  \n"))
                if user_guess <=10:
                    guesses.append(user_guess)
                
    
        except ValueError:
            print("\n---------That is not a valid number---------\n")
            user_guess = int(input ("-----Please enter a number between 1-10 -----\n"))
            if user_guess <=10:
                guesses.append(user_guess)
                
                
    if user_guess == number:
        print("\nYou got it!\n")
        if len(guesses) <2:
            print("You guessed it in {} try!\n".format(len(guesses)))
        else:
            print("You guessed it in {} tries!\n".format(len(guesses)))
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
            
  
   
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    
    2. Store a random number as the answer/solution. COMPLETE
    3. Continuously prompt the player for a guess. COMPLETE
      a. If the guess greater than the solution, display to the player "It's lower". COMPLETE
      b. If the guess is less than the solution, display to the player "It's higher". COMPLETE
    
    4. Once the guess is correct, stop looping, inform the user they "Got it" COMPLETE
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """