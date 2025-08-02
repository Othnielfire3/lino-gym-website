for i in range(1 , 101):  # Loop from 1 to 100
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz") # Divisible by both 3 and 5
    elif i % 3 == 0:
        print("Fizz")     # Divisible by 3 only
    elif i % 5 == 0:
        print("Buzz")     # Divisible by 5 only    
    else:
        print(i)          # Not divisible by 3 or 5