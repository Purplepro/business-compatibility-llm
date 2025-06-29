import json

def load_business_profiles(filepath: str = "data/business_profiles.json") -> list[dict]:
    """
    Loads business profile data from a JSON file and returns it as a list of dictionaries.

    Each dictionary in the returned list contains the structured attributes of a single business,
    such as name, type, location, capacity, transport methods, certifications, and more.

    Parameters:
        filepath (str): Path to the JSON file containing the business profile data. Defaults to
                        "business_comp_ai_agent/data/business_profiles.json".

    Returns:
        list[dict]: A list of business profiles, where each profile is represented as a dictionary.

    Raises:
        FileNotFoundError: If the specified JSON file does not exist.
        json.JSONDecodeError: If the file is not properly formatted JSON.

    Example:
        profiles = load_business_profiles()
        profiles[0]["name"]
        'Ghana Seafood Co.'
    """

    with open(filepath, "r") as f:
        data = json.load(f)

    return data['businesses']
