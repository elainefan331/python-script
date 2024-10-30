import csv;

input_file_path = '../../SNP/name_category_generated/chr7_4_name_category_generated.tsv'
output_file_path = '../../SNP/name_category_generated/unique_name_category/chr7_4_unique_name_category.tsv'

uniq_dict = {}

with open(input_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        category = row['category']
        if ';' in row['name']:
            row['name'].replace(';', ',')
        
        if ',' in row['name']:
            name_list = row['name'].split(',')  
            for name in name_list:
                uniq_dict[name] = category
        else:
            name = row['name']
            uniq_dict[name] = category
                 
            
with open(output_file_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    
    # Write the header
    writer.writerow(['name', 'category'])
    # Write the dictionary contents
    for name, category in uniq_dict.items():
        if name != "NONE" and name != "NA":
            writer.writerow([name, category])