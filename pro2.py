import tkinter as tk
from tkcalendar import Calendar, DateEntry
def on_date_selected(event):
    selected_date = cal.get_date()
    date_button.config(text=selected_date)
root = tk.Tk()
root.title("Calendar")
cal = Calendar(root, selectmode='day', date_pattern='mm-dd-yyyy')
cal.pack(pady=20)
date_button = tk.Button(root, text="Select Date", command=lambda: cal.selection_set())
date_button.pack(pady=10)
cal.bind("<<CalendarSelected>>", on_date_selected)
root.mainloop()




