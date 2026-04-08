import random

def play_game():
    print("Welcome to Number guessing game!")
    
    print("\n Choose difficulty level:")
    print("1. Esay (1 to 50, 10 chances)")
    print("2. Medium (1 to 100, 7 chances)")
    print("3. Hadr (1 to 300, 5 chances)")
    
    choice = input("Enter your choice (1/2/3):")
    
    if choice == '1':
        number = random.randint(1, 50)
        max_attempts = 10
        
    elif choice == '2':
        number = random.randint(1, 100)
        max_attempts = 7
        
    elif choice == '3':
        number = random.randint(1, 300)
        max_attempts = 5
        
    else:
        print("Invalid Choice! Defaulting to Medium")
        number = random.randint(1, 100)
        max_attempts = 7
        
    attempts = 0
    
    print("Start Guessing...🔍")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess🤔:"))
            attempts += 1
            
            if guess > number:
                print("Too high!📈 Try again")
                
            elif guess < number:
                print("Too low!📉 Try again")
                
            else:
                print(f"Congratulations!🎉 You guessed the correct number in {attempts} attempts.👌🔥")
                return
            
            print(f"Attemts left: {max_attempts - attempts}")
            
        except ValueError:
            print("please enter a valid number!")
            
    print(f"Game Over!❌ The number was {number}")
    

while True:
    play_game()
    again = input("Do you want to play again? (yes/no):").lower()
    
    if again != 'yes':
        print("👋🏿Thanks for playing!")
        
     
        break   