
def key_params(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
