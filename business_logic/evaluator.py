#Logic: build + evaluate_business_pairs
import json

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

def build_profile(business: dict) -> str:
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
    Evaluate business compatibilty based on prompt template and business attributes
    business_a: A dict of business attributes(e.g., location, type, certifications).
    business_b: A dict of business attributes(e.g., location, type, certifications).
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