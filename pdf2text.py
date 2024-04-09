from langchain.document_loaders import PyPDFLoader
import os

################################################################################
### Name directories and find PDFs
################################################################################

# Define the source and destination directories
source_dir = "pdfs/SASID"
dest_dir = "text/SASID"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Get a list of all PDF files in the source directory
pdf_files = [f for f in os.listdir(source_dir) if f.endswith('.pdf')]

################################################################################
### Convert PDFs to text files
################################################################################

for pdf_file in pdf_files:
    # Load the PDF file
    loader = PyPDFLoader(os.path.join(source_dir, pdf_file))
    pages = loader.load_and_split()

    # Get the name of the PDF file without the extension
    pdf_name = os.path.splitext(pdf_file)[0]

    # Save each page as a text file in the SASID directory with PDF file name as a prefix
    for i, page in enumerate(pages):
        with open(os.path.join(dest_dir, f"{pdf_name}_page_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(page.page_content)



#print(pages[2].page_content)
#print(pages[3].metadata)

# write to a combined PDF
# with open("text/sasdocs/combined.txt", "w", encoding="utf-8") as f:
#     for page in pages:
#         f.write(page.page_content)
#         f.write("\n\n")  # Optional: Add two newlines between pages for clarity