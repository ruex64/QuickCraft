
import customtkinter as ctk
from tkinter import filedialog
import subprocess
from pathlib import Path
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class DevApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Project Generator")
        self.geometry("520x540")
        self.resizable(False, False)

        self.logo_label = ctk.CTkLabel(self, text="⚙️ Project Generator", font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.pack(pady=(15, 10))

        self.framework = ctk.CTkOptionMenu(self, values=["Vite + React", "Next.js"])
        self.framework.set("Vite + React")
        self.framework.pack(pady=10)

        self.language = ctk.CTkOptionMenu(self, values=["JavaScript", "TypeScript"])
        self.language.set("JavaScript")
        self.language.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Project Name")
        self.name_entry.pack(pady=10, ipady=5)

        self.dir_button = ctk.CTkButton(self, text="📁 Choose Directory", command=self.select_dir)
        self.dir_button.pack(pady=5)

        self.dir_label = ctk.CTkLabel(self, text="No directory selected")
        self.dir_label.pack(pady=5)

        self.git_var = ctk.BooleanVar()
        self.vscode_var = ctk.BooleanVar()

        self.git_check = ctk.CTkCheckBox(self, text="✓ Initialize Git", variable=self.git_var)
        self.git_check.pack(pady=5)

        self.vscode_check = ctk.CTkCheckBox(self, text="✓ Open in VSCode", variable=self.vscode_var)
        self.vscode_check.pack(pady=5)

        self.create_button = ctk.CTkButton(self, text="🚀 Create Project", command=self.create_project)
        self.create_button.pack(pady=20)

        self.progress_label = ctk.CTkLabel(self, text="", text_color="yellow")
        self.progress_label.pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="", text_color="green")
        self.status_label.pack(pady=5)

        self.project_path = None

    def select_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.project_path = Path(path)
            self.dir_label.configure(text=str(path), text_color="white")

    def create_project(self):
        self.create_button.configure(state="disabled", text="Working...")
        self.status_label.configure(text="", text_color="green")
        threading.Thread(target=self._create_project_thread, daemon=True).start()

    def update_progress(self, percent, message):
        self.progress_label.configure(text=f"{percent}% - {message}")

    def _create_project_thread(self):
        name = self.name_entry.get().strip()
        if not name or not self.project_path:
            self.status_label.configure(text="Please enter name & select directory", text_color="red")
            self.create_button.configure(state="normal", text="🚀 Create Project")
            return

        full_path = self.project_path / name
        framework = self.framework.get()
        language = self.language.get()

        try:
            self.update_progress(10, "Initializing project...")

            if "Vite" in framework:
                template = "react-ts" if language == "TypeScript" else "react"
                run_cmd(f"npm create vite@latest {name} -- --template {template}", cwd=self.project_path)

            elif "Next.js" in framework:
                ts_flag = "--ts" if language == "TypeScript" else ""
                run_cmd(f"npx create-next-app@latest {name} {ts_flag} --use-npm", cwd=self.project_path)

            self.update_progress(60, "Installing dependencies...")
            run_cmd("npm install", cwd=full_path)
            self.update_progress(80, "Node modules installed.")

            if self.git_var.get():
                self.update_progress(85, "Initializing Git...")
                run_cmd("git init", cwd=full_path)

            if self.vscode_var.get():
                self.update_progress(95, "Opening in VSCode...")
                run_cmd("code .", cwd=full_path)

            self.update_progress(100, "Done!")
            self.status_label.configure(text=f"✅ Project ready at {full_path}", text_color="green")

        except subprocess.CalledProcessError as e:
            self.progress_label.configure(text="")
            self.status_label.configure(text=f"❌ Error: {e}", text_color="red")

        self.create_button.configure(state="normal", text="🚀 Create Project")

def run_cmd(command, cwd=None):
    subprocess.run(command, shell=True, check=True, cwd=cwd)

if __name__ == "__main__":
    app = DevApp()
    app.mainloop()
