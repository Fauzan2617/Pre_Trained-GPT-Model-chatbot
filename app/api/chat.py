# APIRouter digunakan untuk routing modular atau routing dari alur chat
# Depends -> untuk depensi injection (seperti database injection)
from fastapi import APIRouter, Depends

# import session dari AQLAlchemy digunakan untuk query database
# digunakan untuk membuka session setiap nyambung ke database 
from sqlalchemy.orm import Session

# Mengecek validasi dari user apakah sudah sesuai formatnya
from pydantic import BaseModel

# membuat id unik untuk user
import uuid

# Digunakan untuk koneksi ke database
from app.core.database import SessionLocal

# import untuk menyimpan chat ke database
from app.models.chat_log import ChatLog

# import otak model AI
from app.services.ai_bot import ChatBotService

# Membuat router dari FASTAPI
router = APIRouter()

# Inisialisasi AI Service
# Model akan di-load sekali saat server start
# Ini penting agar tidak load ulang setiap request (hemat waktu & resource)
ai_service = ChatBotService()


# ================================
# Pydantic schema (validasi input)
#==================================
# Class ini digunakan untun validasi inputan dari user sesuai format
class ChatRequest(BaseModel):
    message: str
    
    session_id: str = None


#=============================
# Koneksi ke database
#=============================
# Digunakan untuk membuka sesi atau koneksi dengan database    
def get_db():
    
    # koneksi dengan database
    db = SessionLocal ()
    
    # Kirim koneksi ke enpoint
    try :
        yield db
        
    # Memastikan session selalu ditutup
    finally:
        db.close()
        
# =========================
# ENDPOINT CHATBOT
# =========================

# Endpoint POST /chat
# Akan dipanggil ketika user mengirim request ke API
@router.post("/chat")
def chat_with_bot(
    request: ChatRequest,              # data dari user (sudah divalidasi)
    db: Session = Depends(get_db)      # inject database session
):
    
    # =========================
    # 1. HANDLE SESSION ID
    # =========================

    # Ambil session_id dari request
    current_session_id = request.session_id

    # Jika belum ada → buat ID baru
    if not current_session_id:

        # uuid4() → random unique ID
        # contoh: "550e8400-e29b-41d4-a716-446655440000"
        current_session_id = str(uuid.uuid4())


    # =========================
    # 2. PROSES KE AI MODEL
    # =========================

    # Kirim pesan user ke chatbot
    # Parameter kedua (chat_history_ids) masih None
    # artinya belum pakai konteks percakapan
    bot_reply, _ = ai_service.get_response(
        request.message, 
        None
    )


    # =========================
    # 3. SIAPKAN DATA UNTUK DATABASE
    # =========================

    # Membuat object ChatLog (belum disimpan)
    new_chat_log = ChatLog(

        # simpan session_id
        session_id=current_session_id,

        # simpan pesan user
        user_message=request.message,

        # simpan jawaban AI
        bot_response=bot_reply
    )
    

    # =========================
    # 4. SIMPAN KE DATABASE
    # =========================

    # masukkan data ke session
    db.add(new_chat_log)

    # commit → simpan permanen ke database
    db.commit()


    # =========================
    # 5. RETURN RESPONSE KE USER
    # =========================

    # FastAPI otomatis convert dict → JSON
    return {

        # kirim session_id (penting untuk next request)
        "session_id": current_session_id,

        # echo pesan user
        "user_message": request.message,

        # hasil jawaban AI
        "bot_response": bot_reply
    }


