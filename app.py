import streamlit as st
import requests

def main():
    # Streamlit app title
    st.title("YouWriteLike")

    # Display the description
    st.markdown("""
    YouWriteLike is an AI Bot that will match your writing style with some of the most influential authors out there.
    We have built classification models that can predict which writer's style is closest to your own writing style.
    Now, play, write, and learn!
    """)

    # Display the logo centered
    st.image("assets/logo.png", width=300, use_column_width=True)

    # Display the text input field
    text = st.text_area("Enter Text")

    # Display the submit button
    if st.button("Submit"):
        url = 'https://youwritelike-5i2zktz67q-ew.a.run.app/predict_bert?text='
        response = requests.post(url + text)

        if response.status_code == 200:
            result = response.json()
            st.success("Prediction Result:")
            display_predictions(result)
        else:
            st.error("Error occurred during prediction.")

def display_predictions(predictions):
    # Display avatars and top 3 predictions with probabilities
    st.write("Top 3 Predictions:")
    avatar_size = 128
    for i, (author, prob) in enumerate(predictions.items()):
        if i >= 3:
            break

        # Display avatar
        image_path = f"assets/avatar_{author}.jpg"
        avatar_caption = f"#{i + 1} - {author}"
        # Create a sub-container for each prediction
        with st.beta_container():
            st.image(image_path, width=image_width, caption=avatar_caption, use_column_width=False, output_format="auto")

if __name__ == "__main__":
    main()
