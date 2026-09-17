from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reconciliation import *
#----------CONSTANT VALUES----------------
BOLD_TITLE_FONT = ('Segoe UI', 20, 'bold')
SUB_TITLE_FONT = ('Segoe UI', 14)
SUB_TITLE_BOLD = ('Segoe UI', 14, 'bold')
TEXT_FONT = ('Segoe UI', 11)
# -----------------------------WINDOW CONFIGURATION---------------------------------
window = Tk()
window.title("Branch Sales Manager")
window.geometry("1000x800")
window.resizable(width=False, height=False)
#------------------------------FUNCTIONALITY----------------------------------------
system = ReconciliationSystem()
selected_report = None
def get_form_values():

    mpesa = validate_amount(mpesa_entry.get())
    cash = validate_amount(cash_entry.get())
    card = validate_amount(card_entry.get())
    banked = validate_amount(banked_entry.get())

    results = {'Mpesa': mpesa, 'Cash': cash, 'Card': card, 'Banked': banked}
    for key, value in results.items():
        if value is None:
            messagebox.showerror("Invalid Amount", f"{key} must be a valid non-negative number")
            return None
    return mpesa, cash, card, banked

def add_report():
    branch = branch_entry.get()
    if branch == '':
        messagebox.showerror(  "Missing Branch","Please select a branch")
        return
    form_values = get_form_values()
    if form_values is None:
        return
    mpesa, cash, card, banked = form_values

    existing_report = system.find_report(branch)
    if existing_report:
        messagebox.showerror("Duplicate Branch", f"A report for {branch} already exists")
        return

    report = SalesReport(branch, mpesa, cash, card, banked)
    system.add_report(report)

    branch_summ_value.config(text=report.branch)
    total_sales_value.config(text=report.total_sales)
    total_banked_value.config(text=report.total_banked)
    variance_value.config(text=report.variance)
    status_value.config(text=report.status)

    refresh_table()
def refresh_table():
    for item in reports_table.get_children():
        reports_table.delete(item)
    for report in system.reports:
        reports_table.insert(
            "",
            "end",
            values=(report.branch, report.total_sales, report.total_banked, report.variance, report.status)
        )

def select_report(event):
    selected = reports_table.selection()
    global selected_report
    if not selected:
        return

    values = reports_table.item(selected[0], "values")
    branch = values[0]
    report = system.find_report(branch)
    selected_report = report

    mpesa_entry.delete(0, END)
    mpesa_entry.insert(0, report.mpesa)
    cash_entry.delete(0, END)
    cash_entry.insert(0, report.cash)
    card_entry.delete(0, END)
    card_entry.insert(0, report.card)
    banked_entry.delete(0, END)
    banked_entry.insert(0, report.total_banked)

    branch_entry.config(state='disabled')
    add_button.config(state='disabled')


def update_report():
    global selected_report
    if selected_report is None:
        messagebox.showerror("No report selected", "Please select a report to update from the reports table")
        return
    form_values = get_form_values()
    if form_values is None:
        return
    mpesa, cash, card, banked = form_values

    selected_report.mpesa = mpesa
    selected_report.cash = cash
    selected_report.card = card
    selected_report.total_banked = banked
    selected_report.calculate_totals()

    system.save_reports()
    refresh_table()

    branch_summ_value.config(text=selected_report.branch)
    total_sales_value.config(text=selected_report.total_sales)
    total_banked_value.config(text=selected_report.total_banked)
    variance_value.config(text=selected_report.variance)
    status_value.config(text=selected_report.status)

    clear_form()
    selected_report = None

def clear_form():
    branch_entry.set("")
    branch_entry.config(state='readonly')
    mpesa_entry.delete(0, END)
    cash_entry.delete(0, END)
    card_entry.delete(0, END)
    banked_entry.delete(0, END)

def delete_report():
    global selected_report
    if selected_report is None:
        messagebox.showerror("No report selected", "Please select a report to delete from the reports table")
        return
    choice = messagebox.askyesno('Warning!', f'Report once deleted cannot be recovered. Are you sure you want to delete the {selected_report.branch} report?')
    if choice:
        branch = selected_report.branch
        system.delete_report(selected_report)
        messagebox.showinfo('Deleted', f'{branch} deleted successfully')
        refresh_table()
        clear_form()
        selected_report = None
    return

def reset_button():
    global selected_report
    add_button.config(state='normal')
    clear_form()
    selected_report = None


#-----------------------------WIDGET CONFIGURATION----------------------------------
header_frame = Frame(window, bg="#1F2937")
main_label = Label(header_frame, text='SALES RECONCILIATION SYSTEM', font=BOLD_TITLE_FONT, fg="white", bg="#1F2937")
main_label.pack(anchor='center')
minor_label = Label(header_frame, text='Branch reporting & reconciliation', font=SUB_TITLE_FONT, fg="white", bg="#1F2937")
minor_label.pack(anchor='center')
header_frame.pack(fill='x')

center_frame = Frame(window, bg="#F8FAFC")
#......................Report form frame........................
form_frame = Frame(center_frame, bg="white")
form_label = Label(form_frame, text='REPORT FORM', font=SUB_TITLE_BOLD, bg='white', fg="#111827")
form_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(25,20))

branch_label = Label(form_frame, text='Branch:', font=TEXT_FONT, bg='white', fg="#111827")
branch_label.grid(row=1, column=0, pady=10, padx=30, sticky='w')
branch_entry = ttk.Combobox(form_frame, values=ReconciliationSystem.VALID_BRANCHES, font=TEXT_FONT, state='readonly', width=23)
branch_entry.grid(row=1, column=1, padx=10, pady=10)

