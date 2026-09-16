class SalesReport:
    def __init__(self, branch, mpesa, cash, card, total_banked):
        self.branch = branch
        self.mpesa = mpesa
        self.cash = cash
        self.card = card
        self.total_banked = total_banked
        self.status = None
        self.variance = None
        self.total_sales = None

        self.calculate_totals()


    def calculate_totals(self):
        total_sales = self.mpesa + self.cash + self.card
        variance = self.total_banked - total_sales
        status = 'Underbanked⬇️' if variance < 0 else 'Overbanked⬆️' if variance > 0 else 'Reconciled✅'
        self.total_sales = total_sales
        self.variance = variance
        self.status = status

class ReconciliationSystem:
    VALID_BRANCHES = ['Nairobi', 'Karen', 'Kisumu', 'Kakamega', 'Rongai', 'Nakuru','Mombasa']
    def __init__(self):
        self.reports = []

    def validate_branch(self, prompt):
        while True:
            branch = input(prompt).capitalize()
            if branch not in self.VALID_BRANCHES:
                print(f'{branch} is not a valid branch.')
                continue

            return branch

    def find_report(self, branch_name):
        for report in self.reports:
            if report.branch == branch_name:
                return report
        return None

    def add_report(self, report):
        if self.find_report(report.branch) is not None:
                return f'{report.branch} report already in the system.'

        self.reports.append(report)
        return f'{report.branch} report added successfully.'

    def display_all_reports(self):
        display = '..................BRANCH SALES REPORTS....................\n'
        if not self.reports:
            display += '[No available reports]'
        else:
            for report in self.reports:
                display += (f'Branch: {report.branch}\n'
                        f'Mpesa: {report.mpesa}\n'
                        f'Cash: {report.cash}\n'
                        f'Card: {report.card}\n'
                        f'Total Banked: {report.total_banked}\n'
                        f'Variance: {report.variance}\n'
                        f'Status: {report.status}\n')
                display += '-------------------------------------\n'
        return display

    def display_one_report(self):
        branch_name = self.validate_branch('Branch name: ')
        report = self.find_report(branch_name)
        if report is None:
            return f'{branch_name} report not found in reports list.'
        display = '******************************\n'
        display += (f'Branch: {report.branch}\n'
                    f'Mpesa: {report.mpesa}\n'
                    f'Cash: {report.cash}\n'
                    f'Card: {report.card}\n'
                    f'Total Banked: {report.total_banked}\n'
                    f'Variance: {report.variance}\n'
                    f'Status: {report.status}\n')
        display += '******************************\n'

        return display

    def edit_report(self):
        branch_name = self.validate_branch('Branch name: ')
        report = self.find_report(branch_name)
        if report is None:
            return f'{branch_name} report not found in reports list.'

        report.mpesa = validate_amount('Mpesa amount: ')
        report.cash = validate_amount('Cash amount: ')
        report.card = validate_amount('Card amount: ')
        report.total_banked = validate_amount('Total banked: ')

        report.calculate_totals()
        return f'{branch_name} report updated successfully.'

    def delete_report(self):
        branch_name = self.validate_branch('Branch name: ')
        report = self.find_report(branch_name)
        if report is None:
            return f'{branch_name} report not found in reports list.'
        while True:
            pick = str(input('Report once deleted cannot be recovered. Are you sure you want to delete this report? y/n: ')).lower()
            if pick == 'y' or pick == 'yes':
                    self.reports.remove(report)
                    return f'{report.branch} report deleted successfully.'
            elif pick == 'n' or pick == 'no':
                return f'{report.branch} report not deleted.'
            else:
                print('Invalid input. Please enter y or n')

def validate_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print(f'"{prompt}" cannot be a negative value.')
                continue
            return amount
        except ValueError:
            print(f'"{prompt}" must be a number')
            continue

def collect_branch_report(a_system):
    branch = a_system.validate_branch('Branch name: ')
    mpesa = validate_amount('Mpesa amount: ')
    cash = validate_amount('Cash amount: ')
    card = validate_amount('Card amount: ')
    total_banked = validate_amount('Total banked: ')

    report = SalesReport(branch, mpesa, cash, card, total_banked)

    return report

system = ReconciliationSystem()

running = True

while running:
    print('----------------------SALES REPORT SYSTEM----------------------\n'
          '1. Add Report\n'
          '2. View Reports\n'
          '3. Search Report\n'
          '4. Edit Report\n'
          '5. Delete Report\n'
          '6. Exit\n')
    while True:
        try:
            choice = int(input('Select an option: '))
        except ValueError:
            print('Invalid input. Use a number corresponding to the options provided.')
            continue
        else:
            if choice == 1:
                branch_report = collect_branch_report(system)
                print(system.add_report(branch_report))
                break
            elif choice == 2:
                print(system.display_all_reports())
                break
            elif choice == 3:
                print(system.display_one_report())
                break
            elif choice == 4:
                print(system.edit_report())
                break
            elif choice == 5:
                print(system.delete_report())
                break
            elif choice == 6:
                print('Goodbye!')
                running = False
                break
            else:
                print('Invalid choice. Please try again.')
                continue