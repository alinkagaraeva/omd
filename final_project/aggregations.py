from statistics import mean, median


def count_records(data):
    return len(data)


def mean_value(data, field):
    values = [record[field] for record in data if record.get(field) is not None]
    return mean(values) if values else None


def median_value(data, field):
    values = [record[field] for record in data if record.get(field) is not None]
    return median(values) if values else None


def maximum_value(data, field):
    values = [record[field] for record in data if record.get(field) is not None]
    return max(values) if values else None


def top_n(data, field, n):
    records = [record for record in data if record.get(field) is not None]
    return sorted(records, key=lambda record: record[field], reverse=True)[:n]
