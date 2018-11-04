class CashMachine(object):
    def __init__(self):
        self._bills = []
        self.broken = False

    @property
    def is_available(self):
        return bool(self._bills)

    def put_money(self, bills):
        self._bills.extend(bills)

    def whitdraw_money(self, amount):
        bills_to_whitdraw = []
        for bill in sorted(self._bills, reverse=True):
            if sum(bills_to_whitdraw) + bill <= amount:
                bills_to_whitdraw.append(bill)
        if sum(bills_to_whitdraw) == amount:
            for bill in bills_to_whitdraw:
                self._bills.remove(bill)
            return bills_to_whitdraw
        return []


def test_CashMachine_not_availabel():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available


def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.whitdraw_money(150) == [100, 50]
    cash_machine.whitdraw_money(150) == []


def test_CashMachine_order_matter():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    cash_machine.whitdraw_money(100) == [50, 50]


def test_CashMachine_is_not_available():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 50])
    cash_machine.whitdraw_money(100) == [50, 50]
    assert not cash_machine.is_available

def test_CashMachine_is_not_broken():
        cash_machine = CashMachine()
        assert not cash_machine.broken
