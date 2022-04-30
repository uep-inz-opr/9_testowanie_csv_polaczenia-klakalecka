import csv
from unittest import TestCase
import requests


url = 'https://raw.githubusercontent.com/khashishin/repozytorium_z_plikiem_polaczenia/main/phoneCalls.csv'
r = requests.get(url, allow_redirects=True)
open('phoneCalls.csv', 'wb').write(r.content)


calls_sum_dict = dict()


class MenadzerPolaczen():
    def __init__(self, filename):
        self.filename = filename
        self.data_dict = self.read_data()

    def read_data(self):
        calls_sum_dict = dict()
        with open(self.filename, 'r') as fin:
            reader = csv.reader(fin, delimiter=",")  # comma is default delimiter
            headers = next(reader)

            for row in reader:
                from_subsr = int(row[0])
                if from_subsr not in calls_sum_dict:
                    calls_sum_dict[from_subsr] = 0
                calls_sum_dict[from_subsr] += 1
        return calls_sum_dict

    def pobierz_najczesciej_dzwoniacego(self):
        return max(self.data_dict.items(), key = lambda x: x[1])


class SprawdzDzwoniacegoTest(TestCase):
    def test_czy_abonent_najczesciej_dzwoniacy_rozponany_poprawnie(self):
        mp = MenadzerPolaczen("phoneCalls.csv")
        wynik = mp.pobierz_najczesciej_dzwoniacego()
        self.assertEqual((226,5), wynik)


if __name__ == '__main__':
    print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())


# unittest.main(argv=[''], defaultTest='SprawdzDzwoniacegoTest', exit=False)
