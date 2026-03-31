import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

# Load the trained model and tokenizer
model = load_model('models/next_word_prediction_model.h5')
with open('models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#Function to predict next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted)
    
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

st.title("Next Word Prediction")
input_text = st.text_input("Enter a sequence of words:")
if st.button("Predict"):
    if input_text:
        max_sequence_len = model.input_shape[1]
        predicted_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
        if predicted_word:
            st.write(f"Predicted next word: {predicted_word}")
        else:
            st.write("Could not predict the next word.")
    else:
        st.write("Please enter some text to predict the next word.")
