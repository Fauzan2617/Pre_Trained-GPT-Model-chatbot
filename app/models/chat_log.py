# MEMBUAT RANCANGAN TABEL DATABASE

# Import tipe data kolom dari SQLAlchemy
# Column → untuk mendefinisikan field di tabel
# Integer → tipe angka (biasanya untuk ID)
# String → teks pendek
# Text → teks panjang (chat, paragraf)
# DateTime → untuk menyimpan tanggal dan waktu
from sqlalchemy import Column, Integer, String, Text, DateTime

# Import module datetime bawaan Python
# digunakan untuk membuat timestamp otomatis
import datetime

# Import Base dari file database (sebagai parent class semua tabel)
from app.core.database import Base

# class ini digunakan sebagai table dari database
class ChatLog (Base) :
    
    # ini nama table di database nanti
    __tablename__ = "chat_logs"
    
    
    # ====================
    # KOLOM-KOLOM DATABASE
    # ====================
    
   # Kolom ID (Primary Key)
    # - Integer → angka
    # - primary_key=True → penanda unik setiap data
    # - index=True → mempercepat pencarian berdasarkan id
    id = Column(Integer, primary_key=True, index=True)


    # Kolom Session ID
    # Digunakan untuk membedakan user atau sesi chat
    # Contoh:
    # user A → session_id = "abc123"
    # user B → session_id = "xyz789"
    session_id = Column(
        String(50),  # maksimal 50 karakter
        index=True   # dibuat index supaya pencarian cepat
    )


    # Kolom untuk menyimpan pesan dari user
    # Menggunakan Text karena panjangnya tidak terbatas
    # Cocok untuk chat panjang
    user_message = Column(Text)


    # Kolom untuk menyimpan balasan dari chatbot (AI)
    bot_response = Column(Text)


    # Kolom timestamp (waktu kejadian)
    # DateTime → menyimpan tanggal + jam
    # default=datetime.datetime.utcnow artinya:
    # - otomatis terisi saat data dibuat
    # - menggunakan waktu UTC (standar global)
    timestamp = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )