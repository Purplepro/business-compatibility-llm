import json
import os

business_profils_filepath = os.path.join(os.path.dirname(__file__), "../data/business_profiles.json")

def load_business_profiles(filepath: str = business_profils_filepath) -> list[dict]:
    """
    Return a list of business profile dictionaries.
    Each dictionary represents a single business.
    filepath: string path to the json files location
    """

    with open(filepath, "r") as f:
        data = json.load(f)

    return data['businesses']
    ...
