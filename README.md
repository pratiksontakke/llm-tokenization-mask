# LLM Tokenization & Fill-in-the-Blank Assignment

## Overview
This project explores three popular tokenization algorithms (BPE, WordPiece, SentencePiece) and demonstrates masked language modeling using a 7B open-source language model.

## Files
- `tokenise.py`: Script to tokenize a sentence using BPE (GPT-2), WordPiece (BERT), and SentencePiece (ALBERT).
- `compare.md`: Markdown file comparing the outputs of each tokenization method.
- `predictions.json`: Output of masked language model predictions.
- `README.md`: This file. Instructions and project summary.

## Setup
1. Install Python 3.7+
2. Install dependencies:
   ```
   pip install tokenizers transformers sentencepiece
   ```

## Usage
1. Run the tokenization script:
   ```
   python tokenise.py
   ```
   This will print the tokens, token IDs, and token counts for each method.

2. (Next step) Run the masking and prediction script to generate `predictions.json`.

## Assignment Goals
- Compare how different tokenization algorithms split the same sentence.
- Use a large language model to predict masked tokens in a sentence.
- Analyze and report on the results.

## Sentence Used
```
The cat sat on the mat because it was tired.
```
