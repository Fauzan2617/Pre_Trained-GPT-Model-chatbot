# Import class utama FastAPI → digunakan untuk membuat aplikasi web/API
from fastapi import FastAPI

# Import router dari module chat → berisi endpoint /chat
from app.api import chat

# Import engine dan Base dari database
# engine → koneksi ke database
# Base → blueprint semua tabel
from app.core.database import engine, Base


# =========================
# 1. AUTO CREATE TABLE
# =========================

# Perintah ini akan:
# - membaca semua class model yang mewarisi Base (misalnya ChatLog)
# - membuat tabel di database jika belum ada
# - tidak akan overwrite tabel yang sudah ada
Base.metadata.create_all(bind=engine)


# =========================
# 2. INISIALISASI FASTAPI
# =========================

# Membuat instance aplikasi FastAPI
# Parameter ini akan muncul di dokumentasi Swagger (/docs)
app = FastAPI(

    # Judul API
    title="Enterprise AI Chatbot API",

    # Deskripsi API (menjelaskan fungsi aplikasi)
    description="API untuk melayani permintaan chat menggunakan AI berbasis PyTorch",

    # Versi API (penting untuk versioning di production)
    version="1.0.0"
)


# =========================
# 3. REGISTER ROUTER
# =========================

# Menghubungkan router dari chat.py ke aplikasi utama
app.include_router(

    # router yang sudah dibuat di file chat.py
    chat.router,

    # prefix URL → semua endpoint di chat.py akan diawali /api
    # contoh:
    # /chat → menjadi /api/chat
    prefix="/api",

    # tags → untuk grouping di Swagger UI (/docs)
    tags=["Chatbot"]
)


# =========================
# 4. HEALTH CHECK ENDPOINT
# =========================

# Endpoint sederhana untuk mengecek apakah server berjalan
# Bisa diakses di: http://localhost:8000/
@app.get("/")
def read_root():

    # Mengembalikan response dalam format JSON
    return {

        # status server
        "status": "Server berjalan dengan baik!",

        # informasi tambahan untuk user/developer
        "bantuan": "Akses /docs untuk melihat dokumentasi API"
    }