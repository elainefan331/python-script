import csv

input_file = '../../database/gene_DB/protein_coding_gene.tsv'
output_file = '../../database/gene_DB/protein_coding_gene_remove_duplicates.tsv'


uniq_dict = {}


with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    
    for row in reader:
        name = row['Gene_Name']
        if name in uniq_dict:
            uniq_dict[name] += 1
        else:
            uniq_dict[name] = 1
count = 0
for key in uniq_dict:
    if uniq_dict[key] > 1:
        print("gene name: ", key)
        print('repeated: ', uniq_dict[key])
        count += 1
print("count: ", count)