import pyperclip
import time
import os
import argparse
from datetime import datetime

def save_clip(text, file_path):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    entry = f"[{timestamp}]\n{text}\n{'-'*40}\n"
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(entry)

def monitor_clipboard(file_path):
    print("🔍 Monitoring clipboard... (Tekan Ctrl + C untuk berhenti)\n")
    last_clipboard = ""
    try:
        while True:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard:
                last_clipboard = current_clipboard
                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"[{timestamp}]\n{current_clipboard}")
                print("-" * 40 + "\n")
                save_clip(current_clipboard, file_path)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n❌ Dihentikan oleh pengguna.")

def main():
    parser = argparse.ArgumentParser(description="Clipboard Logger dengan opsi tambahan.")
    parser.add_argument('-f', '--file', type=str, default='clip.txt', help='Nama file untuk menyimpan log clipboard.')
    parser.add_argument('-c', '--clear', action='store_true', help='Hapus isi file sebelum memulai.')
    parser.add_argument('-s', '--start', action='store_true', help='Mulai pemantauan clipboard.')

    args = parser.parse_args()
    file_path = args.file

    # Buat file jika belum ada
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("📋 Clipboard Log\n" + "="*40 + "\n")
        print(f"📁 {file_path} tidak ditemukan, file baru dibuat.")

    # Hapus isi file jika diminta
    if args.clear:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("📋 Clipboard Log\n" + "="*40 + "\n")
        print(f"🧹 Isi file {file_path} telah dihapus.")

    # Mulai pemantauan clipboard jika diminta
    if args.start:
        monitor_clipboard(file_path)
    else:
        print("ℹ️  Gunakan opsi '-s' atau '--start' untuk memulai pemantauan clipboard.")

if __name__ == "__main__":
    main()
