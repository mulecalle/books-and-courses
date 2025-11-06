# Modules out house
from json import load
from pprint import pprint

def read_json(file_path, print=False):

    try:
        with open(file_path) as json_data:
            data = load(json_data)
            json_data.close()
    except:
        return None

    if print:
        pprint(data)

    return data