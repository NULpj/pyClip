import pyperclip
import time
import os
import argparse
from datetime import datetime

def save_clip(text, file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}]\n{text}\n{'-'*40}\n"
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(entry)

def monitor_clipboard(file_path):
    print("🔍 Monitoring clipboard... (Press Ctrl + C to stop)\n")
    last_clipboard = ""
    try:
        while True:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard:
                last_clipboard = current_clipboard
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}]\n{current_clipboard}")
                print("-" * 40 + "\n")
                save_clip(current_clipboard, file_path)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n❌ Stopped by user.")

def main():
    parser = argparse.ArgumentParser(description="Clipboard Logger with extra options.")
    parser.add_argument('-f', '--file', type=str, default='clip.txt', help='Filename for saving clipboard logs.')
    parser.add_argument('-c', '--clear', action='store_true', help='Clear file content before starting.')
    parser.add_argument('-s', '--start', action='store_true', help='Start monitoring the clipboard.')

    args = parser.parse_args()
    file_path = args.file

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("📋 Clipboard Log\n" + "="*40 + "\n")
        print(f"📁 {file_path} not found. Created a new file.")

    if args.clear:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("📋 Clipboard Log\n" + "="*40 + "\n")
        print(f"🧹 Cleared the contents of {file_path}.")

    if args.start:
        monitor_clipboard(file_path)
    else:
        print("ℹ️  Use '-s' or '--start' to begin clipboard monitoring.")

if __name__ == "__main__":
    main()
