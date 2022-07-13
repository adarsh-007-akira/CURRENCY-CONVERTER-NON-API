from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# WINDOW

window=Tk()
window.title("CURRENCY CONVERTER -- NON API BASED")
window.geometry("500x500")

#NOTEBOOK

note=ttk.Notebook(window)
note.pack(pady=5)

# CURRENCY FRAME AND CONVERSION FRAME

currency_frame=Frame(
	note, 
	width = 480, 
	height=480
	)

conversion_frame=Frame(
	note,
	width=480,
	height=480,
	)

currency_frame.pack(
	fill="both", 
	expand=1
	)

conversion_frame.pack(
	fill="both", 
	expand =1
	)

# TABS

note.add(
	currency_frame, 
	text="CURRENCY",
	)

note.add(
	conversion_frame,
	text="CONVERT",
	)

# DISABLER

note.tab(
	1, 
	state="disabled"
	)

# HOME CURRENCY

#FUNCTIONS

def lock():
	
	if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
		
		messagebox.showwarning("ERROR", "PLEASE FILL ALL THE REQUIRED FIELDS")
	
	else:
		home_entry.config(state="disabled")
		conversion_entry.config(state="disabled")
		rate_entry.config(state="disabled")
		
		note.tab(1, state="normal")

		amount_label.config(
			text=f"AMOUNT OF {home_entry.get()} TO CONVERT TO {conversion_entry.get()}"
			)

		converted_label.config(
			text=f"EQUALS THIS MANY {conversion_entry.get()}"
			)

		convert_button.config(
			text=f"CONVERT FROM {home_entry.get()}"
			)

def unlock():
	home_entry.config(state="normal")
	conversion_entry.config(state="normal")
	rate_entry.config(state="normal")
	note.tab(1, state="disabled")

# HOME 

home=LabelFrame(
	currency_frame,
	text="HOME CURRENCY",
	)

home.pack(
	pady=20
	)

home_entry= Entry(
	home,
	font=("Helvetica", 24)
	)

home_entry.pack(
	pady=10,
	padx=10
	)

# CONVERSION CURRENCY

conversion=LabelFrame(
	currency_frame, 
	text="CONVERSION CURRENCY"
	)

conversion.pack(
	pady=20
	)

conversion_label=Label(
	conversion,
	text="CONVERSION TO"
	)

conversion_label.pack(
	pady=10
	)

conversion_entry = Entry(
	conversion,
	font=("Helvetica", 24)
	)

conversion_entry.pack(
	pady=10,
	padx=10
	)

# RATE

rate_label=Label(
	conversion,
	text="CONVERSION RATE"
	)

rate_label.pack(
	pady=10
	)

rate_entry = Entry(
	conversion,
	font=("Helvetica", 24)
	)

rate_entry.pack(
	pady=10,
	padx=10
	)

# BUTTONS

button_frame=Frame(
	currency_frame
	)

button_frame.pack(
	pady=20
	)

lock_button=Button(
	button_frame,
	text="LOCK",
	command=lock
	)

lock_button.grid(
	row=0,
	column=0,
	padx=10,
	)

unlock_button=Button(
	button_frame,
	text="UNLOCK",
	command=unlock
	)

unlock_button.grid(
	row=0,
	column=1,
	padx=10,
	)

# CONVERSION

#FUNCTIONS

def convert():
	
	converted_entry.delete(0, END)

	conversion = float(rate_entry.get()) * float(amount_entry.get())

	conversion = round(conversion, 2)

	conversion = '{:,}'.format(conversion)

	converted_entry.insert(0, conversion)


def clear():
	amount_entry.delete(0, END)
	converted_entry.delete(0, END)

# AMOUNT

amount_label= LabelFrame(
	conversion_frame,
	text="AMOUNT TO CONVERT "
	)

amount_label.pack(
	pady = 20
	)

amount_entry = Entry(
	amount_label,
	font=("Helvetica", 24)
	)

amount_entry.pack(
	pady=10,
	padx=10,
	)

# CONVERT

convert_button=Button(
	amount_label,
	text="CONVERT",
	command=convert
	)

convert_button.pack(
	pady=20
	)

converted_label=LabelFrame(
	conversion_frame,
	text="CONVERTED CURRENCY"
	)

converted_label.pack(
	pady=20
	)

converted_entry = Entry(
	converted_label,
	font=("Helvetica", 24),
	bd=0,
	bg="systembuttonface"
	)

converted_entry.pack(
	pady=10,
	padx=10,
	)

# CLEAR BUTTON

clear_button=Button(
	conversion_frame,
	text="CLEAR",
	command=clear	
	)

clear_button.pack(
	pady=20,
	)

# FAKE LABEL

spacer= Label(
	conversion_frame,
	text="",
	width=68,
	)

spacer.pack()

window.mainloop()