"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9
    print(f"Temperature: {temp_in_fahrenheit}F = {temp_in_celsius}C")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()