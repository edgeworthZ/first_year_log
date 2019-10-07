s = input('Text: ').lower()
#len(s)//2 for slicing point,len(s)%2 to adjust the point according to odd/even.
if(s[:len(s)//2][::-1] == s[len(s)//2+len(s)%2:][::-1]
   and s[::-1] == s):
    print('Double Palindrome')
elif(s[::-1] == s):
    print('Paldindrome')
else:
    print('No')
