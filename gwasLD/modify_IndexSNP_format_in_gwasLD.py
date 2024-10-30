# already finished

import csv;

input_file_path = '../gwasLD_DB/gwas_catalog_v1.0.2-associations_e100_r2020-12-15.tsv_chr23_gwasLD_AnnotationResults.txt_mongoDB.txt'    # Replace with your input file name
output_file_path = '../gwasLD_DB/gwasLD_DB_tsv/gwas_catalog_v1.0.2-associations_e100_r2020-12-15.tsv_chr23_gwasLD_AnnotationResults.txt_mongoDB.tsv'

# Read the original file
with open(input_file_path, 'r') as file:
    tsv_file = csv.reader(file, delimiter="\t")
    tsv_data = list(tsv_file)
    
header = tsv_data[0]
data = tsv_data[1:]

# modify the column values
for line in data:
    line[header.index('IndexSNP')] = line[header.index('IndexSNP')].replace("_", "-")

# insert header to updated data
data.insert(0, header)

# write the new file
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(data)
    
print(f"saved to {output_file_path}")