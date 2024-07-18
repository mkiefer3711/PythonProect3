# Function to test if a run is rising
def rising_runs(s):
    
    # Sets the count variable equal to 1
    count= 1
    
    # Sets the prev_run variable equal to 0
    prev_run = 0
    
    # Sets the index variable equal to 0
    index = 0
    
    # For loop for each character in s
    for char in s:
        
        # If statement for if the index variable is equal to the length of s subtracting 1
        if index == len(s) - 1:
            # If it is equal, it will return print "This string is rising"
            return print("This string is rising")
        
        # If statement for if the character is equal to the position in "s" that is equal to index plus 1 
        if char == s[index + 1]:
            # If it is equal, then we add 1 to the count variable
            count = count + 1
        
        # If statement for if the character is not equal to the position in "s" that is equal to index plus 1
        if char != s[index + 1]:
            # If statement that if the count of the previous run is greater than the count of the new run
            if prev_run > count:
                # Then it will return print that the string is not rising
                return print("This string is not rising")
            
            # Sets prev_run variable equal to count variable
            prev_run = count
            count = 1
        # Sets index equal to index plus 1 
        index = index + 1
    # Will print "This string is rising" if the if statements don't apply
    print("This string is rising")



# The main function where the program starts
def main():
    
    # Input for a string
    word= input("Enter a string: ")
    
    # While loop that will keep looping unless the string is equal to a blank space
    while word != "":
        # Puts the input into the rising_runs function
        rising_runs(word)
        print()
        # Continues asking for an input
        word= input("Enter a string: ")
        

# Calls for the main function       
main()

