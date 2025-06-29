#Logic: build + evaluate_business_pairs
import json

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

def build_profile(business: dict) -> str:
    """
    Constructs a natural language description of a business profile from its attributes.

    Parameters:
        business (dict): A dictionary containing business attributes such as name, type, location, 
                         capacity, transport, demand, certifications, values, and optional notes.

    Returns:
        str: A formatted string summarizing the business's key attributes, suitable for injection 
             into an LLM prompt.
    
    Example:
        Input:
        {
            "name": "Ghana Seafood Co.",
            "type": "Supplier",
            "location": "Coastal Ghana",
            "capacity": "15 tons/month",
            "transport": "5 refrigerated trucks",
            "certifications": ["HACCP", "Certified Organic"]
        }

        Output:
        "Ghana Seafood Co. is a Supplier located in Coastal Ghana. Monthly capacity: 15 tons/month. 
         Transport assets: 5 refrigerated trucks. Certifications HACCP,Certified Organic."
    """

    lines = [
        f"{business['name']} is a {business['type']} located in {business['location']}.",
    ]

    if "capacity" in business:
        lines.append(f"Monthly capacity: {business['capacity']}.")
    if "transport" in business:
        lines.append(f"Transport assets: {business['transport']}.")
    if "demand" in business:
        lines.append(f"Demand requirement: {business['demand']}.")
    if "certifications" in business:
        lines.append(f"Certifications {','.join(business['certifications'])}.")
    if "values" in business:
        lines.append(f"Company values: {', '.join(business['values'])}.")
    if "notes" in business:
        lines.append(business["notes"])

    return " ".join(lines)



def evaluate_business_pairs(business_a: dict, business_b: dict) -> str:
    """
    Evaluates the compatibility between two businesses using a language model and a structured prompt template.

    This function builds natural language profiles for two businesses using their attributes,
    injects them into a predefined prompt template, and uses a local LLM to generate a
    compatibility assessment.

    Parameters:
        business_a (dict): A dictionary containing attributes of the first business (e.g., name, type,
                           location, capacity, certifications, etc.).
        business_b (dict): A dictionary containing attributes of the second business.

    Returns:
        str: A natural language response from the LLM describing the compatibility verdict
             and the reasoning behind it.
    
    Example:
        evaluate_business_pairs(business_a, business_b)
        "**Verdict:** Compatible\n\n**Reasoning:** Both businesses share matching certifications, have
        complementary supply and demand profiles, and operate within the same region."
    """
    with open("/Users/sevios/ai_projects/business_comp_ai_agent/prompts/compatibility_prompt.text", "r") as f:
        prompt_template_str = f.read()

    prompt = PromptTemplate.from_template(prompt_template_str)
    llm = Ollama(model="gemma:2b")  # adjust if you’re using another model



    chain = LLMChain(llm=llm, prompt=prompt)
    profile_a = build_profile(business_a)
    profile_b = build_profile(business_b)

    response = chain.run({
        "business_a": profile_a,
        "business_b": profile_b
    })

    return response
