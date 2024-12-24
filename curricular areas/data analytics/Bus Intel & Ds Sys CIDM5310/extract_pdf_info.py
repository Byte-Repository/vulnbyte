import fitz  # PyMuPDF
import pandas as pd
import os

# Function to extract text and metadata from a PDF
def extract_pdf_info(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    data = {
        "Document ID": [],
        "Page Number": [],
        "Page Type": [],
        "Text Content": [],
        "Image Content": [],
        "Metadata": []
    }

    document_id = os.path.basename(pdf_path).split('.')[0]  # Use the filename as Document ID
    prev_page_blank = False  # Track if the previous page was blank

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        images = page.get_images(full=True)
        metadata = page.get_text("dict")

        # Determine the page type
        if "banner page" in text.lower():
            page_type = "Banner Page"
        elif "bad blank" in text.lower():
            page_type = "Bad Blank"
        elif "good blank" in text.lower():
            page_type = "Blank Page"
        elif "not blank" in text.lower():
            page_type = "Not Blank"
        elif text.strip() == "":
            page_type = "Blank Page" if not prev_page_blank else "Bad Blank"
            prev_page_blank = True
        else:
            page_type = "Non Blank"
            prev_page_blank = False

        # Append data to the dictionary
        data["Document ID"].append(document_id)
        data["Page Number"].append(page_num + 1)
        data["Page Type"].append(page_type)
        data["Text Content"].append(text if text.strip() != "" else "...")
        data["Image Content"].append("Yes" if images else "No")
        data["Metadata"].append(str(metadata))

    return pd.DataFrame(data)

# Path to your PDF file
pdf_path = os.path.expanduser("~/Downloads/PDF-training_batch(wpp).pdf")

# Extract information and create DataFrame
df = extract_pdf_info(pdf_path)

# Print the DataFrame in tabular format
print("Example of Tidy waData (Table Form)")
print(df.to_string(index=False))

# Save the DataFrame to a CSV file
csv_output_path = os.path.expanduser("~/Downloads/PDF_extracted_data.csv")
df.to_csv(csv_output_path, index=False)
print(f"Data saved to {csv_output_path}")