mpesa_label = Label(form_frame, text='Mpesa:', font=TEXT_FONT, bg='white', fg="#111827")
mpesa_label.grid(row=2, column=0, pady=10, padx=30, sticky='w')
mpesa_entry = Entry(form_frame, font=TEXT_FONT)
mpesa_entry.focus()
mpesa_entry.grid(row=2, column=1, padx=10, pady=10)

cash_label = Label(form_frame, text='Cash:', font=TEXT_FONT, bg='white', fg="#111827")
cash_label.grid(row=3, column=0, pady=10, padx=30, sticky='w')
cash_entry = Entry(form_frame, font=TEXT_FONT)
cash_entry.grid(row=3, column=1, padx=10, pady=10)

card_label = Label(form_frame, text='Card:', font=TEXT_FONT, bg='white', fg="#111827")
card_label.grid(row=4, column=0, pady=10, padx=30, sticky='w')
card_entry = Entry(form_frame, font=TEXT_FONT)
card_entry.grid(row=4, column=1, padx=10, pady=10)

banked_label = Label(form_frame, text='Total banked:', font=TEXT_FONT, bg='white', fg="#111827")
banked_label.grid(row=5, column=0, pady=10, padx=30, sticky='w')
banked_entry = Entry(form_frame, font=TEXT_FONT)
banked_entry.grid(row=5, column=1, padx=10, pady=10)

add_button = Button(form_frame, text='Add Report', command=add_report)
add_button.grid(row=6, column=0, padx=10, pady=10)
add_button.grid(row=6, column=0, padx=10, pady=10, sticky='we')
update_button = Button(form_frame, text='Edit', command=update_report)
update_button.grid(row=6, column=1, padx=10, pady=10, sticky='we')
reset_button = Button(form_frame, text='Reset', command=reset_button)
reset_button.grid(row=6, column=2, padx=10, pady=10, sticky='we')

input_note = Label(form_frame, text="Enter amounts in KSh", font=("Segoe UI", 9), bg="white", fg="#6B7280")
input_note.grid(row=7, column=0, columnspan=2, padx=30, pady=(5, 15), sticky="w")

form_frame.pack(side='left', fill='both', expand=True)

#.......................Summary frame.................................
summary_frame = Frame(center_frame, bg="white")
summary_label = Label(summary_frame, text='REPORT SUMMARY', font=SUB_TITLE_BOLD, bg='white', fg="#111827")
summary_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(25,20))

branch_summ_label = Label(summary_frame, text='Branch: ', font=TEXT_FONT, bg="white", fg="#111827")
branch_summ_label.grid(row=1, column=0, sticky='w')
branch_summ_value = Label(summary_frame, text='-', font=SUB_TITLE_BOLD, bg="white", padx=0)
branch_summ_value.grid(row=1, column=1, sticky='w')

total_sales_label = Label(summary_frame, text='Total sales: ', font=TEXT_FONT, bg="white", fg="#111827")
total_sales_label.grid(row=2, column=0, sticky='w')
total_sales_value = Label(summary_frame, text='-', font=SUB_TITLE_BOLD, bg="white", padx=0)
total_sales_value.grid(row=2, column=1, sticky='w')

total_banked_label = Label(summary_frame, text='Total banked: ', font=TEXT_FONT, bg="white", fg="#111827")
total_banked_label.grid(row=3, column=0, sticky='w')
total_banked_value = Label(summary_frame, text='-', font=SUB_TITLE_BOLD, bg="white", padx=0)
total_banked_value.grid(row=3, column=1, sticky='w')

variance_label = Label(summary_frame, text='Variance: ', font=TEXT_FONT, bg="white", fg="#111827")
variance_label.grid(row=4, column=0, sticky='w')
variance_value = Label(summary_frame, text='-', font=SUB_TITLE_BOLD, bg="white", padx=0)
variance_value.grid(row=4, column=1, sticky='w')

status_label = Label(summary_frame, text='Status: ', font=TEXT_FONT, bg="white", fg="#111827")
status_label.grid(row=5, column=0, sticky='w')
status_value = Label(summary_frame, text='-', font=SUB_TITLE_BOLD, bg="white", padx=0)
status_value.grid(row=5, column=1, sticky='w')

summary_frame.pack(side='right', fill='both', expand=True)
center_frame.pack(fill='x')

#........................reports table frame.......................
reports_frame = Frame(window, bg="#E5E7EB")
reports_frame.pack(fill='both', expand=True)
reports_title = Label(reports_frame, text='REPORTS', font=SUB_TITLE_BOLD, bg="#E5E7EB", fg="#111827")
reports_title.pack(anchor='w', padx=30, pady=(15,10))

reports_table = ttk.Treeview(reports_frame, columns=("Branch", "Sales", "Banked", "Variance", "Status"), show='headings')
reports_table.pack(fill='both', expand=True, padx=30, pady=(0,10))
reports_table.heading("Branch", text='Branch')
reports_table.heading("Sales", text='Sales')
reports_table.heading("Banked", text='Banked')
reports_table.heading("Variance", text='Variance')
reports_table.heading("Status", text='Status')
reports_table.bind("<<TreeviewSelect>>", select_report)
refresh_table()


#...........................delete button frame.....................
delete_frame = Frame(window, bg="#E5E7EB")
delete_frame.pack(fill='x', padx=30, pady=(0,20))
delete_button = Button(delete_frame, text='Delete Selected', command=delete_report)
delete_button.pack()











window.mainloop()