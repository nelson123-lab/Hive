import streamlit as st

def main():
    st.title("What are you here for ?")
    
    st.write("Thank you for considering a donation!")
    
    # Donate button
    st.markdown(
        """
        <a href="https://your-donation-link.com" target="_blank">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 4px;">
                Donate an Item
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    
    # Receive button
    st.markdown(
        """
        <a href="https://your-receive-link.com" target="_blank">
            <button style="background-color: #008CBA; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 4px;">
                Receive an item
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
