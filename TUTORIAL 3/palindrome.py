sent=input("Enter a sentence : ")
sent.lower()
a=list(sent)

a.reverse()
testst=''.join(a)
if testst==sent:
     print("It is a palindrome")
else: 
     print("It is not a palindrome")
