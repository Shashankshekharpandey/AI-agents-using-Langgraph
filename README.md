![image](https://github.com/user-attachments/assets/21c9b566-20f9-4b02-806e-853225405951)

Here's a README file for your **AI Chatbot Agents** project:  

---

### **AI Chatbot Agents 🚀**  
A **fully interactive AI-powered chatbot UI** built using **Streamlit**. This chatbot allows users to select different **AI models (Groq, OpenAI)**, define system prompts, enable web search, and interact with the chatbot.  

---

## **🌟 Features**  
✅ **Select AI Model Provider** (Groq / OpenAI)  
✅ **Choose from Multiple AI Models**  
✅ **Customizable System Prompt**  
✅ **Enable Web Search** for real-time information  
✅ **User-Friendly & Interactive UI** with a modern design  
✅ **FastAPI Backend for API Communication**  

---

## **🛠️ Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Shashankshekharpandey/AI-agents-using-Langgraph.git
cd your-repo
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**  
Create a **.env** file and add your API keys:  
```sh
OPENAI_API_KEY="your_openai_api_key"
GROQ_API_KEY="your_groq_api_key"
TRAVILY_API_KEY="your_tavily_api_key"
```

### **4️⃣ Run the FastAPI Backend**  
```sh
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### **5️⃣ Run the Streamlit Frontend**  
```sh
streamlit run app.py
```

---

## **🖥️ Usage**  
1. Open the **Streamlit app** in your browser.  
2. Define the **AI system prompt** (e.g., "You are a software engineer").  
3. Choose the **AI model provider** (Groq / OpenAI).  
4. Select a **model** (e.g., `llama-3.3-70b-versatile`).  
5. Enable **web search** if needed.  
6. Enter a **query** and click **Ask Agent!**  

---

## **📌 Technologies Used**  
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **APIs:** OpenAI, Groq, Tavily Search  
- **Deployment:** Uvicorn  

---

## **📜 License**  
This project is open-source under the **MIT License**.  

---

Let me know if you need modifications! 🚀
