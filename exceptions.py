number = 0
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number.")
    except(ValueError, NameError):
        print("Handling multiple errors")
    except:
        print("Unknown error occurred.")

print("Number entered is ", number)
