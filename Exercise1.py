# from this point on to push something to github use #
# git add .
# git commit -m "message"
# git push

#These are just warm up tasks actual exercises with start on Exercise2 and so on
# 1st Task of Exercsice 1
#FizzBuzz+
#Print numbers 1–100
#Replace multiples of 3 with "Fizz", 5 with "Buzz", 7 with "Pop", combos like "FizzBuzzPop"

for i in range(1, 101):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%7==0:
        print("Pop")
    else:
        print(i)

#Completed

""" Palindrome Checker
Check if string reads same backward
Ignore spaces + capital letters """

user_string = input("Enter you string: ")
if user_string == user_string[::-1]:
    print("palindrome")
else:
    print("Not Palindrome")



    
