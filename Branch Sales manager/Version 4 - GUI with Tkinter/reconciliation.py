import json
from json import JSONDecodeError

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
    def to_dict(self):

        return {
            'branch': self.branch,
            'mpesa': self.mpesa,
            'cash': self.cash,
            'card': self.card,
            'total_banked': self.total_banked
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['branch'],
            data['mpesa'],
            data['cash'],
            data['card'],
            data['total_banked']
        )

class ReconciliationSystem:
    VALID_BRANCHES = ['Nairobi', 'Karen', 'Kisumu', 'Kakamega', 'Rongai', 'Nakuru','Mombasa', 'Kisii', 'Narok', 'Kiserian', 'Embu', 'Meru', 'Marsabit', 'Kitale', 'Kitengela', 'Busia']
    def __init__(self):
        self.reports = []
        self.load_reports()
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
        self.save_reports()
        return f'{report.branch} report added successfully.'
    def delete_report(self, report):
        self.reports.remove(report)
        self.save_reports()

    def save_reports(self):
        dict_reports = [report.to_dict() for report in self.reports]
        with open('reports.json', 'w') as f:
            json.dump(dict_reports, f, indent=4)

    def load_reports(self):
        try:
            with open('reports.json', 'r') as f:
                report_data = json.load(f)
        except FileNotFoundError:
            return
        except JSONDecodeError:
            return
        else:
            for report_dict in report_data:
                self.reports.append(SalesReport.from_dict(report_dict))


def validate_amount(value):
    try:
        amount = float(value)
        if amount < 0:
            return None
        return amount
    except ValueError:
        return None




