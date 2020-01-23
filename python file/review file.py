counter=0
file_name="counter.txt"
with open(file_name)as f:
	for each_line in f:
		counter+=1
		print(each_line)
	print(counter)

    
