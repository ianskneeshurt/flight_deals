from tkinter import *

window = Tk()
window.title("Broke Boi Flight Scanner")
window.config(bg="#94A684")

#pic Canvas
canvas = Canvas(height=300, width=300, background="#E4E4D0", highlightbackground="#E4E4D0")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=0, rowspan=5)

#lower Canvas
fly_from_label = Label(text="Fly From:", background="#FFEEF4", highlightbackground="#FFEEF4")
fly_from_label.grid(row=0, column=1)
fly_to_label = Label(text="Fly To:", background="#FFEEF4", highlightbackground="#FFEEF4")
fly_to_label.grid(row=1, column=1)

window.mainloop()