# 2: Pseudocode
import pyfiglet

# Define variables
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
no_option = ("No", "no", "NO", "n", "N")
yes_option = ("Yes", "yes","YES","y","Y")
character_susbsitute = "\t'a' = *\n\t'e' = &\n\t'i' = #\n\t'o' = +\n\t'u' = !\n"
special_characters = {"*": "a", "&": "e", "#": "i", "+": "o", "!": "u"}
gratitude = "\033[42m" + "(: Thank you for using this program! :)" + "\033[0m"

# Display welcome message and its function
print(intro)
print("\033[45;1m" + "This program will decrypt your encrypted input using the following character substitute:\n" + "\033[0m") # Explains the function of the program
print("\033[93m" + character_susbsitute + "\033[0m")
print("-" * 100)
# ask the user for input
# check each character
# if *, change it to a
# if &, change it to e
# if #, change it to i
# if +, change it to o
# if !, change it to u
# print the output
# Asking the user if they want to try it again
# If the user want to try it again 
# If the user do not want to try it again
# If the user did not input a valid answer
# Exit the loop after a valid input is given
# Go back to the start of the loop