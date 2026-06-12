from docling.document_converter import DocumentConverter
"""When I want to optimise go to: https://docling-project.github.io/docling/getting_started/rtx/
see also for example: https://github.com/AI-Engineer-Skool/booktutor-ai/blob/main/booktutor.py#L26"""
#from langchain_text_splitters import RecursiveCharacterTextSplitter



def read_pdf(pdf_path: str):
    converter = DocumentConverter()
    doc = converter.convert(pdf_path).document
    with open('example.md', 'w', encoding="utf-8") as f:
        f.write(doc.export_to_markdown())
    #print(doc.export_to_markdown()) 

read_pdf("C:/Users/Quinte/OneDrive/Desktop/Lichemaster campaign/Vengeance.pdf")