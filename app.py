import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

st.title('Sentiment Analysis Model')

# User input
review = st.text_input('Enter your review:')
submit = st.button('Predict')

# Convert rating to sentiment
def rating_to_sentiment(rating):
    if rating <= 2:
        return 'Negative'
    elif rating == 3:
        return 'Neutral'
    else:
        return 'Positive'

# Emoji mapping
def sentiment_emoji(sentiment):
    emojis = {
        'Negative': '😞',
        'Neutral': '😐',
        'Positive': '😊'
    }
    return emojis.get(sentiment, '❓')

# Run prediction
if submit:
    rating = model.predict([review])[0]
    sentiment = rating_to_sentiment(rating)

    st.markdown(f"<h4 style='text-align: center;'>Predicted Rating: {rating}</h4>", unsafe_allow_html=True)

    color_map = {
        'Negative': 'red',
        'Neutral': 'orange',
        'Positive': 'green'
    }
    color = color_map.get(sentiment, 'gray')
    
    html_sentiment = f"""
        <h4 style='text-align:center; color:white; background-color:{color}; 
        padding:10px; border-radius:5px;'>Sentiment: {sentiment}</h4>
        <h1 style='text-align:center;'>{sentiment_emoji(sentiment)}</h1>
    """
    st.markdown(html_sentiment, unsafe_allow_html=True)