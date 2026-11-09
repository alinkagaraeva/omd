from collections import Counter


def filter_records(data, condition):
    return [record for record in data if condition(record)]


def group_by_attributes(data, attributes):
    groups = {}
    for record in data:
        key = tuple(record.get(attribute) for attribute in attributes)
        groups.setdefault(key, []).append(record)
    return groups


def aggregate_groups(groups, aggregation):
    return {key: aggregation(records) for key, records in groups.items()}


def count_missing_values(data, fields):
    return {
        field: sum(record.get(field) is None for record in data)
        for field in fields
    }


def missing_value_shares(data, fields):
    counts = count_missing_values(data, fields)
    return {
        field: count / len(data) if data else None
        for field, count in counts.items()
    }


def duplicate_values(data, field):
    counts = Counter(record[field] for record in data)
    return {value: count for value, count in counts.items() if count > 1}


def find_integer_gaps(data, field):
    values = sorted({record[field] for record in data})
    return [
        (left, right)
        for left, right in zip(values, values[1:])
        if right - left > 1
    ]


def unique_records(data, attributes):
    result = []
    seen = set()
    for record in data:
        key = tuple(record.get(attribute) for attribute in attributes)
        if key not in seen:
            seen.add(key)
            result.append(record)
    return result
