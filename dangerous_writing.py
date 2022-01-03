from tkinter import *


COLORS = ["#757bc8", "#8187dc", "#8e94f2", "#9fa0ff", "#ada7ff", "#f5f5f5", "#cbb2fe", "#dab6fc", "#ddbdfc", "#333"]
TEXT_COLOR = ["#590d22", "#800f2f", "#a4133c", "#c9184a", "#ff4d6d", "#ff758f", "#ff8fa3", "#ffb3c1", "#ffccd5",
              "#fff0f3"]
FONT_NAME = "Arial"
timer = None


# ---------------------------- CHECK ------------------------------- #


def start_writing():
    textBox.config(width=150, height=50)
    start_button.grid_forget()
    start_button.config(width=10, height=10)
    textBox.focus_set()
    count_down(10)


def count_down(count):
    count_sec = count
    if count_sec > 0:
        global timer
        textBox.config(fg=TEXT_COLOR[count - 1])
        timer = window.after(1000, count_down, count_sec - 1)
    else:
        inputValue = textBox.get("1.0", "end-1c")
        print(f"Total word count: {len(inputValue.split())}")
        print(inputValue)
        textBox.delete("1.0", 'end')
        wordcount_label.config(text=f"Word count: 0")


def reset_timer(test):
    window.after_cancel(timer)
    inputValue = textBox.get("1.0", "end-1c")
    wordcount_label.config(text=f"Word count: {len(inputValue.split())}")
    count_down(10)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Dangerous Writing App")
window.config(padx=100, pady=50, bg=COLORS[9])
canvas = Canvas(width=600, height=600, bg=COLORS[9], highlightthickness=0)
textBox = Text(width=10, height=10, bg=COLORS[9], bd=0, font=(FONT_NAME, 12, "bold"), fg="#f5f5f5")
textBox.tag_config("center", justify="center")
textBox.grid(column=1, row=1)
notif_label = Label(text="Dangerous Writing App", font=(FONT_NAME, 35, "bold"), bg=COLORS[9], fg="#f5f5f5")
notif_label.grid(column=1, row=0)
start_button = Button(text="Start", bg="#6e5494", fg="#f5f5f5", height=25, width=75, font=(FONT_NAME, 25, "bold"),
                      command=start_writing)
start_button.grid(column=1, row=1)
textBox.bind_all("<KeyPress>", reset_timer)
wordcount_label = Label(text="Word count: 0", font=(FONT_NAME, 35, "bold"), bg=COLORS[9], fg="#f5f5f5")
wordcount_label.grid(column=1, row=3)

window.mainloop()
