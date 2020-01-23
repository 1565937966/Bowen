file1_name=input("Pls enter a file:")
file2_name=input("Pls enter another file:")
def compare_file(file1_name,file2_name):
    count=0
    differ=[]
    try:
        with open (file1_name)as f1, open(file2_name)as f2:
            for line1 in f1:
                line2=f2.realine()
                count+=1
                if line1!=line2:
                    differ.append(count)
        return differ
    except OSError as reason:
        print("The file cannot be found")
        
zbw=compare_file(file1_name,file2_name)


if len(zbw)==0:
    print("Same content in this file")
else:
    print("The file has %d diffrences"%(len(zbw)))
    for each in zbw:
        print("%d rows are different"%(each))
        
