# PassGen.py 🔐

A lightweight Python password generator with customizable options.  
Generate secure passwords quickly from your terminal—no extra dependencies required beyond Python 3.

## Screenshot 

![Passgen Screenshot](media/passgenconsole.png)

## Features ✨

- Generate passwords of any length
- Optionally exclude uppercase letters, numbers, or symbols
- Easy to run from the terminal or add to your PATH
- Lightweight and minimal, perfect for quick use


## Installation 🛠️

Clone the repository:
```bash
git clone git@github.com:d65d0econf/python_pass.git
cd python_pass
python3 passgen.py
```
note, default is 12 length, uppercase and special characters

unless flags are used

use -h for more info

## Optional Instructions for linux/macOS

create new dir if needed to place scripts
```bash
mkdir -p ~/scripts
```
place in PATH
```bash
echo 'export PATH="$HOME/scripts:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
make it executable 
``` bash
chmod +x passgen.py
mv passgen.py ~/scripts/
```

## Optional Instructions for Windows 10/11
 place 'passgen.py' in a folder 
 
```bash
C:\Users\YourName\Scripts\
```

Add that folder to your **USER PATH**:
    
Open **Environment Variables** → Edit **Path** → Add your folder.
        
(Optional) Add .PY to PATHEXT so you can run it without .py.
    
test in PowerShell

```bash
passgen.py -l 16 # or just `passgen -l 16` if PATHEXT includes .PY
```
