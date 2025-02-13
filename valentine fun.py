import tkinter as tk
from tkinter import messagebox

# Function to show the next screen after clicking the button
def next_screen(answer=None):
    if answer == 'yes':
        messagebox.showinfo("Message", "I Love You!", icon="info")
        window.quit()  # Close the window after the message
    elif answer == 'no':
        messagebox.showinfo("Message", "You still need to go with me.", icon="info")
        window.quit()  # Close the window after the message

# Initialize the main window
window = tk.Tk()
window.title("Will you be my Valentine?")
window.geometry("400x300")  # Set window size
window.config(bg="#ffcccb")  # Set background color

# Title label with a larger font and bold
label = tk.Label(window, text="Will you be my Valentine?", font=("Helvetica", 18, "bold"), bg="#ffcccb", fg="#d60000")
label.pack(pady=30)

# Styling for buttons
button_style = {
    "font": ("Helvetica", 14),
    "width": 15,
    "height": 2,
    "relief": "raised",
    "bd": 5,
    "highlightthickness": 0
}

# Button to show the next screen after click
def on_button_click():
    # Change to the next screen with Yes and No buttons
    label.config(text="Do you want to be my Valentine?", fg="#d60000")
    yes_button.pack(pady=10)
    no_button.pack(pady=10)
    click_button.pack_forget()  # Hide the original click button

# Button that says "Click Me"
click_button = tk.Button(window, text="Click Me", command=on_button_click, **button_style, bg="#ff6666", activebackground="#ff4d4d", fg="white")
click_button.pack()

# Yes button to answer 'Yes'
yes_button = tk.Button(window, text="Yes", command=lambda: next_screen('yes'), **button_style, bg="#28a745", activebackground="#218838", fg="white")

# No button to answer 'No'
no_button = tk.Button(window, text="No", command=lambda: next_screen('no'), **button_style, bg="#dc3545", activebackground="#c82333", fg="white")

# Start the window loop
window.mainloop()
