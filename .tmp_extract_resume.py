from pypdf import PdfReader
reader = PdfReader(r"assets/resume.pdf")
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    print(f"\n--- PAGE {i} ---\n")
    print(text)
