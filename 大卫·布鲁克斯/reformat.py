def reformat_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Merge lines to form complete sentences
    merged_lines = []
    sentence = ""
    for line in lines:
        # Strip leading and trailing whitespace
        stripped_line = line.strip()
        if stripped_line:
            sentence += " " + stripped_line if sentence else stripped_line
            # If the line ends in a period, it's the end of a sentence
            if stripped_line.endswith('.'):
                merged_lines.append(sentence)
                sentence = ""
        else:
            # Empty line indicates a paragraph break
            if sentence:
                merged_lines.append(sentence)
                sentence = ""
            merged_lines.append("")

    # Add the last sentence if it wasn't followed by an empty line
    if sentence:
        merged_lines.append(sentence)

    # Write to the output file, adding <br/> before double newlines for paragraphs
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in merged_lines:
            if line:
                file.write(line + "<br/>\n\n")  # Add <br/> at the end of a paragraph
            else:
                file.write("\n")  # Keep paragraph breaks as is

# Example usage
input_file_path = 'test.txt'  # Path to your input .md file
output_file_path = 'output.md'  # Path to your desired output .md file
reformat_text(input_file_path, output_file_path)
