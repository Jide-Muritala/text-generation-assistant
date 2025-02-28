from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Specify the model you want to use, the default is GPT-2
MODEL_NAME = "gpt2"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

def generate_text(prompt, tokenizer, model, max_length=100):
    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    # Generate text using sampling
    output = model.generate(
        input_ids,
        max_length=max_length,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        no_repeat_ngram_size=2
    )
    # Decode and return the generated text
    return tokenizer.decode(output[0], skip_special_tokens=True)

def main():
    print("Welcome to the Interactive Text Generation Assistant!")
    print("Type your prompt below (or type 'exit' to quit).")
    
    tokenizer, model = load_model()
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        response = generate_text(user_input, tokenizer, model)
        print("\nAssistant:", response)

if __name__ == "__main__":
    main()
