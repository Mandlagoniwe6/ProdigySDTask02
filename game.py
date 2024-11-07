import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x400")
        
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.title_label = ctk.CTkLabel(root, text="🎲Guess the Number Game🎲", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)
        self.instruction_label = ctk.CTkLabel(root, text="📝Guess the number (between 1 and 100):", font=("Helvetica", 14))
        self.instruction_label.pack(pady=10)

        self.guess_entry = ctk.CTkEntry(root, placeholder_text="🔢Enter your guess...", font=("Helvetica", 14), width=200)
        self.guess_entry.pack(pady=10)
        self.submit_button = ctk.CTkButton(root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 14), width=150)
        self.submit_button.pack(pady=20)
        self.feedback_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.reset_button = ctk.CTkButton(root, text="Play Again", command=self.reset_game, font=("Helvetica", 14), width=150)
        self.reset_button.pack(pady=20)
        self.reset_button.pack_forget()  

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.target_number:
                self.feedback_label.configure(text="🔻 Too low! Try again.", text_color="orange")
            elif guess > self.target_number:
                self.feedback_label.configure(text="🔺 Too high! Try again.", text_color="orange")
            else:
                self.feedback_label.configure(text=f"🎉 Correct! You guessed it in {self.attempts} attempts.", text_color="green")
                self.submit_button.configure(state="disabled")  
                self.reset_button.pack()  

        except ValueError:
            self.feedback_label.configure(text="❗ Please enter a valid number!", text_color="red")

    def reset_game(self):

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.configure(text="")
        self.guess_entry.delete(0, ctk.END)
        self.submit_button.configure(state="normal")  
        self.reset_button.pack_forget()  

root = ctk.CTk()
app = GuessingGameApp(root)
root.mainloop()
