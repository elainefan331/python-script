import csv

input_file1 = '../../SNP/name_category_generated/unique_name_category/chr7_0_unique_name_category.tsv'
input_file2 = '../../SNP/name_category_generated/unique_name_category/chr7_1_unique_name_category.tsv'
input_file3 = '../../SNP/name_category_generated/unique_name_category/chr7_2_unique_name_category.tsv'
input_file4 = '../../SNP/name_category_generated/unique_name_category/chr7_3_unique_name_category.tsv'
input_file5 = '../../SNP/name_category_generated/unique_name_category/chr7_4_unique_name_category.tsv'
output_file = '../../SNP/name_category_generated/unique_name_category/chr7_unique_name_category.tsv'
uniq_dict = {}

with open(input_file1, mode='r', encoding='utf-8') as file1, \
     open(input_file2, mode='r', encoding='utf-8') as file2, \
     open(input_file3, mode='r', encoding='utf-8') as file3, \
     open(input_file4, mode='r', encoding='utf-8') as file4, \
     open(input_file5, mode='r', encoding='utf-8') as file5:
    reader1 = csv.DictReader(file1, delimiter='\t')
    reader2 = csv.DictReader(file2, delimiter='\t')
    reader3 = csv.DictReader(file3, delimiter='\t')
    reader4 = csv.DictReader(file4, delimiter='\t')
    reader5 = csv.DictReader(file5, delimiter='\t')
    
    
    for row in reader1:
        category = row['category']
        name = row['name']
        uniq_dict[name] = category
    
    for row in reader2:
        category = row['category']
        name = row['name']
        uniq_dict[name] = category
        
    for row in reader3:
        category = row['category']
        name = row['name']
        uniq_dict[name] = category
    
    for row in reader4:
        category = row['category']
        name = row['name']
        uniq_dict[name] = category
    
    for row in reader5:
        category = row['category']
        name = row['name']
        uniq_dict[name] = category
        
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    
    writer.writerow(['name', 'category'])
    
    for name, category in uniq_dict.items():
        writer.writerow([name, category])
    