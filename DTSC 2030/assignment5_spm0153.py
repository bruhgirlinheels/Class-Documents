Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>  
... def count_words(description):
...    # Split the description into words and return the count
...    words = description.split()
...    return len(words)
... def main():
...    # Prompt the user for the input file name
...    input_file_name = input("Enter the name of the input file: ")
...    # Check if the file exists
...    while True:
...        try:
...            with open(input_file_name, 'r') as file:
...                # Read lines from the file
...                lines = file.readlines()
...                break
...        except FileNotFoundError:
...            input_file_name = input("File not found. Please enter a valid input file name: ")
...    # Prompt the user for the output file name
...    output_file_name = input("Enter the name of the output file: ")
...    # Open the output file in write mode (this will erase the old file if it exists)
...    with open(output_file_name, 'w') as output_file:
...        # Iterate over lines in groups of 3 (ID, description, pre-counted number)
...        for i in range(0, len(lines), 3):
...            student_id = lines[i].strip()
...            description = lines[i + 1].strip()
...            pre_count = int(lines[i + 2].strip())
...            # Count the words using the provided function
...            word_count = count_words(description)
...            # Check if the pre-counted number is correct
...            is_correct = word_count == pre_count
...            # Write the results to the output file
...            output_file.write(f"{student_id}\n{word_count}\n{is_correct}\n")
...            # Print status message to the console
...            print(f"Processed {student_id}. Word count: {word_count}. Pre-count is correct: {is_correct}")
...    print(f"Results written to {output_file_name}")
... if __name__ == "__main__":
...    main()
