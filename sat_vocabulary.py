import random 
import tkinter as tk
from tkinter import ttk, messagebox

FILE_PATH = 'SAT100.txt'

def load_lines(path):
    """Load non-empty lines from SAT100.txt"""

    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
        
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"Could not find: {path}")
        return []
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file:\n{e}")
        return []
    
class VocabularyApp(tk.TK):
    """Builds the application window"""
    def __init__(self, lines):
        super().__init__() #runs tk.TK's window initialization code first

        # window configuration
        self.title("SAT Vocabulary Practice")
        self.geometry("650x420")
        self.minsize(600, 380)

        # initialize attributes (instance variables)
        self.lines = lines
        self.current_word = ""
        self.current_definition = ""

        # create the user interface. Helper method for use inside the class
        self._build_ui()

        if not self.lines:
            # Disable controls if we have no data
            self.submit_btn.configure(state="disabled")
            self.next_btn.configure(state="disabled")
        else:
            self.next_word()

    def _build_ui(self):
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        # Title
        title = ttk.Label(container, text="SAT Vocabulary Practice", font=("Segoe UI", 16, "bold"))
        title.pack(anchor="w", pady=(0, 10))

        # Word display
        word_frame = ttk.Frame(container)
        word_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(word_frame, text="Word:", font=("Segoe UI", 11, "bold")).pack(side="left")
        self.word_label = ttk.Label(word_frame, text="", font=("Segoe UI", 13))
        self.word_label.pack(side="left", padx=(8, 0))

        # Student answer
        ttk.Label(container, text="Type the meaning (not graded):").pack(anchor="w", pady=(6, 4))
        self.answer_entry = ttk.Entry(container, width=80)
        self.answer_entry.pack(fill="x", pady=(0, 10))

        # Buttons
        btn_frame = ttk.Frame(container)
        btn_frame.pack(fill="x", pady=(0, 12))

        self.submit_btn = ttk.Button(btn_frame, text="Submit", command=self.submit_answer)
        self.submit_btn.pack(side="left")

        self.next_btn = ttk.Button(btn_frame, text="Next Word", command=self.next_word)
        self.next_btn.pack(side="left", padx=(8, 0))

        # Definition reveal
        ttk.Label(container, text="Correct meaning:").pack(anchor="w", pady=(6, 4))
        self.definition_box = tk.Text(container, height=6, wrap="word")
        self.definition_box.pack(fill="both", expand=True)
        self.definition_box.configure(state="disabled")

        # Allow pressing Enter to submit
        self.bind("<Return>", lambda event: self.submit_answer())




if __name__ == "__main__":
    lines = load_lines(FILE_PATH)
    app = VocabularyApp(lines)
    app.mainloop()
