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
    
class VocabularyApp(tk.Tk):
    """Builds the application window"""
    def __init__(self, lines):
        super().__init__() #runs tk.TK's window initialization code first

        # window configuration
        self.title("SAT Vocabulary Practice")
        self.geometry("865x545")
        self.minsize(780, 495)

        # initialize attributes (instance variables)
        self.all_lines = lines[:] # immutable list of words
        self.remaining_lines = lines[:] # mutable list of words (word removed after it is reviewed)
        self.current_word = ""
        self.current_definition = ""
        self.words_attempted = 0
        self.total_words = len(self.all_lines)
        self.completed = False # will be set to True after all words reviewed

        # create the user interface. 
        self._build_ui()

        if not self.all_lines:
            # Disable controls if we have no data
            self.submit_btn.configure(state="disabled")
            self.next_btn.configure(state="disabled")
        else:
            self._update_counter()
            self.next_word()

    def _build_ui(self):
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        # widgets styling
        style = ttk.Style()
        style.configure(
            "Word.TLabel",
            font=("Segoe UI", 30, "bold"),
            foreground="#1f4fd8"   # deep blue
        )
                        
        # Title
        title = ttk.Label(container, text="SAT Vocabulary Practice", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(0, 20))

        # Word display
        word_frame = ttk.Frame(container)
        word_frame.pack(pady=(0, 18))
       
        self.word_label = ttk.Label(word_frame, text="", style="Word.TLabel")
        self.word_label.pack()
        
        # Student answer
        ttk.Label(container, text="Type your answer (optional)", font=("Segoe UI", 11)).pack(pady=(6, 2))
        self.answer_entry = tk.Entry(container, font=("Segoe UI", 14), width=40)
        self.answer_entry.pack(pady=(0, 20), ipady=6)

        # Buttons
        btn_frame = ttk.Frame(container)
        btn_frame.pack(pady=(22, 18))

        # wrapping the buttons in an inner frame
        inner = ttk.Frame(btn_frame)
        inner.pack()

        self.submit_btn = tk.Button(
                inner, 
                text="Show Definition", 
                font=("Segoe UI", 13, "bold"), 
                bg="#1f4fd8",        # blue
                fg="white",
                activebackground="#173aa8",
                activeforeground="white",
                padx=14,
                pady=6,
                command=self.submit_answer
        )
        self.submit_btn.pack(side="left")

        self.next_btn = tk.Button(
            inner,
            text="Next Word", 
            font=("Segoe UI", 13, "bold"),
            bg="#f4f6f8",   # soft slate
            fg="#333333",
            activebackground="#e6e9ed",
            padx=14,
            pady=6, 
            command=self.next_word
        )
        self.next_btn.pack(side="left", padx=(18, 0))

        # Definition reveal
        self.definition_label = tk.Label(
            container,
            text="",
            font=("Segoe UI", 14),
            bg="#f6f6f6",
            fg="#2c3e50",        # slate/navysteel blue emphasis
            wraplength=720,      # tuned for 865px window; adjust if needed
            justify="center",
            padx=12,
            pady=10
        )
        self.definition_label.pack(pady=(12, 12))

        # status bar
        status_frame = ttk.Frame(container)
        status_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.counter_label = ttk.Label(status_frame, text="")
        self.counter_label.pack(side="right")

        # Allow pressing Enter to submit
        self.bind("<Return>", lambda event: self.submit_answer())

    def _set_definition_text(self, text):
        self.definition_label.configure(text=text)

    def next_word(self):
        if self.completed:
            self._reset_word_list()

        self._prepare_ui_for_new_word()

        if not self.remaining_lines:
            self._reset_deck()

        line = random.choice(self.remaining_lines)
        self.remaining_lines.remove(line)
        word, definition = line.split(None, 1)

        # Your capitalization choice:
        word = word.capitalize()
        definition = definition.capitalize()

        self.current_word = word
        self.current_definition = definition

        self.word_label.configure(text=self.current_word)
        self.answer_entry.delete(0, "end")
        #self._set_definition_text("")  # clear definition until submitted
        self.answer_entry.focus_set()

    def submit_answer(self):
        # No grading: reveal the correct definition
        self._set_definition_text(self.current_definition)

        # Count this as "attempted" and update UI
        self.words_attempted += 1
        self._update_counter()

        # disable the submit button after clicking it
        self.submit_btn.configure(state="disabled")

        # If that was the last word, notify and reset on next "Next Word"
        if len(self.remaining_lines) == 0:
            messagebox.showinfo(
                "All Done",
                "Congratulations! You have reviewed all the words.\n\n"
                "Clicking 'Next Word' will reset the word list and your progress."
                )
            self.completed = True
            self.next_btn.configure(text="Restart")

    def _update_counter(self):
        self.counter_label.configure(
            text=f"{self.words_attempted} words answered out of {self.total_words}"
        )

    def _prepare_ui_for_new_word(self):
    # Clear definition and re-enable submit button for a new attempt
        self._set_definition_text("")
        self.submit_btn.configure(state="normal")
        self._update_counter()

    def _reset_word_list(self):
        self.remaining_lines = self.all_lines[:]
        self.words_attempted = 0
        self.completed = False
        self.next_btn.configure(text="Next Word")


if __name__ == "__main__":
    lines = load_lines(FILE_PATH)
    app = VocabularyApp(lines)
    app.mainloop()
