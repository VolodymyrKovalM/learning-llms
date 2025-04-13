from llama_cpp import Llama
import os

model_path = '../../models/llama-2-7b-chat.Q4_K_M.gguf'
print(os.path.exists(model_path))
llama=Llama(model_path=model_path)

def generate_output(prompt, max_tokens, temperature, top_p):
    output= llama(prompt, temperature=0.75,
    max_tokens=2000,
    top_p=1)
    return output['choices'][0]['text']
