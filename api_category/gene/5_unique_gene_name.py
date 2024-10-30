import csv

input_file = '../../SNP/name_category_generated/unique_name_category/chr7_unique_name_category.tsv'
output_file = '../../SNP/name_category_generated/unique_name_category/chr7_unique_gene_name.tsv'

uniq_dict = {}

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    
    for row in reader:
        if row['category'] == "gene":
            name = row['name']
            if ";" in name:
                gene_list = name.split(";")
                for gene in gene_list:
                    uniq_dict[gene] = row['category']
            else:
                uniq_dict[name] = row['category']
                
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    writer.writerow(['name', 'category'])
    
    for name, category in uniq_dict.items():
        if name != "NONE" and name != "NA":
            writer.writerow([name, category])
    
    