# 📸 Image Email Generator using LLM & Streamlit

A simple yet powerful Streamlit web app that uses Large Language Models (LLMs) to generate professional or casual emails based on user input and optionally includes an image. Whether you're sending business emails or dropping casual notes, this app has your back (and a touch of AI magic ✨).

---

## 🧠 Features

* 📝 Generate email content using user-provided prompts
* 🎨 Select email style (Formal, Casual, Friendly, etc.)
* 👤 Custom fields for sender and recipient
* ⚡ Powered by LLMs like OpenAI or similar
* 🌐 Built with Streamlit for an easy-to-use UI

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain / OpenAI API**
* **Virtual Environment (`venv`)**

---

## 🚀 Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/Zoya28/email_generator.git
   cd image-email-generator
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   * On Windows:

     ```bash
     .\venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 📥 Input Fields

* **Email Prompt** – Describe what the email is about
* **Sender** – Name of the email sender
* **Recipient** – Who you're sending the email to
* **Email Style** – Choose the tone (e.g., formal, casual)

---

## 🧪 Example Use Case

> **Prompt:** “Invite team to project kickoff meeting next Monday”
> **Style:** Formal
> **Recipient:** Team
> **Sender:** Project Manager
> → Generates a polished invitation email. 💼

---

## 💡 To-Do

* Add email sending functionality (via SMTP or API)
* Save generated emails to history
* Allow custom templates

---

## 🤝 Contributing

Pull requests are welcome!

