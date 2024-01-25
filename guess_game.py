secret = 9
guess_num=1
while guess_num<=3:
    guess= int(input("guess : "))
    guess_num +=1
    if guess == secret:
        print("you won")
        break
else:
    print("sorry try again")