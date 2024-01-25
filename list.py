# names = ['john', 'bob','mosh', 'sarah']
# print(names)
# names[0]= 'jon'
# print(names)

numbers=[100,3,4,2,5,7,8,10]
largest=numbers[0]
numbers.insert(0,90)
numbers.sort()
numbers.reverse()
print(numbers)
for x in numbers:
    if(x > largest):
        largest= x
print(f"largest number is {largest}")

