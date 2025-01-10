# Write a function to check if a given string is a palindrome 

n =  input("Enter a string") 
rev =''
for char in n:
  rev = char + rev
if n == rev:
    print("Yes,string is palindrome")
else:
      print("No,string is not palindrome")

