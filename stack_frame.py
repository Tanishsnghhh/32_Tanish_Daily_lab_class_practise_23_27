def main():
    a = 100
    b = 55
    
    # Print the contents of the directory within the main() function
    print("in function main…......dir() =", dir())
    
    # Define a nested function absdiff(x, y) to calculate absolute difference
    def absdiff(x, y):
        # Print the contents of the directory within the absdiff() function
        print("in function absdiff...dir() =", dir())  
        
        # Calculate the absolute difference between x and y
        if x > y:
            z = x - y
        else:
            z = y - x 
        
        return z
    
    # Call the absdiff function with values a and b
    result = absdiff(a, b)
    
    # Print the absolute difference between a and b
    print("The absolute value of ", a ,"-", b," =", result)

# Call the main function
main()




#dir()    #dir() to display the names present within the module.