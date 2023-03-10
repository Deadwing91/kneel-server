METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },

    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },

    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },

    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },

    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241.0
    }
]

def get_all_metals():
    """_summary_

    Returns:
        _type_: _description_
    """
    return METALS

def get_single_metal(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Variable to hold the found metal, if it exists
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal
    