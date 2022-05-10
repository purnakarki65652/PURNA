# Add user input

num =int(input("how many number Enter the user input: "))
numbers = []
sum = 0;
for i in range(num):
    number = int(input(f"enter the nuber {i+1} : "))
    numbers.append(number)
    sum = sum+number
average = float(sum/num)
print(f"the user entered numbers is {numbers}")
print(f"The sum is {sum}")
print(f"The average is {average}")
print("Largest number in the entered list is", max(numbers),"\nSmallest numbers in the entered list is :",min(numbers))