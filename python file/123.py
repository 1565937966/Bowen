def count(*setence):
    leng=len(setence)
    for i in range(leng):
        letters=0
        space=0
        digit=0
        others=0
        for each in setence[i]:
            if each.isalpha():
                letters+=1
            elif each.isdigit():
                digit+=1
            elif each==' ':
                space+=1
            else:
                others+=1
        print("第%d个字符串有字母%d个，数字%d个，空格%d个，其他%d个." %(i+1,letters,digit,space,others))
count(setence)
