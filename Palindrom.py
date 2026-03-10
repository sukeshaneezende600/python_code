#Example1 
def ispalindrom (s):
    return s==s [::-1]
s="madam"
ans= ispalindrom(s)
if ans:
    print("yes")
else:
    print("no")   

#example 2

def ispalindrom(s):
    return s==s[::-1]
s= "sukeshanee"
ans= ispalindrom(s)
if ans:
    print("Yes")
else:
    print("No")    


# example 1.Using 2nd Method
def ispalindrome(s):
    rev = ''.join(reversed(s))  # Reverse the string
    if s == rev:  # Check if the string is equal to its reverse
        return True
    return False

s = "civic"
ans = ispalindrome(s)  # Call the function and store the result

if ans:  # Check the result and print "yes" if True, else print "No"
    print("Yes")
else:
    print("No")

#example 2

def ispalindrome(s):
    rev = ''.join(reversed(s))  # Reverse the string
    if s == rev:  # Check if the string is equal to its reverse
        return True
    return False

s = "Waterfall"
ans = ispalindrome(s)  # Call the function and store the result

if ans:  # Check the result and print "yes" if True, else print "No"
    print("Yes")
else:
    print("No")

