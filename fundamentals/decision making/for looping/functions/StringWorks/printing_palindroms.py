# longest palindromic substring from given string
text="RACECAR"
longest_palindrome=""
for i in range (0,len(text)):

    left=i
    right=i

    while(left>=0 and right<len(text) and text[left]==text[right]):
        current_palindrome=text[left:right+1]
        print(current_palindrome)
        left=left-1
        right=right+1



        


    

