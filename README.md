Multi-Agent AI System for AI/GenAI Use Case Generation
This project implements a Multi-Agent AI Architecture that automates the process of researching a company, generating tailored AI/GenAI use cases, and finding relevant datasets and resources.
It is designed to assist organizations in identifying strategic AI opportunities based on their industry and business focus.

Project Architecture
Input: Company Name, Industry, Strategic Focus
        ↓
Company Research Agent
- Gathers company and industry details
        ↓
Use Case Generation Agent
- Creates AI/GenAI use cases relevant to the company
        ↓
Dataset/Asset Collection Agent
- Finds datasets, APIs, and resources supporting the use cases
        ↓
Output: Final Report
- Company profile
- Generated use cases
- Dataset/resource links

 How It Works
Input: The user provides:
Company Name
Industry Segment
Strategic Focus Areas
Company Research Agent:
Scrapes or queries general company and industry information.
Use Case Generation Agent:
Uses a locally running LLM (like Huggingface model gpt2 or better) to generate innovative AI/GenAI use cases.
No external API keys are needed.
Dataset/Asset Collection Agent:
Suggests general datasets or public resources related to the use cases.
Output:
A compiled report with insights, use cases, and dataset links.

Setup Instructions
1.Clone the repository:
git clone https://github.com/AgarwalBhavya/multiagent-ai.git
cd multiagent-ai

2.Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Run the application:
python multiagent-ai.py


Dependencies:
Python 3.8+
Huggingface Transformers (transformers)
Torch (torch)
BeautifulSoup (beautifulsoup4)
Requests (requests)

Example Output:
Example of generated content:
Company Profile: Tesla - Electric Vehicles & AI Innovations
Use Cases: Predictive maintenance AI, Customer personalization with GenAI, Autonomous decision-making models
Datasets/Resources: Links to open datasets, APIs, and research papers

Highlights:
No Paid API Key Needed (uses open-source LLMs)
Customizable and Extendable
Lightweight and Fast
Ready for Deployment and Further Expansion
