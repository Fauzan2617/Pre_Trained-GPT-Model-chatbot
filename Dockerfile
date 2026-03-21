# =========================
# 1. BASE IMAGE
# =========================

# Menggunakan image resmi Python versi 3.10 (versi ringan/slim)
# "slim" artinya:
# - ukuran lebih kecil dibanding full Python image
# - tidak membawa banyak package tambahan
# - cocok untuk production (lebih efisien)
FROM python:3.10-slim


# =========================
# 2. WORKING DIRECTORY
# =========================

# Menentukan folder kerja di dalam container
# Semua perintah berikutnya akan dijalankan dari folder ini
# Jika folder belum ada, Docker akan otomatis membuatnya
WORKDIR /code


# =========================
# 3. COPY REQUIREMENTS
# =========================

# Copy file requirements.txt dari local (laptop kamu)
# ke dalam container di folder /code
COPY ./requirement.txt /code/requirements.txt


# =========================
# 4. INSTALL DEPENDENCIES
# =========================

# Install semua library Python yang dibutuhkan
# -r → membaca daftar library dari requirements.txt
# --no-cache-dir → tidak menyimpan cache (hemat storage image)

RUN pip install --no-cache-dir -r /code/requirements.txt


# =========================
# 5. COPY SOURCE CODE
# =========================

# Copy seluruh folder app (kode FastAPI kamu)
# dari local ke dalam container
COPY ./app /code/app


# =========================
# 6. RUN APPLICATION
# =========================

# CMD adalah perintah yang dijalankan saat container start
# Kita menjalankan FastAPI menggunakan uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]