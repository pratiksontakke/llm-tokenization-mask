from transformers import GPT2Tokenizer, BertTokenizer, AlbertTokenizer

def tokenize_bpe(text):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.encode(text)
    return {
        'method': 'BPE (GPT-2)',
        'tokens': tokens,
        'token_ids': token_ids,
        'token_count': len(tokens)
    }

def tokenize_wordpiece(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.encode(text)
    return {
        'method': 'WordPiece (BERT)',
        'tokens': tokens,
        'token_ids': token_ids,
        'token_count': len(tokens)
    }

def tokenize_sentencepiece(text):
    tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.encode(text)
    return {
        'method': 'SentencePiece (ALBERT)',
        'tokens': tokens,
        'token_ids': token_ids,
        'token_count': len(tokens)
    }

if __name__ == "__main__":
    sentence = "The cat sat on the mat because it was tired."
    results = [
        tokenize_bpe(sentence),
        tokenize_wordpiece(sentence),
        tokenize_sentencepiece(sentence)
    ]
    for result in results:
        print(f"\n--- {result['method']} ---")
        print("Tokens:", result['tokens'])
        print("Token IDs:", result['token_ids'])
        print("Token count:", result['token_count'])