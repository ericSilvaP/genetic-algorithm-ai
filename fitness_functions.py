def aluffi_pentini(ind):
    x, y = ind
    return format_decimals(0.25 * x**4 - 0.5 * x**2 + 0.1 * x + 0.5 * y**2)


def three_camel_back(ind):
    x, y = ind
    return format_decimals(2 * x**2 - 1.05 * x**4 + (x**6) / 6 + x * y + y**2)


def format_decimals(x):
    return float(f"{x:.4f}")
