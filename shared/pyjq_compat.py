import jq

def all(program, value):
    try:
        return jq.all(program, value)
    except ValueError as e:
        if "Cannot iterate over null" in str(e):
            return []
        raise

def first(program, value, default=None):
    try:
        res = jq.all(program, value)
        return res[0] if res else default
    except ValueError as e:
        if "Cannot iterate over null" in str(e):
            return default
        raise

def one(program, value):
    try:
        res = jq.all(program, value)
        if len(res) != 1:
            raise ValueError(f"Expected exactly 1 element, got {len(res)}")
        return res[0]
    except ValueError as e:
        if "Cannot iterate over null" in str(e):
            raise ValueError("Expected exactly 1 element, got 0")
        raise
