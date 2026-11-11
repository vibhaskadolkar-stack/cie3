string = "madam"
if string.lower() == string[::-1].lower():
   print(f"'{string}' is a palindrome.")
else:
   print(f"'{string}' is not a palindrome.")