# tiny-llm

A small (135M-parameter) instruction-tuned language model that runs on a laptop CPU.
The weights are stored in this repo with Git LFS.

The model is **SmolLM2-135M-Instruct** by Hugging Face
([source](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct)), redistributed
unmodified under the Apache 2.0 license (see `LICENSE`).

## Contents

| Path | What it is |
|---|---|
| `model/model.safetensors` | Weights (~270 MB, Git LFS) |
| `model/*.json`, `merges.txt` | Config and tokenizer |
| `chat.py` | Command-line chat script |

## Quick start

```bash
git lfs install
git clone https://github.com/chara129/tiny-llm.git
cd tiny-llm
pip install -r requirements.txt
python chat.py "Explain what an LLM is in two sentences."
```

Run `python chat.py` with no arguments for an interactive chat.

## Notes

- Model size: 135M parameters, 2,048-token context, English only.
- It is a small model: answers can be wrong or repetitive, so don't rely on it for facts.
