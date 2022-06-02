my_string = "test string test, test string testing, test string test string"
startIndex = 0
count = 0
for i in range(len(my_string)):
    k = my_string.find('test', startIndex)
    if(k != -1):
        startIndex = k+1
        count +=   1
        k = 0
print("Total count of substing test is: ", count )

text = "hello world guru99"
#splits at space
print(text.split())
text = "hello, world, guru99, purna, karki,"
split_1 = text.split(',', 4)
print(text.split(", "))
text = "Hello, wold:, guru99"
#splits at ','
print(text.split(":"))
