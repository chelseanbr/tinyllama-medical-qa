# Rejection Sampling for Medical MCQ Generation and Fine-Tuning TinyLlaMA for Layperson QA
	AI in Healthcare
	MSAI Spring 2025
	Chelsea Ramos
Hi, I’m Chelsea Ramos.
Today, I’ll share my project on improving layperson medical question answering using rejection sampling and fine-tuning TinyLLaMA.
This is important because reliable medical information should be accessible, but general models often struggle without targeted fine-tuning.
---
# Introduction
First, let’s start with some background and objectives.
---
### Background
	- Medical QA: complexity and accuracy
	- Layperson QA: simplicity and reliability
	- LLMs: need domain fine-tuning
	- Data quality: key to performance
Medical QA is challenging — it needs technical accuracy and clarity.
For laypeople, answers have to be simple and reliable.
Most language models aren't tuned for this domain, so quality fine-tuning becomes critical.
Based on these challenges, I set a few key goals for my project.
---
### Objectives
	- MCQ generation from MedQuAD
	- Rejection sampling for quality
	- Fine-tune TinyLLaMA (supervised)
	- Evaluate vs. baseline and MedAlpaca
My objective were to generate MCQs from the MedQuAD dataset
use rejection sampling to filter for quality,
fine-tune TinyLLaMA using supervised learning,
and compare performance against a baseline TinyLLaMA and the MedAlpaca model
---
# Method
Now I'll walk through the method.
---
### MedQuAD Dataset
	- 47K+ layperson medical QA pairs
	- Sourced from trusted U.S. health organizations
	- Designed for accuracy and accessibility
I used MedQuAD, a high-quality dataset with over 47,000 layperson-focused QA pairs,
sourced from trusted U.S. health organizations like NIH and MedlinePlus.
With this dataset, I generated the MCQs needed for training.
---
### Workflow
/assets/workflow.png
size: contain
Here's the overall workflow: sample data, 
generate MCQs, 
apply rejection sampling, 
fine-tune TinyLLaMA, 
and evaluate performance against other models.
Now, let's look at how the MCQs were generated.
---
### MCQ Generation Prompt
/assets/mcqgen-prompt.png
size: contain
I sampled 3,000 QA pairs from MedQuAD.
Then, using a custom prompt and rejection sampling, I generated about 728 high-quality MCQs.
After filtering, I finalized the training data.
---
### Generated MCQs
/assets/data-sampled.png
size: contain
	- Sampled 3K question-answer pairs
/assets/data-generated.png
size: contain
	- Generated 728 MCQs via Rejection Sampling
I sampled 3,000 QA pairs from MedQuAD.
Then, using a custom prompt and rejection sampling, I generated about 728 high-quality MCQs.
After filtering, I finalized the training data.
---
### Final Data
/assets/data-train.png
size: contain
	- Finalized 511 total MCQs -> 408 train, 103 test (80/20 split)
After manual review, I finalized 511 MCQs —
splitting 80% for training and 20% for testing.
Now let's see how the model performed.
---
# Results
---
### Loss 
	Small dataset → fewer epochs, noisier loss curves
/assets/training.png
size: contain
Because the dataset was small, training finished in just a few epochs.
The loss curves are noisy, but still show some learning.
Let’s see how that translated to accuracy.
---
### Accuracy
	Finetuning improved accuracy, but gains were modest
/assets/accuracy 1.png
size: contain
Fine-tuning improved TinyLLaMA’s accuracy over the baseline and MedAlpaca.
The gains were modest, but clear given the small training set.
Next, I’ll show how the model handled answer distributions.
---
### Answer Distributions
/assets/train-test-dist.png
size: contain
/assets/baseline-tinyllama-dist.png
size: contain
/assets/finetuned-tinyllama-dist.png
size: contain
/assets/medalpaca-dist.png
size: contain
The train and test sets were balanced, so evaluation was fair.
The baseline TinyLLaMA was heavily biased toward one option.
After fine-tuning, TinyLLaMA had a more even spread, but still skewed.
MedAlpaca improved slightly but produced many missing answers.
Based on these results, there are several directions for future work.
---
## Future Directions
	- Scale to larger models
	- Improve MCQ generation
	- Extend to open-ended QA
	- Broaden evaluation datasets
With more time, I would scale fine-tuning to larger models like LLaMA-2 and evaluating against GPT-based models.
I'd also work on improving MCQ generation beyond rejection sampling.
Future work could extend to open-ended medical QA, not just multiple-choice,
and evaluate performance on broader datasets to strengthen generalization.
---
# Thank You!
Thank you for listening!
