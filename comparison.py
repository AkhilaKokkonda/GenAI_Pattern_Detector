def compare_models(pattern, confidence):

    gpt_score = max(confidence - 5, 80)
    claude_score = max(confidence - 7, 78)
    gemini_score = confidence

    return [
        {
            "Model": "GPT-4",
            "Pattern": pattern,
            "Score": gpt_score
        },
        {
            "Model": "Claude",
            "Pattern": pattern,
            "Score": claude_score
        },
        {
            "Model": "Gemini",
            "Pattern": pattern,
            "Score": gemini_score
        }
    ]