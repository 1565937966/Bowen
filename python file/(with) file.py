try:
    with open("Mytext1.txt","w") as file:
        #for each_line in file:
         #   print(each_line)
         file.write("Hello world")
except OSError as reason:
    print("Wrong!Reason:"+str(reason))
