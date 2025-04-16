# 📋 pyClip - Clipboard Logger

**pyClip** is a simple Python script that automatically logs copied clipboard text into a file and displays it in the terminal with a timestamp.

---

## ✨ Features

- 📝 Save clipboard content into a `.txt` file
- 🕒 Add timestamp to each entry
- 📺 Display new clipboard content in the terminal
- 🗃️ Option to set custom output file name
- 🧹 Option to clear file before logging
- ✅ Continuous monitoring (until manually stopped)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NULpj/clipboard-logger.git
   cd pyClip
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

```bash
python clipboard_logger.py [options]
```

### Options

| Option           | Description                                       |
|------------------|---------------------------------------------------|
| `--file`, `-f`   | Specify the log file name (default: `clip.txt`)   |
| `--clear`, `-c`  | Clear file content before starting                |
| `--start`, `-s`  | Start monitoring the clipboard                    |

### Example

```bash
python clipboard_logger.py -f mylog.txt -c -s
```

---

## 🧪 Example Output

```bash
[2025-04-16 18:05:17]
Hello World
LOL
----------------------------------------
```

---

## 🛑 Notes

- This script runs until the terminal is closed or stopped manually.
- For background execution, consider using `nohup` on Linux or Task Scheduler on Windows.

---

## 📜 License

GNU License.
