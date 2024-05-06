import auxiliary_funcs

def pdf2img(document_file, dpi = 600, format = 'PNG', pages = 'ALL'):
    """The main function that drives the PDF to image conversion process.

    Args:
        document_file (str): Path to the PDF document.
        dpi (int, optional): The desired Dots Per Inch resolution (default 600).
        format (str, optional): The desired image format (default 'PNG').
        pages (str or list, optional): Specifies which pages to convert. 
            'ALL' for all pages, or a list of page numbers (default 'ALL').

    Prints:
        Error messages if issues occur during loading or conversion.
    """
    
    pdf = auxiliary_funcs.load(document_file)

    if pages.upper() == 'ALL':
        pages = list(
            range(auxiliary_funcs.get_pages(pdf)))

    elif not isinstance(pages, list):
        pages = [pages]
    
    for page_number in pages:
        page = auxiliary_funcs.load_page(pdf, page_number)
        pixel_map = auxiliary_funcs.get_pixel_map(page, dpi)
        
        auxiliary_funcs.convert(pixel_map, f'{page}.{format}', format.upper())

