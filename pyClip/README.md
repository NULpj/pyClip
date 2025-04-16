# 📋 Clipboard Logger

**Clipboard Logger** adalah script Python sederhana untuk merekam teks yang disalin ke clipboard secara otomatis, menyimpannya ke file log, dan menampilkannya langsung di terminal dengan timestamp.

---

## ✨ Fitur

- 📝 Menyimpan semua teks clipboard ke file `.txt`
- 🕒 Menambahkan timestamp setiap entri
- 📺 Menampilkan teks baru langsung ke terminal
- 🗃️ Opsi untuk menentukan nama file log
- 🧹 Opsi untuk menghapus isi file log sebelum memulai
- ✅ Bisa dijalankan terus menerus (selama terminal aktif)

---

## 📦 Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/clipboard-logger.git
   cd clipboard-logger
   ```

2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Penggunaan

```bash
python clipboard_logger.py [opsi]
```

### Opsi:

| Opsi         | Keterangan                                           |
|--------------|------------------------------------------------------|
| `--file`, `-f`   | Menentukan nama file output (default: `clip.txt`) |
| `--clear`, `-c`  | Hapus isi file sebelum mulai                      |
| `--start`, `-s`  | Memulai pemantauan clipboard                     |

### Contoh:

```bash
python clipboard_logger.py -f logku.txt -c -s
```

---

## 🧪 Contoh Output

```bash
[2025-04-16 18:05:17] 📋 Teks baru disalin:
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
----------------------------------------
```

---

## 🛑 Catatan

- Proses akan berhenti jika terminal ditutup.
- Untuk menjalankan secara terus menerus di background, gunakan `nohup` (Linux) atau scheduler (Windows).

---

## 📜 Lisensi

Proyek ini menggunakan lisensi MIT.
