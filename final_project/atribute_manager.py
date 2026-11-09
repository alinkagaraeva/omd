def add_attribute(data, attribute, value_function):
    return [
        {**record, attribute: value_function(record)}
        for record in data
    ]
