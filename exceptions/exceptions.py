try:
    age = int(input("Age: "))
    print(age)
except ZeroDivisionError:
    print("age cannot b zero")
except ValueError:
    print("invalid value")