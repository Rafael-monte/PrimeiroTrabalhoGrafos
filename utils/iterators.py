
def map_and_list(fn, collection: list) -> list:
    map_result = map(fn, collection)
    return list(map_result)


def filter_map_and_list(filter_fn, map_fn, collection):
    filtered = list(filter(filter_fn, collection))
    mapped = list(map(map_fn, filtered))
    return mapped
