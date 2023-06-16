import streamlit as st
import requests

def main():
    # Streamlit app title
    st.title("YouWriteLike")

    # Display the description
    st.markdown("""
    YouWriteLike is an AI classifier that will match your writing style with some of the most influential authors out there.
    We have built a model that can predict which writer's style is closest to your own writing style.
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
    num_columns = 3
    num_predictions = min(len(predictions), num_columns)

    # Create columns
    columns = st.beta_columns(num_columns)
    avatar_size = 128

    # Display predictions in columns
    for i, (author, prob) in enumerate(predictions.items()):
        if i >= num_predictions:
            break

        # Display avatar
        image_path = f"assets/avatar_{author}.jpg"
        avatar_caption = f"#{i + 1} - {author}"
        with columns[i % num_columns]:
            st.image(image_path, width=avatar_size, caption=avatar_caption, use_column_width=False, output_format="auto")

if __name__ == "__main__":
    main()
