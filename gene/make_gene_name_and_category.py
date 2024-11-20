
input_file = '../../database/gene_DB/protein_coding_gene.tsv'    # Replace with your input file name
output_file = 'gene_api_category.tsv'     # Replace with your output file name
headers = 'name\tcategory'  # Replace with your actual headers

# Read the original file
with open(input_file, 'r') as file:
    lines = file.readlines()
   
# Get the index of the Gene_Name column (assuming it's a tab-separated file with a header row)
header_line = lines[0].strip().split('\t')  # Split header line into columns
gene_name_index = header_line.index('Gene_Name')  # Find the index of 'Gene_Name' column

# Write the header and then the original file contents to a new file
with open(output_file, 'w') as file:
    file.write(headers + '\n')  # Write the header
    
    for line in lines[1:]:
        # name = line.strip() # Remove any leading/trailing whitespace including newlines
        # file.write(f'{name}\tgene\n')
        columns = line.strip().split('\t')  # Split the line into columns
        gene_name = columns[gene_name_index]  # Extract the Gene_Name value
        file.write(f'{gene_name}\tgene\n')  # Write the name and category to the output file

   
    
    
print(f"Header added to {output_file}")