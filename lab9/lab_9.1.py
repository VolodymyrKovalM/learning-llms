from langchain_huggingface.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20},
)

domain = "laptop"
template = "Craft an innovative name for my upcoming {domain} sales and service"
prompt = PromptTemplate.from_template(template)

formatted_prompt = prompt.format(domain=domain)

chain= prompt | llm

answer = chain.invoke(formatted_prompt)

print(answer)