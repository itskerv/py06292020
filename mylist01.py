#!/usr/bin/python3
'''
Author: KervinRodriguez@me.com
The purpose of this program is to teach students how Python lists work. 
Students studying JSON may understand a list as an "array".
'''



def main():
    movies = [] # one way to create a list
    movies.append("Avatar") # .append is a list method that applies the value
                            # passed to it at the END of the list

    movies. append("Back to the Future")

    print(movies) # use the print FUNCTION to display to std out
    
    # ["Avatar", "Back to the Future"]
    print(movies[0]) # display Avatar

    movies.append("Ghostbusters") # adds Ghostbusters to the end of the list/array

    print(movies[2]) # prints out Ghostbusters
    print(movies[1]) #
    

# Zach says this is the best way to run the main function
if __name__ == "__main__":
    main()





