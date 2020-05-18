import random

val = random.randint(0, 20)
print('welcome to this guess game\n')
print(val)

guess = int(input("try to find the number i have between 0 and 20\n"))
while (guess!=val):
    if (guess > val):
        print("Your guess is to long")
        guess = int(input("try to find the number i have between 0 and 20\n"))
    else:
        print("Your guess is to short!")
        guess = int(input("try to find the number i have between 0 and 20\n"))
if (guess == val):
    print("Congratulations you got it!")



    '''elif (guess < val):
        print("Your guess is to short")
        guess = int(input("try to find the number i have between o and 20\n"))
    else:
        print("Congratulations you got it!")
      '''