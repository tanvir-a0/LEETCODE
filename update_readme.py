# Open the README.md file in append mode
with open('README.md', 'a') as file:
    # Get input from the user
    line = input("Enter a line to append to README.md: ")
    
    # Append the line to the file
    file.write( "<br>" + line + '\n')