from transformers import pipeline

# Load a sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Analyze sentiment of a sample text
# result = classifier("I kind of love and hate using Hugging Face Transformers!")
# print(result)

import psutil

process = psutil.Process()
mem_info = process.memory_info()

print(f"Memory Usage: {mem_info.rss / 1024 ** 2:.2f} MB")  # Memory usage in MB

# Analyze sentiment of a sample text
result = classifier("I love using Hugging Face Transformers!")
print(result)