import streamlit as st

st.title("What are you here for ?")

def main():
    # Set the page layout to center the buttons
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a container div with the center class
    st.markdown('<div class="center">', unsafe_allow_html=True)

    # Add the donate button
    if st.button("Donate an Item"):
        # Add your donate button logic here
        st.write("Donate button clicked!")

    # Add some space between the buttons
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # Add the receive button
    if st.button("Receive an Item"):
        # Add your receive button logic here
        st.write("Receive button clicked!")

    # Close the container div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
