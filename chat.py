"""Chat with the bundled SmolLM2-135M-Instruct model.

Usage:
    pip install -r requirements.txt
    python chat.py                       # interactive chat
    python chat.py "What is gravity?"    # single prompt
"""
import sys
from pathlib import Path

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_DIR = Path(__file__).parent / "model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)


def reply(history):
    text = tokenizer.apply_chat_template(history, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=256, temperature=0.2, top_p=0.9, do_sample=True)
    return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()


if len(sys.argv) > 1:
    print(reply([{"role": "user", "content": " ".join(sys.argv[1:])}]))
else:
    history = []
    print("tiny-llm chat (type 'exit' to quit)")
    while (msg := input("you> ").strip()).lower() not in {"exit", "quit"}:
        history.append({"role": "user", "content": msg})
        answer = reply(history)
        history.append({"role": "assistant", "content": answer})
        print("bot>", answer)
