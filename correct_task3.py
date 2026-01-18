def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        if v is None:
            continue
        try:
            num = float(v)
            total += num
            count += 1
        except (TypeError, ValueError):
            continue  # Skip items that cannot be converted to float

    if count == 0:
        return 0

    return total / count