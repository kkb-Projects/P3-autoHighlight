import pdfplumber

pdf_name = "pdf/input/1.pdf"
with pdfplumber.open(pdf_name) as pdf:
    for page in pdf.pages:
        page_txt = page.extract_text()
        # 获取文本，直接得到字符串，包括了换行符【与PDF上的换行位置一致，而不是实际的“段落”】
        print(page_txt)

        
