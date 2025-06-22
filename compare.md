# Tokenization Comparison Report

## Sentence
```
The cat sat on the mat because it was tired.
```

## 1. BPE (GPT-2)
- **Tokens:** ['The', 'Ġcat', 'Ġsat', 'Ġon', 'Ġthe', 'Ġmat', 'Ġbecause', 'Ġit', 'Ġwas', 'Ġtired', '.']
- **Token IDs:** [464, 3797, 3332, 319, 262, 2603, 780, 340, 373, 10032, 13]
- **Token Count:** 11

## 2. WordPiece (BERT)
- **Tokens:** ['the', 'cat', 'sat', 'on', 'the', 'mat', 'because', 'it', 'was', 'tired', '.']
- **Token IDs:** [101, 1996, 4937, 2938, 2006, 1996, 13523, 2138, 2009, 2001, 5458, 1012, 102]
- **Token Count:** 11

## 3. SentencePiece (ALBERT)
- **Tokens:** ['▁the', '▁cat', '▁sat', '▁on', '▁the', '▁mat', '▁because', '▁it', '▁was', '▁tired', '.']
- **Token IDs:** [2, 14, 2008, 847, 27, 14, 4277, 185, 32, 23, 4117, 9, 3]
- **Token Count:** 11

---

## Why Do the Splits Differ?
Each tokenization algorithm uses a different approach to splitting text:
- **BPE (GPT-2):** Merges frequent pairs of bytes/subwords, resulting in variable-length subword tokens. It is efficient for handling rare words and open vocabulary.
- **WordPiece (BERT):** Similar to BPE but uses a different merge strategy, often resulting in more granular subword splits for rare words.
- **SentencePiece (ALBERT):** Uses a probabilistic model (Unigram LM) and can split text into subwords or even single characters, making it flexible for languages without spaces.

These differences affect how the sentence is broken down, the number of tokens, and how unknown words are handled. 

## BERT Mask Predictions

### Original Sentence with Masks
```
The cat sat on the [MASK] because it was [MASK].
```

### Top Predictions

#### First [MASK] (what the cat sat on):
1. floor (25.3% confidence)
2. couch (8.7% confidence)
3. bed (8.7% confidence)
4. ground (6.7% confidence)
5. sofa (4.3% confidence)

**Analysis:** BERT's predictions are highly plausible for where a cat might sit. The model shows strong preference for flat surfaces (floor, ground) and furniture (couch, bed, sofa) that cats commonly choose as resting places. The high confidence for "floor" (25.3%) suggests this is the most typical location in BERT's training data.

#### Observations:
- All predictions are nouns representing surfaces or furniture
- All predictions make semantic sense in the context
- The confidence scores drop significantly after the first prediction
- The predictions show both common (floor) and specific (sofa) options

This demonstrates BERT's ability to:
1. Understand context (what objects a cat can sit on)
2. Maintain grammatical correctness (all predictions fit the sentence structure)
3. Provide semantically meaningful alternatives
4. Assign reasonable confidence scores based on likelihood 