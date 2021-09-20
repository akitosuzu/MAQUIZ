print("\033[1;32;40m  \n")


#imports
import random
import time


#Variables
points = 0 
correct_answers = 0
wrong_answers = 0
rounds_played = 0
first_number = 0
second_number = 0

#functions, decoration
def question_creator():
  global first_number 
  global second_number
  if difficulty_levels == 1:
    first_number = random.randint(0,20) 
    second_number = random.randint(0,20)
  elif difficulty_levels == 2:
    first_number = random.randint(25,45)
    second_number = random.randint(25,45)
  elif difficulty_levels == 3:
    first_number = random.randint(50,100)
    second_number = random.randint(50,100)


def yes_no(question):
  valid = False
  global yes_no_answer
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
      response = "yes"
      yes_no_answer = 1
      return response
    elif response == "no" or response == "n":
      response = "no"
      yes_no_answer = 0
      return response
    else:
      print("Please answer yes / no")


def statement_generator(statement, decoration):
  sides = decoration * 3
  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return " "

def end_of_game():
  statement_generator("Final Points: {}".format(points), "◌")
  print(" ")
  time.sleep(0.5)
  statement_generator("rounds played: {}".format(rounds_played), "◌")
  print(" ")
  time.sleep(0.5)
  print("THANKS FOR PLAYING")

def num_checker(question, low, high):
    error = "Please enter a whole number between 1 and 3"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low <= response <= high:
                return response

            # output an error
            else:
              print(" ")
              statement_generator(error,"!")
              print(" ")

        except ValueError:
            print(" ")
            statement_generator(error,"!")
            print(" ")
  
#Variable - User experience
statement_generator("WELCOME TO MAQUIZ", "●")
print(" ")
time.sleep(1.5)
input("PRESS ENTER TO START")
time.sleep(1)
print(" ")
userexperience = yes_no("Have you played MaQuith before? (y/n):")
print(" ")
if yes_no_answer == 0:
  print("Well then, here's INSTRUCTION")
  print(" ")
  input("- 1: pick a level from 1 - 3, each level has different difficulties. -")
  input("- level 1: addition of 0 - 20 / level 2: addition of 25 - 45. / level 3: addition of 50 - 100. -")
  input("- 2: and just solve the questions!! -")
  input("- whenever you want to quit type '000' -")
  print(" ")
  time.sleep(1)


#lists
difficulty_levels = ["1","2","3"]




#Tutorial


      
      

#Variables - Difficulty Of Questions
difficulty_levels = num_checker("What level of difficulty would you like to play? 1/2/3: ", 1, 3)
time.sleep(1)
print(" ")


#Amt of questions

#Questions & Answer Checkingto

#Gameplay
print(" ")
statement_generator("LEVEL {} QUESTIONS".format(difficulty_levels), "-")
print(" ")

while True:
  try:
    question_creator()
    user_answer = int(input("what is " + str(first_number) + " + " + str(second_number) + "? " ))
    if user_answer == 000:
      end_of_game()
      break
      
    if user_answer == first_number + second_number:
      print(" ")
      statement_generator("RIGHT ANSWER", "✔")
      print(" ")
      statement_generator("POINT +1", "-")
      rounds_played += 1 
      correct_answers += 1
      points += 1 

    elif user_answer != first_number + second_number:
      print(" ")
      statement_generator("WRONG ANSWER", "X")
      print(" ")
      statement_generator("POINT ADDED +0", "-")
      rounds_played += 1 
      wrong_answers += 1

  except ValueError:
    statement_generator("NUMBER ONLY PLEASE","!") 
  