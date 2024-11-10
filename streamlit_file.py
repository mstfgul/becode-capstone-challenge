import streamlit as st
import joblib
import json
import random
from sentence_transformers import SentenceTransformer
from scrapping_final import main



classifier = joblib.load('/models/classifier_model.joblib')
label_encoder = joblib.load('/models/label_encoder.joblib')
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

with open('/scraping/articles_info.json', 'r') as f:
    articles = json.load(f)

#predict
def predict_theme(headline):
    embedding = model.encode([headline])
    label = classifier.predict(embedding)
    theme = label_encoder.inverse_transform(label)
    return theme[0]

#recommendation articles
def get_recommendations(theme, articles, num_recommendations=5):
    recommendations = [article for article in articles if article.get('theme') == theme]
    if len(recommendations) < num_recommendations:
        additional_recommendations = random.sample(articles, num_recommendations - len(recommendations))
        recommendations.extend(additional_recommendations)
    return recommendations[:num_recommendations]

#appp

if st.button("Update Data"):
    main()
    st.write("Data updated successfully.")

st.title("Theme Prediction and Article Recommendation App")
st.write("Enter a headline or theme to predict and get article recommendations:")

headline = st.text_input("Headline or Theme")

if st.button("Predict"):
    if headline:
        predicted_theme = predict_theme(headline)
        st.write(f"Predicted theme: {predicted_theme}")
        
        recommendations = get_recommendations(predicted_theme, articles)
        if recommendations:
            st.write("Here are some articles you might like:")
            for rec in recommendations:
                title = rec.get('title', 'No title available')
                summary = rec.get('Summary', 'No summary available')
                theme = rec.get('Theme', 'No theme available')
                link = rec.get('Link', '#')
                
                st.write(f"**Title**: {title}")
                st.write(f"**Summary**: {summary}")
                st.write(f"**Theme**: {theme}")
                st.write(f"[Read more]({link})")
                st.write("---")
        else:
            st.write("No recommendations found for this theme.")
    else:
        st.write("Please enter a headline.")
