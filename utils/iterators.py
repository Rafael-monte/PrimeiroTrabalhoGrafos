
def map_and_list(fn, collection: list) -> list:
    map_result = map(fn, collection)
    return list(map_result)
