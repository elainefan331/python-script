import csv

# Define the file paths
input_file_path = '../SNP/dbSNP154_chr7_4_MUSC_AnnotationResults.txt_addID'
output_file_path = '../SNP/variant_DB/dbSNP154_chr7_4_MUSC_AnnotationResults.txt_addID_updated.tsv'

# Function to process the file in chunks
def process_file_in_chunks(input_path, output_path, chunk_size=10000):
    with open(input_path, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        # Get the header and modify it
        header = next(reader)
        header = [name.replace('#Chr', 'Chr')
                        .replace('chromHMM_E129_25', 'chromHMM_osteoblast')
                        .replace('chromHMM_E026_25', 'chromHMM_hMSC') 
                  for name in header]

        # Add a new 'variantID' column if it doesn't exist
        if 'variantID' not in header:
            header.append('variantID')
        writer.writerow(header)

        # Process the file in chunks
        for i, row in enumerate(reader, start=1):
            # Ensure row has the same length as header (in case of adding 'variantID')
            if len(row) < len(header):
                row.extend([''] * (len(header) - len(row)))

            # Combine Chr, Start, Ref, and Alt to create the variantID
            chr_index = header.index('Chr')
            start_index = header.index('Start')
            ref_index = header.index('Ref')
            alt_index = header.index('Alt')
            variant_id = f"{row[chr_index]}-{row[start_index]}-{row[ref_index]}-{row[alt_index]}"
            row[header.index('variantID')] = variant_id

            writer.writerow(row)

print(f"Processing the file: {input_file_path}")

# Process the file in chunks of 10000 rows
process_file_in_chunks(input_file_path, output_file_path, chunk_size=10000)

print(f"Processed and saved to {output_file_path}")
