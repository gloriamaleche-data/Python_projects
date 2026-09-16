import pandas
import time

reports =[]
branches = ['Nairobi', 'Karen', 'Kisumu', 'Kakamega']
branches_added = []

def reconcile(mpesa_val, cash_val, card_val, total_banked_val):
    total_sales = mpesa_val + cash_val + card_val
    variance = total_banked_val - total_sales

    return variance != 0, variance

def amounts_verifications():
    while True:
        try:
            mpesa = int(input('Mpesa amount: '))
            if mpesa < 0:
                print('Amount cannot be negative')
                continue
            break
        except ValueError:
            print('Invalid input. Use integers only. Try again.')
            continue
    while True:
        try:
            cash = int(input('Cash amount: '))
            if cash < 0:
                print('Amount cannot be negative')
                continue
            break
        except ValueError:
            print('Invalid input. Use integers only. Try again.')
            continue
    while True:
        try:
            card = int(input('Card amount: '))
            if card < 0:
                print('Amount cannot be negative')
                continue
            break
        except ValueError:
            print('Invalid input. Use integers only. Try again.')
            continue
    while True:
        try:
            total_banked = int(input('Total amount banked: '))
            if total_banked < 0:
                print('Amount cannot be negative')
                continue
            break
        except ValueError:
            print('Invalid input. Use integers only. Try again.')
            continue

    return mpesa, cash, card, total_banked

def collect_branch_report():
    while True:
        branch = input('Input branch: ').capitalize()
        if branch not in branches:
            print('No such branch. Try again.')
            continue
        else:
            try:
                mpesa, cash, card, total_banked = amounts_verifications()
            except TypeError as t:
                print(f'Invalid input detected. Error "{t}" generated while unpacking tuple.')
            else:
                outcome ,value = reconcile(mpesa, cash, card, total_banked)

                return {'Branch': branch,
                        'Mpesa': mpesa,
                        'Cash': cash,
                        'Card': card,
                        'Total Banked': total_banked,
                        'Variance': value,
                        'Status': 'Underbanked⬇️' if value < 0 else 'Overbanked⬆️' if value > 0 else 'Reconciled✅'
                        }
        break

def display_reports():
    display = '=================SALES REPORTS=============\n'
    if not reports:
        display += '[No available reports]\n'
    else:
        for index, item in enumerate(reports):
            display += '---------------------------------\n'
            display += f'Report #{index+1}\n'
            display += '---------------------------------\n'
            display += (f'Branch: {item["Branch"]}\n'
                        f'Mpesa: {item["Mpesa"]}\n'
                        f'Cash: {item["Cash"]}\n'
                        f'Card: {item["Card"]}\n'
                        f'Total Banked: {item["Total Banked"]}\n'
                        f'Variance: {item["Variance"]}\n'
                        f'Status: {item["Status"]}\n')
    return display

def add_to_database():
    data = pandas.DataFrame(reports)
    data.to_csv('database.csv', index=False)

def display_report(branch_choice):
    display = '=====================================\n'
    for a_report in reports:
        if a_report['Branch'] == branch_choice:
            display += (f'Branch: {a_report["Branch"]}\n'
                        f'Mpesa: {a_report["Mpesa"]}\n'
                        f'Cash: {a_report["Cash"]}\n'
                        f'Card: {a_report["Card"]}\n'
                        f'Total Banked: {a_report["Total Banked"]}\n'
                        f'Variance: {a_report["Variance"]}\n'
                        f'Status: {a_report["Status"]}\n')
            display += '=====================================\n'

            return display
    print(f'{branch_choice} report not found in reports list.')
    return None

def search_report():
    while True:
        search = input('Enter branch name: ').capitalize()
        if search not in branches:
            print(f'No {search} branch. Try again.')
            continue

        if search in branches_added:
            return display_report(search)
        else:
            print(f'{search} report not found.')


def edit_report():
    while True:
        choice = input('Enter branch name: ').capitalize()
        if choice not in branches:
            print(f'No {choice} branch. Try again.')
            continue
        break
    try:
        if choice in branches_added:
            print('\n---Enter corrected category/categories amount(s)---\n')
            mpesa, cash, card, total_banked = amounts_verifications()
            outcome, value = reconcile(mpesa, cash, card, total_banked)
            for branch_report in reports:
                if branch_report['Branch'] == choice:
                    branch_report['Mpesa'] = mpesa
                    branch_report['Cash'] = cash
                    branch_report['Card'] = card
                    branch_report['Total Banked'] = total_banked
                    branch_report['Variance'] = value
                    branch_report['Status'] = 'Underbanked⬇️' if value < 0 else 'Overbanked⬆️' if value > 0 else 'Reconciled✅'
                print(f'{choice} report updated successfully.')
                add_to_database()
        else:
            print(f'{choice} report unavailable.')
    except TypeError as t:
        print(f'Invalid input detected. Error "{t}" generated while unpacking tuple.')

def delete_report():
    while True:
        choice = input('Enter branch name: ').capitalize()
        if choice not in branches:
            print(f'No {choice} branch. Try again.')
            continue
        break
    if choice in branches_added:
        print('Report found.')
        display_report(choice)
        choice2 = str(input('Report once deleted cannot be recovered. Are you sure you want to delete this report? y/n: ')).lower()
        if choice2 == 'y' or choice2 == 'yes':
             for branch_report in reports:
                reports.remove(branch_report)
             print(f'{choice} report deleted successfully.')
        elif choice2 == 'n' or choice2 == 'no':
            print(f'{choice} report not deleted.')
            pass
        else:
            print('Invalid input. Try again.')
    else:
        print(f'{choice} report unavailable.')

system_on = True
while system_on:
    time.sleep(3)
    print('----------------------SALES REPORT SYSTEM----------------------\n'
          '1. Add Report\n'
          '2. View Reports\n'
          '3. Search Report\n'
          '4. Edit Report\n'
          '5. Delete Report\n'
          '6. Exit\n')
    try:
        user_choice = int(input('Select an option: '))
    except ValueError:
        print('Invalid input. Use a number corresponding to the options provided.')

    else:
        if user_choice == 1:
            report = collect_branch_report()
            if isinstance(report, dict):
                if report['Branch'] in branches_added:
                    print(f'{report["Branch"]} report has already been added to the system.⚠️')
                else:
                    reports.append(report)
                    add_to_database()
                    print('Report successfully added! ✅')
                    branches_added.append(report['Branch'])
            else:
                continue
        elif user_choice == 2:
            print(display_reports())
        elif user_choice == 3:
            print(search_report())
        elif user_choice == 4:
            edit_report()
        elif user_choice == 5:
            delete_report()
        elif user_choice == 6:
            system_on = False
        else:
            print('Invalid input. Use a number corresponding to the options provided.')