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
Ola: Hello Kate, sorry for not keeping in touch properly. As expected, we have hardly any connectivity here in Cuba. But we're doing fine and enjoying our trip. How are the things at home?
Kate: At long last! Started to worry. Nothing new happening, if you disregard all that Xmas craze. Momo has recovered from her injury and frolicking again.
Kate: <file_photo>
Kate: Good old Momo! Yes, it is your scarf!
Ola: NO!!! It's one of my favorites! The one from Laos!
Kate: Too late. Momo thinks it belongs to her now. Get yourself a new one. They surely have nice ones there.
Ola: Not at all. Only cheapish cotton blouses with horrible multi-coloured embroidery or some equally horrible crochetted tops. No shawls or scarfs.
Ola: <file_photo>
Kate: Wait a sec!
Kate: <file_photo>
Kate: Isn't it similar?! Mum would probably like it. Why don't you?
Ola: Not a bad idea. But the quality is usually crappy.
Kate: And if you go to some boutique shop or something? Not at a market as in your pics?
Ola: I might try and find some. Would you like one too?
Kate: Not really. And Mum would prefer to be the only one with an authentic Cuban blouse :))
Ola: OK I'll have a look. Greets to everyone at home pls.
Kate: Take care!

csharp
Copy code

**🤖 Pretrained BART-base Output**
(Often copies large portions of the dialogue without real summarization.)
Ola: Hello Kate, sorry for not keeping in touch properly. As expected, we have hardly any connectivity here in Cuba. But we're doing fine and enjoying our trip. How are the things at home? Kate: At long last! Started to worry. Nothing new happening, if you disregard all that Xmas craze. Momo has recovered from her injury and frolicking again. Kate: <file_photo> Kate: Good old Momo! Yes, it is your scarf! Ola: NO!!! It's one of my favorites! The one from Laos! Kate: Too late. Get yourself a new one. They surely have nice ones there. Ola and Momo: Not at all. Only cheapish cotton blouses with horrible multi-coloured embroidery or some equally horrible crochetted tops. No shawls or scarfs. Go and get yourself a better one, Kate: Why don't you go to some boutique shop and see if they have a nice one? Ola & Kate: I don't think so. I think you should try and find one at a boutique shop. Not at a market as in your pics? Why would you like one too? Kate: Not really. I might try

csharp
Copy code

**✨ Fine-tuned BART-base Output**
Ola and Momo are in Cuba. Momo is recovering from her injury. Ola will look for a new scarf.

yaml
Copy code

---

### 🔍 Example 2  

**📝 Input Dialogue**
Cara: hey
Cara: are you at home
Celine: hey Cara
Celine: No i'm not
Cara: okay then, i just wanted to pass by
Celine: im sorry, i can drop by in the evening if you dont mind
Cara: its fine, call me then if you decide to come
Celine: ok

csharp
Copy code

**✨ Fine-tuned BART-base Output**
Cara will pass by Celine in the evening.

yaml
Copy code

✅ The fine-tuned model learns to condense conversations into meaningful summaries, while the pretrained model mostly copies the input.  

---

## ⚙️ Setup Instructions  

**1️⃣ Clone the Repository**
git clone https://github.com/Zeyadelgabbas/text-summarization.git
cd text-summarization

markdown
Copy code

**2️⃣ Create Virtual Environment**
python -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows

markdown
Copy code

**3️⃣ Install Dependencies**
pip install -r requirements.txt

css
Copy code

**4️⃣ Download / Train Model**  

To train your own model:
python main.py

pgsql
Copy code

To use pretrained fine-tuned model (already trained):
```python
from textSummarizer.pipeline.prediction import PredictionPipeline

pipeline = PredictionPipeline()
summary = pipeline.predict("Your dialogue text here...")
print(summary)
5️⃣ Run FastAPI Server

nginx
Copy code
uvicorn app:app --host 0.0.0.0 --port 8080
Open your browser at:
👉 http://127.0.0.1:8080/docs

There you can test the /predict endpoint with your own dialogues.

📂 Project Structure
bash
Copy code
.
├── src/         # Core package
│   ├── config/             # Configurations
│   ├── pipeline/           # Training & prediction pipelines
│   └── ...
├── app.py                  # FastAPI server
├── main.py                 # Training entrypoint
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
🔮 Future Improvements
Experiment with DistilBART for even faster inference.

Add Gradio UI for easy testing.

Extend to multi-lingual dialogue summarization.