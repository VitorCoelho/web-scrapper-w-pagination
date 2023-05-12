# python-web-scrapper
This Python script performs web scraping to extract company data from a website and saves it in a CSV file. It uses the BeautifulSoup library for HTML parsing and requests library for making HTTP requests.

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.
3. Install the required Python dependencies by running the following command:

**pip install requests beautifulsoup4**

## Usage

1. Update the `url_base` variable in the code with the URL of the website's page containing the list of companies you want to scrape.
2. Run the Python script by executing the following command:

**python scrapper.py**


3. The script will start scraping the company data from each page and save it in a CSV file named `company.csv` in the same directory.

## Customization

- You can modify the CSV file name and the fields being extracted by editing the `csv_writer.writerow()` statement in the code.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
