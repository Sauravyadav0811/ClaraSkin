# 💄 ClaraSkin – Agentic AI Skincare Assistant

ClaraSkin is an **Agentic AI-powered skincare assistant** that helps users discover personalized skincare routines based on their skin type, concerns, and budget. It uses **LangChain**, **Hugging Face LLMs**, and **Streamlit** to simulate an intelligent agent that reasons, plans, and executes tool-based actions to deliver actionable recommendations.

---

## 🧠 What Makes ClaraSkin Agentic?

ClaraSkin isn't just a chatbot — it's an **AI agent** that:
- Understands your skincare needs using LLM reasoning
- Selects tools like product search and budget calculator
- Plans the response flow and returns a personalized skincare routine
- Is modular and extendable with new tools like RAG, memory, or vision

---

## 🚀 Features

- 🧠 LangChain-based agent with Hugging Face LLM (FLAN-T5)
- 🧴 Search skincare products based on user concern and skin type
- 💸 Auto-calculate total cost of selected routine
- ⚙️ Tool-based agent architecture (easy to expand)
- 🎨 Dark-mode Streamlit UI

---

## 🧰 Tech Stack

| Feature        | Tool/Library                         |
|----------------|--------------------------------------|
| Agent Framework | LangChain                           |
| LLM             | Hugging Face Hub (`flan-t5-base`)   |
| UI              | Streamlit                           |
| Data            | Custom JSON product catalog         |
| Tools           | LangChain `Tool` API (search + calculator) |



## 📁 Folder Structure

```

ClaraSkin/
├── agent/
│   └── beauty\_agent.py         # LangChain agent setup
├── tools/
│   ├── search\_tool.py          # Searches mock product DB
│   ├── calculator\_tool.py      # Calculates product total
│   └── fake\_product\_db.json    # Mock product catalog
├── main.py                     # Streamlit UI app
├── .gitignore
├── requirements.txt
└── README.md

```

---

## 🔑 .env Setup (Optional)

If you're using an API key for Hugging Face:

```

HF\_API\_KEY=your\_huggingface\_token\_here

````

> ⚠️ Make sure `.env` is added to `.gitignore`

---

## 📦 Installation

```bash
git clone https://github.com/Sauravyadav0811/ClaraSkin.git
cd ClaraSkin
pip install -r requirements.txt
````

---

## ▶️ Run the App

```bash
streamlit run main.py
```

Then open in browser:
[http://localhost:8501](http://localhost:8501)

---

## 🧪 Sample Output

> 💄 Here's your personalized skincare routine for **oily skin with acne** under ₹1000:
>
> 1. **Salicylic Acid Cleanser** – ₹300
> 2. **Niacinamide Serum** – ₹400
> 3. **Oil-Free Moisturizer** – ₹250
>
> 🧾 Total: ₹950
> ✅ Targeted for acne-prone, oily skin.

---

## 🌟 Future Enhancements

* 🧠 Add Memory (remember previous sessions)
* 📄 Add RAG (retrieve skincare advice from PDFs)
* 🌍 Use real APIs like Amazon, Purplle, or Nykaa
* 🎯 Skin condition classifier from image (CV model)

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork the repo and improve ClaraSkin!



## 👤 Author

**Saurav Virendranath Yadav**
🔗 [GitHub](https://github.com/Sauravyadav0811)
🔗 [LinkedIn](https://linkedin.com/in/sauravyadav8113)
