# ✍️ Next Word Prediction (LSTM + Streamlit)

## 🌐 Live App  
https://lstm-next-word.streamlit.app/

---

## 🧠 Problem Statement  

Predicting the next word in a sequence is a core problem in Natural Language Processing (NLP) and forms the foundation of modern text generation systems.

Applications include:
- Search query suggestions  
- Smart text autocomplete  
- Chatbots and virtual assistants  
- AI writing tools  

Instead of manually crafting rules, we can train deep learning models to learn language patterns from data and predict the most probable next word.

This project builds an end-to-end system to:

- Predict the next word given a sequence  
- Understand how sequence models learn language structure  
- Generate text dynamically using deep learning  
- Provide real-time predictions through an interactive web app  

---

## 🚀 What I Built  

This is a complete deep learning NLP application, not just a model.

✔ Text preprocessing pipeline using tokenizer  
✔ Sequence generation and padding  
✔ LSTM-based deep learning model  
✔ Model training and evaluation  
✔ Reusable prediction pipeline  
✔ Interactive Streamlit web application  
✔ Live deployment for real-time predictions  

This project demonstrates how sequence-based deep learning models can be used for language modeling and text generation.

---

## 📸 App Preview  

 <img width="1920" height="868" alt="lstm" src="https://github.com/user-attachments/assets/a446e5c9-88a5-4296-92d1-62b640faf589" />


---

## 📊 Key Observations  

- LSTM captures sequential dependencies better than simple RNN  
- Model learns common language patterns and word transitions  
- Predictions improve with better training data and vocabulary size  
- Context length significantly impacts prediction quality  
- Model struggles with rare or unseen words  

---

## 🛠 Tech Stack  

- Python 3.11  
- TensorFlow / Keras (LSTM)  
- NumPy  
- Streamlit (deployment)  
- NLTK (text preprocessing)  

---

## 🧩 How It Works  

1. User enters a sequence of words  
2. Text is tokenized into numerical representation  
3. Sequence is padded to fixed length  
4. LSTM model processes the sequence  
5. App returns:  
   - Predicted next word  
   - (Optional) multiple suggestions  

---

## 🧠 Model  

The model is built using a stacked LSTM architecture:

- Embedding layer to convert words into dense vector representations  
- First LSTM layer (returns sequences) to capture context  
- Dropout layer for regularization  
- Second LSTM layer for deeper sequence understanding  
- Dense output layer with softmax activation  

This architecture allows the model to learn language structure and context across sequences, making it more powerful than basic RNNs.

---

## 📈 Model Behavior  

The model performs well for:

- Common sentence patterns  
- Frequently occurring word sequences  
- Short to medium-length inputs  

However, it may struggle with:

- Long and complex sentences  
- Rare or unseen vocabulary  
- Ambiguous contexts  

This highlights the importance of data quality and sequence modeling techniques.

---

## 🎯 Skills Demonstrated  

- Deep Learning (LSTM, sequence modeling)  
- Natural Language Processing (tokenization, padding)  
- Model deployment using Streamlit  
- End-to-end ML system development  
- Handling inference pipelines and real-time predictions  

---

## ▶️ Run Locally  

```bash
git clone https://github.com/your-username/next-word-prediction.git

cd next-word-prediction

py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

streamlit run app.py
```

🔮 Future Improvements
- Generate full sentences instead of a single word
- Add top-k predictions
- Use GRU / Transformer-based models
- Improve dataset size and vocabulary
- Add temperature-based text generation
- Enhance UI/UX
