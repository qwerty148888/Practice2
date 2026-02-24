import json
source = json.loads(input())
patch = json.loads(input())
def apply_patch(source, patch):
    for key in patch:
        if patch[key] is None:
            if key in source:
                del source[key]
        elif key in source and isinstance(source[key], dict) and isinstance(patch[key], dict):
            source[key] = apply_patch(source[key], patch[key])
        else :
            source[key] = patch[key]
    return source
result = apply_patch(source, patch)
print(json.dumps(result, separators=(",", ":"), sort_keys = True))