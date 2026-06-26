# from this point on to push something to github use #
# git add .
# git commit -m "message"
# git push
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