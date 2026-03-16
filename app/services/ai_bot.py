# torch digunakan untuk menjalankan model AI atau engine dari model
import torch

# os Digunakan untuk memanggil system terminal
import os

# time dipanggil untuk memberikan efek seperti loading atau menunggu 
import time

# Import Model pre_trained dari hungging face 
# AutoModelForCausaILm = Upload atau Download Model dari hungging face
# AutoTokenizer = Fungsi untuk mengubah teks menjadi angka dan pre processing sedikit
from transformers import AutoModelForCausalLM,AutoTokenizer

# class ini digunakan untuk load model atau model berjalan
class ChatBotService :
    def __init__(self, model_name = "microsoft/DialoGPT-small"):
        
        print (f"Loading AI Model {model_name}")
        time.sleep(2)
        
        # Memuat tokenizer dari model yang dipilih
        # Tokenizer berfungsi untuk mengubah teks menjadi token (angka)
        # karena model AI hanya bisa membaca angka
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Memuat model bahasa (language model) dari HuggingFace
        # Model ini digunakan untuk menghasilkan respon chatbot
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        
        # OS membersihkan terminal agar clean
        os.system("cls")
        print(f"{self.model} sudah siap digunakan")
        
        
    def get_response (self,user_text: int, chat_history_ids = None):
        
        # 1. encode mengubah kata menjadi angka
        # eos_token itu untuk memberi tahu model ini akhir dari kalimat 
        new_user_input_ids = self.tokenizer.encode(
            user_text + self.tokenizer.eos_token, return_tensors = 'pt'
        )
        
        # 2. ini digunakan untuk menggabungkan chat user dengan riwayt chat sebelumnya
        # sehingga model mengingat riwayat percakapan
        if chat_history_ids is not None :
            
            # torch cat digunakan untuk menyatukan chat user dengan history
            # dim = -1 menyimpan penggabungan di dimensi terakhir
            bot_input_ids = torch.cat(
                [chat_history_ids, new_user_input_ids],
                dim=-1
            )
        
        else : 
            # Namun jika belum ada riwayat chat 
            # maka input dari user jadikan riwayat pertama 
            bot_input_ids = new_user_input_ids
            
            
        # 3. Model AI menghasilkan jawaban dari inputan user dan riwayat 
        # Generate() membuat model memulai membuat kontent baru
        new_chat_history_ids = self.model.generate (
            # Input data dari hasil user dan riwayat 
            bot_input_ids,
            
            # maksimalkan teks yaitu 1000 panjangnya
            max_length = 1000,
            
            # # Token padding menggunakan token akhir kalimat
            pad_token_id = self.tokenizer.eos_token_id
        )
            
        