import jq

def all(program, value):
    return jq.all(program, value)

def first(program, value, default=None):
    res = jq.all(program, value)
    return res[0] if res else default

def one(program, value):
    res = jq.all(program, value)
    if len(res) != 1:
        raise ValueError(f"Expected exactly 1 element, got {len(res)}")
    return res[0]
