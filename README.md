# 🤖 Pre-Trained GPT Model Chatbot

Proyek ini merupakan implementasi **chatbot berbasis Pre-trained GPT Model** menggunakan Python.  
Model bahasa digunakan untuk memahami input pengguna dan menghasilkan respon otomatis seperti percakapan manusia.

Project ini memanfaatkan **Hugging Face Transformers** sebagai penyedia model bahasa, **PyTorch** sebagai framework machine learning, serta **FastAPI** untuk membuat API chatbot.

---

# 🚀 Features

- Menggunakan **Pre-trained GPT Model**
- Tokenisasi teks menggunakan tokenizer
- Mengubah input teks menjadi tensor
- Sistem percakapan sederhana
- API endpoint untuk menerima input user
- Mudah dikembangkan untuk chatbot yang lebih kompleks

---

# 🧠 Cara Kerja Sistem

Alur kerja chatbot dalam project ini:

User Input  
↓  
Tokenization (Tokenizer)  
↓  
Text → Token ID  
↓  
Token ID → Tensor (PyTorch)  
↓  
Model GPT Processing  
↓  
Generated Response  
↓  
Response ditampilkan ke user  

Prosesnya adalah:

1. User memasukkan teks
2. Teks diubah menjadi token menggunakan tokenizer
3. Token diubah menjadi angka (token id)
4. Token id diubah menjadi tensor
5. Tensor dimasukkan ke model GPT
6. Model menghasilkan respon teks

---

# 📂 Project Structure
Pre_Trained-GPT-Model-chatbot
│
├── app/
│ └── source code utama chatbot
│
├── Dockerfile
│ └── konfigurasi untuk menjalankan project menggunakan Docker
│
├── requirement.txt
│ └── daftar dependency Python
│
├── README.md
│ └── dokumentasi project
│
└── Step By step membuat chatbot pre-trained.docx
└── dokumentasi langkah pembuatan project


---

# ⚙️ Installation
Clone repository terlebih dahulu
git clone https://github.com/Fauzan2617/Pre_Trained-GPT-Model-chatbot.git

Masuk ke folder project
- cd Pre_Trained-GPT-Model-chatbot

Install dependency
- pip install -r requirement.txt


---

# ▶️ Running the Project
Menjalankan aplikasi Python
- python main.py

Jika menggunakan FastAPI
- uvicorn main:app --reload


---

# 🐳 Running with Docker

Build docker image
- docker build -t gpt-chatbot .
- Run container


---

# 📦 Dependencies

Library utama yang digunakan dalam project ini:

- transformers
- torch
- fastapi
- uvicorn
- sqlalchemy
- pymysql

---


---

# 🎯 Future Development

Beberapa pengembangan yang bisa dilakukan pada project ini:

- Menambahkan database chat history
- Fine tuning model GPT
- Membuat UI web chatbot
- Integrasi dengan Discord Bot
- Integrasi dengan Telegram Bot
- Menambahkan context memory conversation

---

# 👨‍💻 Author
Fauzan Dwi Putera  

Project ini dibuat untuk pembelajaran mengenai implementasi **Pre-trained Language Model dalam pembuatan chatbot menggunakan Python**.
