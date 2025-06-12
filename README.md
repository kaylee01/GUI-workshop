# GUI-Workshop: Build a Qt GUI with Python

Welcome to the GUI workshop! In this session, you'll learn how to build a desktop application using Python and Qt (via PySide6), including designing your own UI files.

---

## ✅ Prerequisites (Before the Workshop)

Please ensure you have the following **installed and working** on your computer **before** the session:

1. **GitHub account** – [Sign up here](https://github.com/)
2. **Homebrew** `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. **Python 3+** – [Installation instructions here](https://docs.python-guide.org/starting/install3/osx/)
4. **Git** – `brew install git`
5. **Qt Creator / Qt Designer** – [Download here (Offline Installers)](https://www.qt.io/offline-installers)

> 💡 You do **not** need to create a Qt account to use Qt Creator. You can skip login when installing.

---

## Part 1 - Workshop Setup (Start Here)

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

### Step 4: **Install the required Python packages
```pip install --upgrade pip
pip install -r requirements.txt
```

---

## Part 2 - **Designing your UI**
We’ll be using Qt Designer (inside Qt Creator) to visually build your app’s layout.

Step-by-Step to Create a UI File:
1. Open Qt Creator
2. Go to File > New File or Project
3. Select Qt > Qt Widgets Designer Form
4. Choose Main Window, then click Continue
5. Keep the file name as mainwindow.ui
6. Save the file inside your cloned repo folder (e.g., gui-workshop/)
7. When prompted about version control, choose “None”
8. Click Finish

✅ You’ve now created a .ui file! This is the base of your GUI.

Designing your .ui file
follow Kaylee's instructions
edit this bit and put in specifics

To compile your ui file to python
`pyside6-uic mainwindow.ui -o mainwindow.py`
---

## Part 3 -- **Python code**
TO DO



