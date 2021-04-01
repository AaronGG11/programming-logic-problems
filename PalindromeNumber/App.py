def checkPalindrome(str):
   
    # Run loop from 0 to len/2
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
           
    # If the above loop doesn't
    #return then it is palindrome
    return True



def main():
    st = "112233445566778899000000998877665544332211"
    
    if(checkPalindrome(st) == True):
        print("it is a palindrome")
    else:
        print("It is not a palindrome")


if __name__ == "__main__":
    main()