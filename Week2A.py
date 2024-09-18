'''1.	Challenge 1: FizzBuzz
Write a program that prints the numbers from 1 to 50.
 For multiples of 3, print “Fizz” instead of the number,
   and for multiples of 5, print “Buzz”. For numbers which are 
   multiples of both 3 and 5, print “FizzBuzz”.
'''
def listExpand(name, expander):
    print("\nHere are all of the", name,"Numbers: ")
    for index, i in enumerate(expander):
      if index == len(expander)-1:
        print (i)
      else:
        print (i, end=", ")

while True:  
  counter = 1   
  fizznumbers = []
  buzznumbers = []
  fizzbuzznumbers = []
  try:
    number = input("What is your number (0 to Exit): ")
    number = int(number)

  except:
    print("invalid entry. Please Try again")
  
  if number == 0:
    break
  
  while counter <= number:
    print (counter, end=" ")
    if counter % 3 == 0:
      print("Fizz", end="")
      fizznumbers.append(counter)

    if counter % 5 == 0:
      print("Buzz", end="")
      buzznumbers.append(counter)

    print()
    counter+= 1
  for i in fizznumbers:
    for j in buzznumbers:
      if j == i: 
        fizzbuzznumbers.append(j)

  listExpand("FIZZ", fizznumbers)
  listExpand("BUZZ", buzznumbers)
  listExpand("FIZZBUZZ", fizzbuzznumbers)