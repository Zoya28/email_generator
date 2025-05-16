import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


# Function to get the response back
def getLLMResponse(form_input, email_sender, email_recipient, email_style):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.9,
    )

    # Template for building the PROMPT
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:\n
    """

    # Creating the final PROMPT
    prompt = PromptTemplate(
        input_variables=["style", "email_topic", "sender", "recipient"],
        template=template,
    )

    # Generating the response using LLM
    response = llm.invoke(
        prompt.format(
            email_topic=form_input,
            sender=email_sender,
            recipient=email_recipient,
            style=email_style,
        )
    )
    return response

# UI statrts here
st.set_page_config(
    page_title="Generate Emails",
    page_icon="📧",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.header("Generate Emails 📧")

form_input = st.text_area("Enter the email topic below: ", height=275)

col1, col2, col3 = st.columns([10,15,5])
with col1:
    email_sender = st.text_input("Sender Name")
with col2:
    email_recipient = st.text_input("Recipient Name")
with col3:
    email_style = st.selectbox(
        "Writing Style", ("Formal", "Appreciating", "Not Satisfied", "Neutral"), index=0
    )


submit = st.button("Generate")

# When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(form_input, email_sender, email_recipient, email_style).content)
