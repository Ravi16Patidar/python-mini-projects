# simple calcuator

print("Simple Calculator")
numberCount=int(input("How many numbers you want to enter"))
numbers=[]
try:
    print("Please enter numbers")
    for x in range(0,numberCount):
        numbers.append(int(input()))
except ValueError:
    print("Please enter a valid number.")

print(numbers);
operation=input("""Enter +
Enter -
Enter *
Enter /
""")
match operation:
    case "+":
        sum=0;
        for x in numbers:
            sum+=x
        print(sum)
    case "-":
        subtration=numbers[0];
        for x in numbers[1:]:
            subtration-=x
        print(subtration)
    case "*":
        multiplication=1;
        for x in numbers:
            multiplication*=x
        print(multiplication)
    case "/":
        division=numbers[0]
        for x in numbers[1:]:
            division/=x
        print(division)
    