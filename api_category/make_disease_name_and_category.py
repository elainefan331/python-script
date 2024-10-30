# already finished


input_file = '../disease/gwas_catalog_v1.0.2-associations_e100_r2020-12-15_allChr.txt_uniq_traits_list.txt'    # Replace with your input file name
output_file = 'disease_api_category.tsv'     # Replace with your output file name
headers = 'name\tcategory'  # Replace with your actual headers

# Read the original file
with open(input_file, 'r') as file:
    lines = file.readlines()
   

# Write the header and then the original file contents to a new file
with open(output_file, 'w') as file:
    file.write(headers + '\n')  # Write the header
    
    for line in lines:
        name = line.strip() # Remove any leading/trailing whitespace including newlines
        file.write(f'{name}\tdisease\n')

   
    
    
print(f"Header added to {output_file}")
