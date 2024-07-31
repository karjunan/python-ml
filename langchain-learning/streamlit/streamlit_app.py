import streamlit as st
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Load LLaMA model and tokenizer
model_name = "mmeta-llama/Meta-Llama-3.1-8B-Instruct"  # You can choose another version if available
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Streamlit app interface
st.title("LLaMA Text Generator")
st.write("Generate text using the LLaMA model.")

# User input
prompt = st.text_area("Enter your prompt here:", "Once upon a time")

# Button to generate text
if st.button("Generate Text"):
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    # Generate text
    outputs = model.generate(inputs.input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
    # Decode generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Display generated text
    st.subheader("Generated Text:")
    st.write(generated_text)