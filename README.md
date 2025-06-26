# GUI-Workshop: Build a Qt GUI with Python

Welcome to the GUI workshop! In this session, you'll learn how to build a desktop application using Python and Qt (via PySide6), including designing your own UI files.

---

## Before the Workshop

Please ensure you have the following **installed and working** on your computer **before** the session:

1. **GitHub account** – [Sign up here](https://github.com/)
2. **Python 3+** – [Installation instructions here](https://docs.python-guide.org/starting/install3/osx/)
3. **Homebrew** `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. **Git** – `brew install git`
5. **Qt Creator / Qt Designer** – [Download here (Offline Installers)](https://www.qt.io/offline-installers)

> 💡 You do **not** need to create a Qt account to use Qt Creator. You can skip login when installing.

---

## Workshop Setup

### Step 1: **Fork this GitHub repository**
- Go to the top right of this page and click **“Fork”**
- This creates your own editable copy of the repo

---

### Step 2: **Clone your forked repo**
Open a terminal (or Git Bash) and run:

```bash
git clone https://github.com/YOUR_USERNAME/gui-workshop.git
cd gui-workshop
```

### Step 3: **Create a Python virtual environment**
```
python -m venv gui-venv
# Activate the environment:
# macOS/Linux:
source gui-venv/bin/activate
# Windows:
gui-venv\Scripts\activate
```

### Step 4: Install the required Python packages
```pip install --upgrade pip
pip install -r requirements.txt
```

---

## Workshop

Please follow along with Kaylee’s presentation during the workshop. It contains step-by-step instructions.

Presentation: [GUI Workshop Slides](https://docs.google.com/presentation/d/1qVXofIlC3Qt0AH7aOXCUngue-LeBbE73_zVk1BWPoqo/edit?usp=sharing)

Remember, to compile your .ui file to .py, run:
`pyside6-uic mainwindow.ui -o mainwindow.py`

---


