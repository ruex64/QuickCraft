
# 🚀 QuickCraft

**QuickCraft** is a beginner-friendly Python GUI application that lets you create modern web development projects using **Vite + React** or **Next.js** in just a few clicks — no terminal required.

It supports both **JavaScript** and **TypeScript**, with optional **Git** initialization and automatic **VSCode** project opening. Ideal for new developers or anyone who wants to speed up project bootstrapping.

---

## ✨ Features

- 🔧 Choose between **Vite + React** or **Next.js**
- ⚙️ Select **JavaScript** or **TypeScript**
- 📁 Pick any directory to create your project
- ✅ Optional: Initialize Git repository
- 💻 Optional: Open project in **Visual Studio Code**
- 📊 Clean, animated progress indicator
- 🪟 Simple and modern desktop GUI (no terminal clutter)

---

## 📦 Requirements

Make sure the following are installed before running:

| Tool         | Description                   | Download Link |
|--------------|-------------------------------|----------------|
| Python 3.10+ | Required to run the app       | [python.org](https://www.python.org/downloads/) |
| Node.js      | Needed for `npm` and `npx`    | [nodejs.org](https://nodejs.org/) |
| VSCode       | For the "Open in VSCode" feature | [code.visualstudio.com](https://code.visualstudio.com/) |

---

## 🛠 Setup Instructions

### 🔹 1. Clone or Download

```bash
git clone https://github.com/YOUR_USERNAME/quickcraft.git
cd quickcraft
```

Or [Download as ZIP](https://github.com/YOUR_USERNAME/quickcraft/archive/refs/heads/main.zip)

### 🔹 2. Install Dependencies

```bash
pip install customtkinter
```

### 🔹 3. Run the App

```bash
python quickcraft.py
```

You'll see the GUI launch. Pick your options and click **"Create Project"**.

---

## 🧪 Optional: Create `.exe`

Want to share or use without opening Python?

```bash
pip install pyinstaller

pyinstaller --noconsole --onefile --icon=icon.ico quickcraft.py
```

The `.exe` will appear inside the `dist/` folder.

You can then upload this `.exe` file to a GitHub Release.

---

## 📁 Folder Structure

```
QuickCraft/
├── quickcraft.py         # Main source code
├── README.md             # This file
├── LICENSE               # MIT License
├── icon.ico              # Optional app icon
├── dist/                 # Compiled .exe file (after build)
└── assets/               # Screenshots, future themes, etc. (optional)
```

---

## 🧩 Customizing the Code

To add support for your own templates, modify these parts:

| Part | What it does |
|------|--------------|
| `OptionMenu` widgets | Add more frameworks or languages |
| `_create_project_thread()` | Add custom install logic |
| `run_cmd()` | Executes terminal commands |
| `update_progress()` | Shows status in the GUI |

---

## 📤 Publishing Updates

1. Edit `quickcraft.py` and test changes
2. Build new `.exe` with PyInstaller
3. Go to GitHub → Releases → Draft new release
4. Attach the updated `.exe`

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE). Free to use, modify, and distribute.

---

Made with ❤️ by [Your Name]
