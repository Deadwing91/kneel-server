ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
    }
]

def get_all_orders():
    """_summary_

    Returns:
        _type_: _description_
    """
    return ORDERS

def get_single_order(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order

def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break

def create_order(order):
    """_summary_

    Args:
        location (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)
