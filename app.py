import streamlit as st

def main():
    # Streamlit app title
    st.title("YouWriteLike Streamlit App")

    # Load and display the HTML content
    with open("page.html", "r") as file:
        html_code = file.read()
        st.components.v1.html(html_code, height=800)

if __name__ == "__main__":
    main()
