import random

class Number:
    def __init__(self, lower_bound, upper_bound):
        self.number = random.randint(lower_bound, upper_bound)


    def guess_num(self, num, lower_bound, upper_bound):
        attempt = 6
        
        while(attempt > 0):
            if(num < lower_bound or num > upper_bound):
                print("Number is not in range. Please try again.")
            if(num > self.number):
                print("You guessed too high. Please try again.")
                num = int(input(f"You have {attempt} attempts to guess: "))
            elif (num < self.number):
                print("You guessed too low. Please try again.")
                num = int(input(f"You have {attempt} attempts to guess: "))  
            else:
                print(f"Your guess is correct. The number is {num}. You win!")
                break
            attempt -= 1
            if(attempt == 0): 
                print(f"You have no more attemtps to guess. You lost. Answer was {num}.")




def main():

    while(1):
        try:
            lower_bound = int(input("Enter lower bound of range: "))
            upper_bound = int(input("Enter upper bound of range: "))
            if(lower_bound > upper_bound):
                print("Lower bound can't be greater than upper bound. Please enter the range again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        if(lower_bound < upper_bound):
            break
    
        
    num = int(input("Guess the integer number between the range. You have 7 attempts to guess: "))

    obj = Number(lower_bound, upper_bound)
    obj.guess_num(num, lower_bound, upper_bound)


if __name__=="__main__":
    main()