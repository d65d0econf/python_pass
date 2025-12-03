# PassGen.py 🔐

A lightweight Python password generator with customizable options.  
Generate secure passwords quickly from your terminal—no extra dependencies required beyond Python 3.


## Features ✨

- Generate passwords of any length
- Optionally exclude uppercase letters, numbers, or symbols
- Easy to run from the terminal or add to your PATH
- Lightweight and minimal, perfect for quick use


## Installation 🛠️

1. Clone the repository:
```bash
git clone git@github.com:d65d0econf/python_pass.git
cd python_pass
```
## Optional Instructions for linux/windows
make it executable and run in PATH to use anywhere 
``` bash
chmod +x passgen.py
```
for windows, add ```passgen.py``` to 
C:\Users\YourName\Scripts\
    - Add that folder to your **USER PATH**:
        Open **Environment Variables** → Edit **Path** → Add your folder.
    - (Optional) Add `.PY` to `PATHEXT` so you can run it without `.py`.
    - test in PowerShell

```powershell 
passgen.py -l 16 # or just `passgen -l 16` if PATHEXT includes .PY
```
