def int_input(word):
    while True:
        try:
            int(input(word))
            break
        except ValueError:
            print("This is not a int.")

words=input("Insert a number:")
int_input(words)
            

    
    



