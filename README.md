# aih-final-project

## Notes

1. MedQuAD
    - Type: Layperson medical questions and answers
    - Size: ~47,000 QA pairs
    - Source: NIH, MedlinePlus, National Cancer Institute, etc.
    - Best For: Patient education, general health QA
    - Link: https://github.com/abachaa/MedQuAD


    Format a batch evaluation script using GPT-4 on these QA pairs?

    Build a Streamlit interface to explore the dataset interactively?

    Would you like a quick notebook to load and evaluate a few PubMedQA samples using GPT-4?


### Project Flow
Convert MedQuAD to Multiple-Choice Format
→ Use GPT-4 to generate distractors
→ Store in SFT or MCQ format
Fine-Tune a Hugging Face LLM
→ e.g., Mistral-7B, Phi-2, or TinyLLaMA using LoRA
Evaluate on Held-Out MedQuAD MCQs
→ Accuracy (% correct)
→ Optional: Factuality or hallucination review


Plan: Two-Stage Fine-Tuning

Stage 1 — MCQ Fine-Tuning (Now)
Fine-tune TinyLLaMA on MedQuAD-derived MCQs
Objective: Train the model to select correct answers and learn core medical associations
Format: Classification or instruction-based MCQs
Stage 2 — Open-Ended QA Fine-Tuning (Future Work)
Fine-tune the same model further using open-ended question–answer pairs
Objective: Enable the model to generate full-text, readable explanations
Method: Continue training via LoRA or SFT using instruction-style datasets

“This project focuses on fine-tuning a large language model (TinyLLaMA) on MedQuAD-derived multiple-choice questions to teach medical domain understanding.
As future work, we propose a second-stage fine-tuning using open-ended QA examples from MedQuAD to enable generative medical explanations. This staged approach allows the model to first learn content grounding through structured formats (MCQs) before expanding into more flexible generative reasoning.”