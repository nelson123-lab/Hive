import streamlit as st

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
        .button {
            margin: 10px;
            padding: 20px;
            font-size: 24px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a container div with the center class
    st.markdown('<div class="center">', unsafe_allow_html=True)

    # Add the donate button
    st.markdown('<button class="button">Donate</button>', unsafe_allow_html=True)

    # Add some space between the buttons
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # Add the receive button
    st.markdown('<button class="button">Receive</button>', unsafe_allow_html=True)

    # Close the container div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
