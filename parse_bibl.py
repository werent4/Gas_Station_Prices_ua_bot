from bs4 import BeautifulSoup
import requests
import json

def write_json(refueling_array):
    '''Записовает данные о заправках в json файл'''

    with open('refueling_data','w') as r_d:
        json.dump(refueling_array, r_d, indent=4, ensure_ascii= False)



def parse_refueling(gas_station_name):
    '''Получает название и цени на бензин  выбрной заправки'''

    r = requests.get(url='https://auto.ria.com/uk/toplivo/'+ gas_station_name)

    soup = BeautifulSoup(r.text, 'html.parser')

    fuel_list = soup.find('div', class_='table size16 fuel-table-common').find_all('div', class_='t-row')

    fuel_list.pop(0)

    refueling_array = {}
    key = 0

    for fuel_name in fuel_list:
        key += 1
        title = fuel_name.find('div',class_='t-cell').get_text(strip=True)
        price = fuel_name.find('div', class_='t-cell bold size18').text.strip()

        refueling_array[key]={
            'title':title,
            'price':price
        }

        write_json(refueling_array=refueling_array,)