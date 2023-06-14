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
    st.image("assets/logo.png", width=500, use_column_width=True)

    # Display the radio button for model selection
    model = st.radio("Select Model", ("GRUtenberg", "GutenBERT"))

    # Display the text input field
    text = st.text_area("Enter Text")

    # Display the submit button
    if st.button("Submit"):
        # Perform the API request and display the results
        url = 'http://127.0.0.1:8002/predict_bert?text='
        # print(url + text)
        requests.post(url + text)

        # Replace this with your API request code
        st.success("Submitted!")

if __name__ == "__main__":
    main()
