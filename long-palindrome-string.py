def longest_palindromic_substring(string):
    res=1
    str_res=string[0]
    for i in range(0,len(string)):
        left=i
        right=i
        while(left>=0 and right<len(string) and string[left]==string[right]):
            if(right-left+1>res):
                res=right-left+1
                reverse=string[left:right+1]
            left-=1
            right+=1
        left=i
        right=i+1
        while(left>=0 and right<len(string) and string[left]==string[right]):
            if(right-left+1>res):
                res=right-left+1
                str_res=string[left:right+1]
            left-=1
            right+=1
    return reverse
string=input()
print(longest_palindromic_substring(string))