def palindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return False
        return True
s=input()
k=palindrome(s)
if(k):
    print("palindrome")
else:
    print("not")
