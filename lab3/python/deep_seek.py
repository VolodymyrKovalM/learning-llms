import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model_name = "../../models/deepseek-llm-7b-chat"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")

model.generation_config = GenerationConfig.from_pretrained(model_name)
model.generation_config.pad_token_id = model.generation_config.eos_token_id

messages = [
    {
        "role": "user",
        "content": """
            You are a language learning assistant.
            User will first choose the language that he would like to learn,
            and you will help with vocabulary, pronunciation, grammar, and conversation.
            Also, you need to offer personalized guidance and exercises to enhance language proficiency.
        """
    }
]

def generateAnswer(message):
    messages.append({
        "role": "user",
        "content": message
    })

    # Convert messages to input tensor
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

    # Generate response
    outputs = model.generate(input_ids, max_new_tokens=100)

    # Decode and print response
    result = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=True)

    messages.append({
        "role": "assistant",
        "content": result
    })

    print(result)

    return result

