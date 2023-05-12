import requests
import re
import json
import csv
from bs4 import BeautifulSoup

# Change the URL for the page that has a list of companies
url_base = 'https://github.com/company/page-here'

# Makes a initial request to get the total number of pages
response = requests.get(url_base)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
num_paginas_text = soup.find('span', text=re.compile(r'de \d+')).text
num_paginas = int(re.search(r'\d+', num_paginas_text).group())

# Opens the CSV file to write
csv_file = open('company.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Nome', 'Descrição', 'Endereço', 'Código Postal', 'Localidade', 'Região', 'País', 'Telefone'])

# Loop to run all of the paginations
for pagina in range(1, num_paginas + 1):
    url = f'{url_base}/{pagina}'  # Updates the URL with the number of the page
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    companies_scripts = soup.find_all('script', type='application/ld+json')

    for script in companies_scripts:
        data = json.loads(script.text)

        # Verifies if the JSON object is a company
        if isinstance(data, list):
            for company in data:
                if company.get('@type') == 'LocalBusiness':
                    name = company['name']
                    description = company['description']
                    address = company['address']['streetAddress']
                    zip_code = company['address']['postalCode']
                    locality = company['address']['addressLocality']
                    state = company['address']['addressRegion']
                    country = company['address']['addressCountry']
                    phone = company['telephone']

                    # Writes the data on the CSV file
                    csv_writer.writerow([name, description, address, zip_code, locality, state, country, phone])

# Closes the CSV file
csv_file.close()
