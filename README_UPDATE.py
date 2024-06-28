import datetime

# Open the README.md file in append mode
with open('README.md', 'a') as file:
    # Get input from the user
    line = input("Enter a line to append to README.md: ")

    current_date_time = str(datetime.datetime.now())
    
    # Append the line to the file
    file.write( "<br>" +current_date_time + " : " + line + '\n')