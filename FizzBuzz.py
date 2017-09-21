print "Welcome to the FizzBuzz game!"
end = raw_input("Please enter a number between 1 and 100: ")

#try-except statement: if code inside try fails the program goes to the except part.
try:
    end = int(end) #convert string into number

    for num in range(1, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num
except Exception as e:
    print "Please enter a whole number."
