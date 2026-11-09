def extract_nested_value(obj, keys):
    for key in keys:
        if not isinstance(obj, dict) or key not in obj:
            return None
        obj = obj[key]
    return obj

def process_dictionary_with_config(dictionary, config):
    result = {}

    for attribute, setting in config.items():
        if isinstance(setting, tuple):
            path, processor = setting
            value = extract_nested_value(dictionary, path)

            if value is not None:
                value = processor(value)
        else:
            value = extract_nested_value(dictionary, setting)

        result[attribute] = value

    return result

def process_list_of_dicts_with_config(list_of_dicts, config):
    result = []

    for dictionary in list_of_dicts:
        result.append(process_dictionary_with_config(dictionary, config))

    return result

def create_processor(config, list_processor=False):
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)
        else:
            return process_dictionary_with_config(data, config)

    return processor