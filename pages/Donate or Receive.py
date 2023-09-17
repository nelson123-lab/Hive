import streamlit as st

def main():
    # Set the page layout to center the buttons
    with open('style.css') as f:
            st.markdown('<style>(f.read())</style>', unsafe_allow_html=True)

    # Add the donate button
    if st.button("Donate an Item", key="donate_button"):
        # Add your donate button logic here
        st.write("Donate button clicked!")

    # Add some space between the buttons
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    # Add the receive button
    if st.button("Receive an Item", key="receive_button"):
        # Add your receive button logic here
        st.write("Receive button clicked!")

    # Close the container div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
