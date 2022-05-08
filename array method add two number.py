# Add user input

number =int(input("how many number Enter the user input"))
sum = 0
avrage =0
for i in range(number):
    num =int(input(f"enter the nuber {i} : "))
    sum = sum+num
    average = float(sum/number)
    print(f"The sum is{sum}")
    print(f"The average is {average}")