phone=input("enter your number: ")

numbers={
    "1":"one",
    "2":"two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in phone:
    output += numbers.get(ch,"!") + " "
print(output)