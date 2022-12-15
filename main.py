# See the Instructions tab
import time
#welcome the user
print("hi! i'm squad six chat bot,how can i help you today? ")
print()
#using while loop for the code to keep running
while True:
  print("press [Enter] to continue")
  print()
  time.sleep(3)
#questions asked to the user
  info_of_school="1.You want to know about the school? choose 1."
  info_of_squad = "2.You want to know more about the squad? choose 2. "
  info_of_interest= "3. You want to know about the squad's character traits? choose 3."
  info_of_teacher = "4. You want to know about the squad's teaching assistant? choose 4."
  guess = "5. You want to know who is the squad's representative."
  riddle= "6.let's play a game ! riddle me.  "
  names= ["1.Terry S" , "2.Israel B" , "3.Beatrice K" , "4.Audrey I" , "5.Adetomiwa A"]
  print(info_of_school)
  print(info_of_squad)
  print(info_of_interest)
  print(info_of_teacher)
  print(guess)
  print(riddle)
  print()
  users_choice = int(input("choose a number: "))
  print()
# information stored in variables 
  info = "Try Kibo school is a online university that was started to improve the African tech.The program is designed in such a way that everyone that passes the interview access it easily with internet. There are personal projects and team projects that are asigned to everyone every week.Try Kibo also encourages growth as a community and personal growth." , "A Teaching assistant is assigned to every team depending on different times one picked for the online session. For squad six we chose 6pm WAT. Our teaching assistant was Stanley U. He helped us when we had a problem and gave us a few assignents during our online sessions. He made sure that everyone understood the concepts and was comfortable with it. "
#using conditionals for the correct information to be printed out
  if users_choice == 1:
    print(info[0])
  if users_choice == 2:  
    for names in  names:
     print(names)
  elif users_choice == 3:
     print("1.Terry S")
     print("2.Israel B")
     print("3.Beatrice K")
     print("4.Audrey I")
     print("5.Adetomiwa A")
     users_choice2 = int(input("choose a number depending on whose character traits you would like to know: "))
     if users_choice2 == 1:
       print("Terry S")
       print("Patient and persistent")
     elif users_choice2 == 2:
       print("Israel B")
       print("Resilent, hardworking and productive")
     elif users_choice2 == 3:
       print("Beatrice K")
       print("I can be overly patient if that's a thing")
     elif users_choice2 == 4:
       print("Audrey I")
       print("An ethusiast, driven and goal oriented")
     elif users_choice2 == 5:
       print("Adetomiwa A")
       print("finds it easy to help people out and to check up on people")
     else:
       print("You have to enter a number between 1 and 5")
  elif users_choice == 4:
    print(info[1])
  elif users_choice == 5:
    print("DRUM ROLL!")
    print("1.Terry S")
    print("2.Israel B")
    print("3.Beatrice K")
    print("4.Audrey I")
    print("5.Adetomiwa A")
    cap = int(input("guess the squad's representative:"))
    if cap == 1:
      print("You guessed right")
    else:
      print("Sorry wrong answer, Terry S is the squad's representative")
  elif users_choice == 6:
    riddle_ans = input("I’m tall when I’m young, and I’m short when I’m old. What am I? ")
    if riddle_ans == "candle" and "Candle"and "CANDLE":
      print("Congratulations! You got it right")
    else:
      print("Sorry wrong answer. The answer is candle")
  elif users_choice == "5":
    break
  else:
     print ("Please choose a number between 1 and 5")