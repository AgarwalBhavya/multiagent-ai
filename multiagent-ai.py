import os
import time
from transformers import pipeline, set_seed

# Load local model (GPT-2 small)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)


def research_company(company_name, industry_segment, strategic_focus):
    print("\n🔎 Researching Company...")
    prompt = (f"Provide a short company profile for {company_name} operating in the {industry_segment} industry. "
              f"Focus especially on {strategic_focus}.")

    response = generator(
        prompt,
        max_length=300,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256
    )
    return response[0]['generated_text']


def generate_use_cases(industry_segment, strategic_focus):
    print("\n🧠 Generating Use Cases...")
    prompt = (f"Suggest 5 innovative AI and GenAI use cases for a company in the {industry_segment} industry. "
              f"Focus on {strategic_focus}. List them clearly.")

    response = generator(
        prompt,
        max_length=300,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256
    )
    return response[0]['generated_text']


def collect_dataset_links(industry_segment, strategic_focus):
    print("\n🔗 Suggesting Relevant Datasets...")
    prompt = (f"Suggest 5 real datasets from sources like Kaggle, UCI ML repository, or HuggingFace datasets "
              f"that can help build AI solutions for the {industry_segment} industry focusing on {strategic_focus}. "
              f"Only suggest dataset names, do not give fake links.")

    response = generator(
        prompt,
        max_length=300,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256
    )
    return response[0]['generated_text']


def run_pipeline(company_name, industry_segment, strategic_focus):
    company_profile = research_company(company_name, industry_segment, strategic_focus)
    time.sleep(1)
    use_cases = generate_use_cases(industry_segment, strategic_focus)
    time.sleep(1)
    dataset_suggestions = collect_dataset_links(industry_segment, strategic_focus)
    time.sleep(1)

    return use_cases, dataset_suggestions, company_profile


if __name__ == "__main__":
    # Example Inputs
    company = input("\n🏢 Enter Company Name: ")
    industry = input("🏭 Enter Industry Segment: ")
    focus = input("🎯 Enter Strategic Focus (e.g., 'Customer Experience', 'Automation', etc.): ")

    print("\n🚀 Running Multi-Agent System...\n")
    use_cases, dataset_suggestions, company_profile = run_pipeline(company, industry, focus)

    print("\n\n===== 📄 Company Profile =====\n")
    print(company_profile.strip())

    print("\n\n===== 💡 AI/GenAI Use Cases =====\n")
    print(use_cases.strip())

    print("\n\n===== 📚 Dataset Suggestions =====\n")
    print(dataset_suggestions.strip())

    print("\n✅ Done!\n")
