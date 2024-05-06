"""
Simple module to convert PDF documents to images.
"""

from .utils import utils

def pdf2img(document_file, dpi = 600, img_format = 'PNG', pages = 0):
    """
    # TODO add input to select pages
    # TODO add input to prompt for document
    
    The main function that drives the PDF to image conversion process.

    Args:
        document_file (str): Path to the PDF document.
        dpi (int, optional): The desired Dots Per Inch resolution (default 600).
        format (str, optional): The desired image format (default 'PNG').
        pages (str or list, optional): Specifies which pages to convert. 
            'ALL' for all pages, or a list of page numbers (default 'ALL').

    Prints:
        Error messages if issues occur during loading or conversion.
    """
    pdf = utils.load(document_file)

    if isinstance(pages, str) and pages.upper() == 'ALL':
        pages = list(
            range(utils.get_pages(pdf)))

    elif not isinstance(pages, list):
        pages = [pages]
    
    for page_number in pages:
        page = utils.load_page(pdf, page_number)
        pixel_map = utils.get_pixel_map(page, dpi)
        
        utils.convert(pixel_map, f'{page}.{img_format}', img_format.upper())

