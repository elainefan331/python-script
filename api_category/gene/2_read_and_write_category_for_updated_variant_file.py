import csv

input_file_path = '../../SNP/variant_DB/dbSNP154_chr7_4_MUSC_AnnotationResults.txt_addID_updated.tsv'    # Replace with your input file name
output_file_path = '../../SNP/name_category_generated/chr7_4_name_category_generated.tsv'

# chunk_size = 10000  # Number of lines to process at a time

def process_row(row, writer):
    writer.writerow([row['variantID'], 'variant'])
    writer.writerow([row['RSID'], 'variant'])
    writer.writerow([row['GeneName_ID_Ensembl'], 'gene'])

with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(['name', 'category'])
        
        for row in reader:
            process_row(row, writer)
        
        # Process the remaining rows
        # if chunk:
        #     process_chunk(chunk, writer)
