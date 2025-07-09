import os
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain_community.llms import HuggingFaceHub
from tools.search_tool import search_products
from tools.Calculator_tool import calculate_total

# Load API key
load_dotenv()
hf_api_key = os.getenv("HF_API_KEY")

# ✅ Use a model that's publicly available and works
llm = HuggingFaceHub(
    repo_id="google/flan-t5-xl",
    model_kwargs={
        "temperature": 0.7,
        "max_length": 512
    },
    huggingfacehub_api_token=hf_api_key
)
# Define tools
tools = [
    Tool(
        name="Product Search Tool",
        func=lambda query: search_products(query),
        description="Search skincare products based on user skin type and concern"
    ),
    Tool(
        name="Cost Calculator",
        func=lambda products: calculate_total(products),
        description="Calculate total cost of selected products"
    )
]

# Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
