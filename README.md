# 📝 Dialogue Summarizer (BART-base fine-tuned on SAMSum)

This project implements a text summarization system for dialogues, built on top of the lightweight BART-base model.  
The model is fine-tuned on the SAMSum dataset to generate concise and meaningful summaries of conversations.  

While the pretrained BART-base model struggles with dialogue summarization (often just copying parts of the input), the fine-tuned version captures the core meaning and produces short, clear summaries.  

---

## 🚀 Project Highlights
- **Model:** `facebook/bart-base` (lightweight, ~140M parameters).  
- **Dataset:** SAMSum (dialogues + human-written summaries).  
- **Frameworks:** Hugging Face Transformers, Datasets, PyTorch, FastAPI.  

**Features:**
- Training script with Hugging Face Trainer.  
- Evaluation using ROUGE metrics.  
- FastAPI inference server with `/predict` endpoint.  
- Comparison of fine-tuned vs pretrained results.  

---

## 📊 Results Comparison

### 🔍 Example 1  

**📝 Input Dialogue**
