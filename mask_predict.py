from transformers import pipeline
import json

# Use a model that supports fill-mask (e.g., BERT)
model_name = "bert-base-uncased"
fill_mask = pipeline("fill-mask", model=model_name)

# Original sentence with two masks
original_sentence = "The cat sat on the [MASK] because it was [MASK]."

# Initialize output dictionary
output = {
    "blank_1": [],
    "blank_2": []
}

try:
    # Get predictions for the first mask
    first_mask_predictions = fill_mask(original_sentence)
    
    # Process top 3 predictions for the first mask
    for first_pred in first_mask_predictions[:3]:
        # Get prediction for first mask
        first_token = first_pred['token_str']
        first_score = float(first_pred['score'])
        
        # Create sentence with first prediction filled in
        intermediate_sentence = original_sentence.replace("[MASK]", first_token, 1)
        
        # Get predictions for the second mask
        second_mask_predictions = fill_mask(intermediate_sentence)
        
        # Add first mask prediction to output
        output["blank_1"].append({
            "prediction": first_token,
            "score": first_score,
            "comment": "Plausible" if first_score > 0.1 else "Less likely"
        })
        
        # Get the top prediction for the second mask
        if second_mask_predictions:
            second_pred = second_mask_predictions[0]
            second_token = second_pred['token_str']
            second_score = float(second_pred['score'])
            
            # Create full sentence with both predictions
            full_sentence = intermediate_sentence.replace("[MASK]", second_token)
            
            # Add second mask prediction to output
            output["blank_2"].append({
                "prediction": second_token,
                "score": second_score,
                "comment": "Plausible" if second_score > 0.1 else "Less likely",
                "full_sentence": full_sentence
            })

    # Save predictions to JSON file
    with open("predictions.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Print results in a readable format
    print("\nPredictions for masked tokens:")
    print("-" * 50)
    for i in range(len(output["blank_1"])):
        print(f"\nOption {i+1}:")
        print(f"First mask:  '{output['blank_1'][i]['prediction']}' (score: {output['blank_1'][i]['score']:.3f})")
        if i < len(output["blank_2"]):
            print(f"Second mask: '{output['blank_2'][i]['prediction']}' (score: {output['blank_2'][i]['score']:.3f})")
            print(f"Full sentence: {output['blank_2'][i]['full_sentence']}")
            print(f"Assessment: {output['blank_1'][i]['comment']} (first mask), {output['blank_2'][i]['comment']} (second mask)")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    # Print the actual structure of the predictions for debugging
    if 'first_mask_predictions' in locals() and len(first_mask_predictions) > 0:
        print("\nFirst mask prediction structure:")
        print(first_mask_predictions[0]) 