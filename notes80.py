# small utilities, no deps

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]
