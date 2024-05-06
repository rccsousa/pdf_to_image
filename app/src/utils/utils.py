import fitz
from PIL import Image
import io

def load(document):
    """
    Loads a PDF document using PyMuPDF fitz library.

    Args:
        document (str): Path to the PDF document.

    Raises:
        AssertionError: If the document does not end with the '.pdf' extension.

    Returns:
        fitz.open: A PyMuPDF document object.
    """
        
    assert document.endswith('.pdf'), 'Document must be a PDF.'
    return fitz.open(document)

def get_pages(document):
    """
    Gets the total number of pages in the loaded PDF document.

    Args:
        document (fitz.open): A loaded PyMuPDF document object.

    Returns:
        int: The total number of pages in the document.
    """
    return document.page_count

def load_page(document, page_number):
    """Loads a specific page from the loaded PDF document.

    Args:
        document (fitz.open): A loaded PyMuPDF document object.
        page_number (int): The page number (zero-based indexing).

    Returns:
        fitz.page: The loaded PyMuPDF page object.

    Prints:
        An error message if the page fails to load with the specific reason.
    """
    try: 
        return document.load_page(page_number)
    except ValueError as e:
        print(f'Failed to load {page_number}: {e}')
    
def get_pixel_map(page, dpi):
    """Gets the pixel map of a loaded PyMuPDF page at a specified DPI.

    Args:
        page (fitz.page): A loaded PyMuPDF page object.
        dpi (int): The desired Dots Per Inch resolution.

    Returns:
        bytes: The raw pixel data of the page.

    Prints:
        An error message if getting the pixel map fails with the specific reason.
    """

    try:   
        pixel_map = page.get_pixmap(dpi = dpi)
        return pixel_map.tobytes()
    
    except Exception as e:
        print(f'Failed to get pixel map: {e}. Are you sure you have loaded a page?')
        raise e


def convert(pixel_map, output_file, img_format):
    """Converts the raw pixel map data to an image file.

    Args:
        pixel_map (bytes): The raw pixel data of the page.
        output_file (str): The path to save the converted image file.
        format (str): The desired image format (e.g., PNG, JPEG).

    Raises:
        Exception: If the image format is invalid or an error occurs during conversion.
    """
    try:
        img = Image.open(io.BytesIO(pixel_map))
        img.save(output_file, format = img_format.upper())
    
    except Exception as e:
        print(f'Error converting pixel map to image, invalid format {e}')
        raise e