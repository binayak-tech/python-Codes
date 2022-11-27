def palindrome(string):
    
    string = string.lower()
    newString = ''.join(e for e in string if e.isalnum())
    
    #This list comprehension technique is saying,
    # in a for loop check if each element e in string is alphanumemric or not,
    # if it is true then append it to the output expression E
    # after performing all comparision then join each element in E list by using .join with a empty string ""
    
    return newString == newString[::-1]
    
    
print(palindrome("%%(*&(*#@(896 **("))
