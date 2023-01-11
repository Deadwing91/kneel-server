STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },

    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },

    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]

def get_all_styles():
    """_summary_

    Returns:
        _type_: _description_
    """
    return STYLES

def get_single_style(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_style = None
    for style in STYLES:
        if style["id"] == id:
            requested_style = style
    return requested_style
    