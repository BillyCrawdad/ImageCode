import fitz  # PyMuPDF
from PIL import Image

def pdf_to_png(pdf_path, page_number, output_path):
    pdf_document = fitz.open(pdf_path)
    pdf_page = pdf_document[page_number]

    pix = pdf_page.get_pixmap()

    # Convert Pixmap to Pillow Image
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the Pillow Image as PNG
    image.save(output_path, "PNG")

    pdf_document.close()

# Example usage
if __name__ == "__main__":
    pdf_to_png("ComicArtPanel.pdf", 0, "ComicArtPanel.png")
