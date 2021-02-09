def GetInput() -> None:
    try:
        #try to excecute this code
        inp = int(input("Please provide an int: "))
    except:
        #if any error jappeneds in the try blokc, meaning that the provided input cannot be converted to an int

        #inform the user about it
        print("You didn't provide an int.")

        #and ask the user for the input again
        GetInput()
    else:
        #else if an error didn't happen, meaning the code in the try block was run successfully

        #display the int the user provided
        print(f"You provided: {inp}")
    finally:
        #The code in the finally block will be executed no matter whether an error happened in the try block or not
        print("The function ended")

#Call the function
GetInput()