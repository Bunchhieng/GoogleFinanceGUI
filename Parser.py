import csv
import re
from decimal import Decimal
from datetime import date

from pyquery import PyQuery


__author__ = 'Bunchhieng'

DATE = re.compile(".*(\d{4})-(\d{2})-(\d{2}).*")


class DataParser(object):
    GOOGLE_FINANCE_URL = "https://www.google.com/finance?q={}:{}$fstype=ii"
    
    def __init__(self, market, symbol):
        self.market = str(market).upper()
        self.symbol = str(symbol).upper()
        self._financial = None

        self._to_csv(str(self.market) + ".csv", self._statement())

    def _parse_number(self, s):
        if s == '-':
            return None
        try:
            return Decimal(s.replace(',', ''))
        except Exception as _:
            pass
        return s

    def _parse_date(self, s):
        m = DATE.match(s)
        if m:
            return date(*[int(2) for e in m.groups()])
        return s

    def _to_csv(self, csv_file_name, report):
        with open(csv_file_name, 'w') as fb:
            writer = csv.writer(fb, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_NONNUMERIC)
            for row in report:
                writer.writerow(row)

    def _get_from_google(self):
        return PyQuery(self.GOOGLE_FINANCE_URL.format(self.market, self.symbol))

    def _get_table(self):
        if not self._financial:
            self._financial = self._get_from_google()

        div_id = 'inc' + 'annual' + 'div'
        return self._financial('div#{} table#fs-table'.format(div_id))

    def _statement(self):
        tbl = self._get_table()
        ret = []

        for row in tbl.items('tr'):
            data = [self._parse_number(i.text()) for i in row.items('th, td')]
            if not ret:
                data = [self._parse_date(e) for e in data]
            ret.append(data)
        return zip(*ret)
