import argparse
from pathlib import Path
import re


# Create the parser
my_parser = argparse.ArgumentParser(description='Prepare a platform article for blog publishing.')
# Add the arguments
my_parser.add_argument('File',
                       metavar='file',
                       type=str,
                       help='the path to the file to be sanitized')
# Execute the parse_args() method
args = my_parser.parse_args()
input_path = Path(args.File)

if not input_path.is_file():
    print('The file specified does not exist')
    sys.exit()

with open(input_path, 'r+') as fin:
    content = fin.read()
    # take out bootstrap-specific formatting of information boxes
    # and replace with making them comments
    content = re.sub(r"<div\sclass='alert+\s+\w+-\w+'\srole='alert'>\n\s+(<strong>\w+:<\/strong>\s)?", ">", content)
    content = re.sub(r"<\/div>\n", "", content)
    # upscale the levels of the headings by one (title will remain only 1st-level heading)
    content = re.sub(r"###\s+", "## ", content)
    content = re.sub(r"####\s+", "### ", content)
    fin.seek(0)
    fin.truncate(0)
    fin.write(content)

if __name__ == '__main__':
    args = my_parser.parse_args()