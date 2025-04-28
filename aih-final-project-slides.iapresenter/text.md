# Rejection Sampling for Medical MCQ Generation and Fine-Tuning TinyLlaMA for Layperson QA
	AI in Healthcare
	MSAI Spring 2025
	Chelsea Ramos
Hi, I’m Chelsea Ramos.
Today I’ll share my project on improving layperson medical question answering using rejection sampling and fine-tuning TinyLlaMA.
Reliable medical answers should be easy to access, but general models often miss the mark.
This project hopes to tackles that gap.
---
# Introduction
First, I’ll walk through some quick background, and what my project set out to do.
---
### Background
	- Medical QA: complex, needs accuracy
	- Layperson QA: needs simplicity
	- LLMs: need domain fine-tuning
	- Good data is critical
Medical question answering demands precision and clarity.
For everyday users, answers need to be simple and trustworthy.
Big models like TinyLlaMA aren’t tuned for that by default.
And without good, targeted data, even a fine-tuned model won’t perform well.
---
### Objectives
	- Generate MCQs from MedQuAD
	- Filter with rejection sampling
	- Fine-tune TinyLLaMA
	- Compare to baseline and MedAlpaca
My objectives were to generate multiple-choice questions from MedQuAD,
filter for quality using rejection sampling,
fine-tune TinyLlaMA with supervised learning,
and compare it to both the baseline and MedAlpaca models.
---
# Method
Now I’ll dive into the methods — starting with the dataset and workflow.
---
### MedQuAD Dataset
	- 47K+ layperson medical QA pairs
	- Trusted U.S. health sources
	- Clear, accessible answers
I used the MedQuAD dataset — over 47,000 question-answer pairs built for layperson understanding.
Sources include trusted organizations like National Institutes  of Health and MedlinePlus.
It was a good fit for creating accessible multiple-choice questions.
---
### Workflow
/assets/workflow.png
size: contain
The pipeline was simple:
sample question-answer pairs, generate multiple-choice questions w/ MedAlpaca, filter using rejection sampling, fine-tune TinyLlaMA, and then evaluate.
---
### MCQ Generation
/assets/mcqgen-prompt.png
size: contain
For generation, I sampled about 3,000 question-answer pairs.
Then, I used a custom few-shot prompt with reasoning to guide the MedAlpaca's multiple-choice question generation.
---
### Generated MCQs
/assets/data-train.png
size: contain
	- 511 MCQs finalized
	- 408 train / 103 test (80/20 split)
From 3,000 question-answer pairs, I generated 728 multiple-choice questions.
After review, 511 were finalized — about 400 for training and 100 for testing.
---
# Results
Now, let’s jump into the results.
---
### Loss 
	Small dataset: quick, noisy training
/assets/training.png
size: contain
Since the dataset was small, training finished fast.
The loss curves were a little noisy, but overall showed improvement.
---
### Accuracy
	Finetuning improved accuracy, but gains were modest
/assets/accuracy 1.png
size: contain
Fine-tuning gave a clear accuracy boost over both the baseline TinyLlaMA and MedAlpaca.
The gains weren’t massive, but they were consistent.
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
The train/test sets were balanced, so the evaluation was fair.
Baseline TinyLlaMA was super biased toward one answer choice.
Fine-tuning helped spread the answers more evenly.
MedAlpaca did better than the baseline but often skipped questions entirely.
---
## Future Directions
	- Scale to larger models
	- Improve MCQ generation
	- Extend to open-ended QA
	- Test on broader datasets
If I had more time, I’d fine-tune larger models like LLaMA-2 and evaluate against GPT models.
I’d also look at smarter ways to generate MCQs, not just rejection sampling.
Lastly, I’d also explore open-ended QA and broader evaluation datasets.
---
# Thank You!
Thank you for listening!
