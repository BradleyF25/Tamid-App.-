# add string to allow user to imput a word
s = input ("Please enter a word: ")

# reverses the word
reverse = s[::-1]

#If/Else statement checks if inputted word matches its reverse and determines if its a palindrome or not

if(s == reverse ):
  print(" yes it is a a palindrome")
else:
  print("no it is not a palindrome")
