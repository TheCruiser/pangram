from string import ascii_lowercase as asc_lower 
def check(s):
    return set(asc_lower)-set(s.lower()) == set([])

strng = input("Enter String : ")
if(check(strng)==True):
    print("The String is a pangram")
else:
    print("The String is not a pangram")