SIZES = [
    {
        "id": 1,
        "carets": 0.5,
        "price": 405
    },

    {
        "id": 2,
        "carets": 0.75,
        "price": 782
    },

    {
        "id": 3,
        "carets": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1997
    },

    {
        "id": 5,
        "carets": 2,
        "price": 3638 }
]

def get_all_sizes():
    """_summary_

    Returns:
        _type_: _description_
    """
    return SIZES

def get_single_size(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_size = None
    for size in SIZES:
        if size["id"] == id:
            requested_size = size
    return requested_size
    