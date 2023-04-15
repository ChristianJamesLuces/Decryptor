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
while True:
    print(intro)
    print("\033[45;1m" + "This program will decrypt your encrypted input using the following character substitute:\n" + "\033[0m") # Explains the function of the program
    print("\033[93m" + character_susbsitute + "\033[0m")
    print("-" * 100)

    # ask the user for input
    ask = str(input("\033[1m" + "Enter a string to decrypt: " + "\033[0m"))
    output = ""

    # check each special characters and decrypt it
    for char in ask:
        if char not in special_characters:
            output += "\033[94;1m" + char + "\033[0m"
        else:
            output += "\033[91;4;1m" + special_characters[char] + "\033[0m"

    # print the output
    print(("\033[93m" + "The decrypted input is: " + "\033[0m" + output))

    # Asking the user if they want to try it again
    answer = str(input("\nDo you want to try it again? (Yes or No): "))

    # If the user want to try it again 
    if answer in yes_option:
        print("\n\n")
    # If the user do not want to try it again
    elif answer in no_option:
        print("\n" + "<" * 100) 
        print(gratitude.center(100))
        print(">" * 100)
        break
    # If the user did not input a valid answer
    # Exit the loop after a valid input is given
    # Go back to the start of the loop