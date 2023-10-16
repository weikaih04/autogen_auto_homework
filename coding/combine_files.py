# filename: combine_files.py

import nbformat as nbf
import os

# Define the paths to the files
ipynb_file_path = './dataset/project1/demo.ipynb'
md_file_path = './dataset/project1/instructions.md'
output_file_path = './answer/result.ipynb'

# Read the .ipynb file
with open(ipynb_file_path, 'r') as f:
    ipynb_content = nbf.read(f, as_version=4)

# Read the .md file
with open(md_file_path, 'r') as f:
    md_content = f.read()

# Add the .md content as a markdown cell to the .ipynb content
md_cell = nbf.v4.new_markdown_cell(md_content)
ipynb_content.cells.append(md_cell)

# Write the combined content to the output file
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
with open(output_file_path, 'w') as f:
    nbf.write(ipynb_content, f)

print("Files combined successfully.")