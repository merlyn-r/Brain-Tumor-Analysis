#!/usr/bin/env python3
"""
Test script to check LLM loading
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import transformers
    import torch
    print("✓ Packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    print("✓ Transformers classes imported")
except ImportError as e:
    print(f"✗ Transformers import error: {e}")
    sys.exit(1)

try:
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2", timeout=30)
    print("✓ Tokenizer loaded")

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2", timeout=30)
    print("✓ Model loaded")

    # Test generation
    inputs = tokenizer("Hello, I am", return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=10, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"✓ Generation test successful: '{generated_text}'")

except Exception as e:
    print(f"✗ Model loading error: {e}")
    sys.exit(1)

print("✓ All tests passed!")