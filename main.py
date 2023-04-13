from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from gtts import gTTS
import os
from read_file import Read_File

# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "black"
GREY = '#e5e5e5'
ORANGE = '#fca311'
YELLOW = '#ffc300'
FONT_NAME = "Courier"


# ---------------------------- FUNCTIONS ------------------------------- #

def upload_files_from_computer():
    filetypes = [('Choose File', '*.pdf *.docx *.doc *.txt')]
    file_name = askopenfilename(filetypes=filetypes)
    if file_name[-3:] != "pdf" and file_name[-3:] != "txt" and file_name[-4:] != "docx":
        messagebox.showerror(title="Wrong File Type", message="Acceptable text files: pdf, txt, docx.")
    else:
        text.delete('1.0', 'end')
        text.insert('1.0', f"{file_name}")


def convert_text_to_audio():
    to_convert = text.get('1.0', 'end')
    read_file = Read_File(to_convert)
    if len(to_convert) == 0:  # check if text area is empty
        messagebox.showerror(title="No text to convert", message="Write or upload text to convert.")
    elif ".pdf" in to_convert:  # check if uploaded pdf, txt or doc file if yes redirect to proper function
        return read_file.read_pdf_files()
    elif ".txt" in to_convert:
        return read_file.read_text_files()
    elif ".doc" in to_convert:
        return read_file.read_word_files()
    else:  # if none of above then text in text area can be directly proceed in play or save function
        return to_convert


def play():
    # Passing the text, language and slow=False - tells the module that the converted audio should have a high speed
    to_play = gTTS(text=convert_text_to_audio(),
                   lang=StringVar.get(rb_var),
                   slow=False)

    to_play.save("convert.mp3")
    os.system("convert.mp3")


def save():
    to_save = gTTS(text=convert_text_to_audio(),
                   lang=StringVar.get(rb_var),
                   slow=False)

    to_save.save("convert.mp3")
    messagebox.showinfo(title="Successful",
                        message=f'Your text file has been converted to audio and saved successfully as "convert.mp3".')


# --------------------------- GUI SETUP --------------------------------------#

window = Tk()
img = PhotoImage(file="sound4.png")
window.title("Convert text to audio")
window.geometry("900x600")
window.resizable(False, False)
canvas = Canvas(window, width=900, height=600)
canvas.create_image(450, 300, image=img)
canvas.place(x=0, y=0)

# -----Labels

title_label = Label(text=" CONVERT TEXT TO AUDIO ", fg=YELLOW, bg=BLACK, font=(FONT_NAME, 30, "bold"))
title_label.place(x=180, y=40)

write_label = Label(text=" Write the text to convert: ", fg=YELLOW, bg=BLACK, font=(FONT_NAME, 20))
write_label.place(x=220, y=200)

# -----Text

text = Text(window, width=50, height=5, fg=BLACK, bg=GREY, font=(FONT_NAME, 12))
text.place(x=200, y=250)

# -------Buttons

upload_button = Button(window, text="or UPLOAD file", width=15, height=1, font=(FONT_NAME, 14, "bold"),
                       background=BLACK,
                       activebackground=YELLOW, activeforeground=BLACK, foreground=YELLOW,
                       command=upload_files_from_computer)
upload_button.place(x=450, y=350)

play_button = Button(window, text="Play", width=10, height=1, font=(FONT_NAME, 18, "bold"),
                     background=ORANGE,
                     activebackground=GREY, activeforeground=ORANGE, foreground=BLACK,
                     command=play)
play_button.place(x=370, y=500)

save_button = Button(window, text="Save", width=10, height=1, font=(FONT_NAME, 18, "bold"),
                     background='grey',
                     activebackground=ORANGE, activeforeground='grey', foreground=ORANGE,
                     command=save)
save_button.place(x=570, y=500)

# -------- Radio Buttons

rb_var = StringVar()
rb_en = Radiobutton(window, variable=rb_var, value="en", text="en", fg="#fca311", bg=BLACK,
                    activebackground=ORANGE, font=(FONT_NAME, 20))
rb_pl = Radiobutton(window, variable=rb_var, value="pl", text="pl", fg="#fca311", bg=BLACK,
                    activebackground=ORANGE, font=(FONT_NAME, 20))
rb_var.set("pl")
rb_en.place(x=50, y=150)
rb_pl.place(x=150, y=150)


# -------------- WINDOW MAINLOOP --------------#

window.mainloop()
