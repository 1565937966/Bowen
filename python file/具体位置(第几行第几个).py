import os

root=input('Please input the root of file:')
key_words=input('Please input the word:')
def each_txt_file(root,key_words):
    os.chdir(root)
    txt_file=[]
    for each_file in os.listdir(os.curdir):
        ext=os.path.splitext(each_file)[1]
        if ext=='txt':
            txt_file.append(each_file)
    for each_file in txt_file:
        search_file(each_file,key_words)
        print (print_pos)


def search_file(each_file,key_words):
    f=open(os.getcwd()+os.sep+each_file)
    counter=0
    row=dict()
    for eachline in f:
        counter+=1
        if key_words in eachline:
            row[counter]=search_key(eachline,key_words)

    f.close()
    return row

def search_key(eachline,key_words):
    begin=eachline.find(key_words)
    pos=[]
    while begin!=-1:
        pos.append(begin)
        begin=eachline.find(key_words,begin+1)
    return pos
def print_pos(row):
    keys=row.keys()
    keys=sorted(keys)
    for each_key in keys:
        print("Key words appeared in %s row and %d position"%(each_key,row(each_key)))
each_txt_file(root,key_words)
