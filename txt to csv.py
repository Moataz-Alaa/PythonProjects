def convert_spaces_to_commas(input_file, output_file, num_col):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        modified_lines = []
        for line in lines:
            line = line.replace(' ', ',', num_col-1)
            line = line.replace(' ', '')
            modified_lines.append(line)
        
        with open(output_file, 'w') as file:
            file.writelines(modified_lines)
        
        print(f"Converted file saved to {output_file}")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
input_file = 'D:\Projects\MySQLProjects\Submissions.txt'  # Replace with your input file path
output_file = 'D:\Projects\MySQLProjects\Submissions.csv'  # Replace with your desired output file path
num_col = 4 # Number of columns
convert_spaces_to_commas(input_file, output_file, num_col)

# This script assumes that the csv is witout a header but maybe it could work with a header who knows
# This script won't work if the text of individual columns can contain whitespaces
# This script only works if each field is seperated with only ONE whitespace and there is a new line character at the end of each line
