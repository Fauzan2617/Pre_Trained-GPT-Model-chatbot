# MENGATUR KONEKSI KE DATABASE

# Create Engine dibuat untuk membuat mesin untuk SQL 
# Bertugas untuk menghubungkan aplikasi dan database 
# dan mengeksekusi SQL
from sqlalchemy import create_engine

# Library ini digunakan untuk membuat jiplakan dari database di database
from sqlalchemy.ext.declarative  import declarative_base

# Library ini dipakai untuk membuat session setiap kali terhubung dengan database
from sqlalchemy.orm import sessionmaker

# 1. Membuat lokasi database lokal di laptop
# Format atau artinya:
# sqlite : jenis database
# /// : path relatif
# ./ : folder project saat ini
# chatbot_history.db : nama file di database
SQLALCHEMY_DATABASE_URL = "sqlite:///./chatbot_history.db"
# Catatan:
# Jika nanti ingin menggunakan database lain seperti MySQL:
# contoh:
# "mysql+pymysql://username:password@localhost/nama_database"



# 2. Membuat engine\mesin dari database
# beberapa tugas dari engine ini
# - Menghubungkan dengan database
# - Mengesekusi perintah SQL
# - Mengelola koneksi
engine = create_engine (
    # lokasi database lokal
    SQLALCHEMY_DATABASE_URL,
    
    # connect_args digunakan untuk KHUSUS untuk SQlite
    # Check_same_thread = False artinya
    # - mengizinkan satu koneksi oleh beberapa thread
    # - karena FastAPI bersifat multi-thread
    connect_args= {"check_same_thread ": False}
)


# Membuat SESSION LOCAL
# Session adalah "jalur komunikasi" antara aplikasi dan database
# alurnya simple
# - buka session
# - lakukan query
# - tutup session
SessionLocal = sessionmaker (
    
    # autocommit = false adalah
    # - perubahan tidak langsung terjadi di database
    # - memakai db.commit() secara manual
    # - ini dipakai karena lebih aman dibanding langsung di database
    autocommit = False,
    
    # Autoflush = false adalah 
    # dimana data tidak langsung dikirim ke database sebelum commmit
    autoflush= False,
    
    # Session ini terhubung dengan engine sebelumnya saat dibuat
    bind = engine
)

# 4. Membuat BASE CLASS (cetakan tabel)
# Base ini digunakan sebagai "induk" untuk semua model database
# Nanti setiap tabel akan dibuat sebagai class Python yang mewarisi Base
Base = declarative_base()

# Contoh penggunaan Base (di file lain):
#
# class ChatHistory(Base):
#     __tablename__ = "chat_history"
#
#     id = Column(Integer, primary_key=True)
#     message = Column(String)
#
# Jadi Base ini seperti "template awal" untuk semua tabel