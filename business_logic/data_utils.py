import json

def load_business_profiles(filepath: str = "business-compatibility-llm/data/business_profiles.json") -> list[dict]:
    """
    Return a list of business profile dictionaries.
    Each dictionary represents a single business.
    filepath: string path to the json files location
    """

    with open(filepath, "r") as f:
        data = json.load(f)

    return data['businesses']
    ...
