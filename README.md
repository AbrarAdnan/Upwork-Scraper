# Project Title

Upwork Scraper

# Description

Upwork Scraper is a Python script that allows you to scrape job details from Upwork.com. You can scrape job descriptions, titles, skills and experties and reviews by providing a list of job links to the script. The script logs in to Upwork.com to access jobs that require authentication, and saves the scraped data to a JSON file.
<br>
Additionally, the project includes a second script that scans the freelancer reviews of a job and retrieves the name of the job poster. The project is a part of a client project and is designed to make job searching on Upwork.com more efficient.

# Installation

1. Clone the repository:



```bash
git clone https://github.com/AbrarAdnan/Upwork-Scraper.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file with your Upwork credentials:

```
MAIL=<your email>
PASSWORD=<your password>
```

4. Provide a list of job links in job_links list in scraper.py.

# Usage

Before running the script, you must have the following:

- Python 3.x installed
- `pip` package manager
- `dotenv` package installed
- Firefox browser installed

To use the script, simply run 
```bash
scraper.py
```
The script will automatically log in to Upwork.com and scrape job details for the provided links. The scraped data will be saved in a JSON file named data.json.

The get_job_poster.py script is used to scan freelancer reviews in the json files and retrieve the name of the job poster. To use this script run it in the following way:

```bash
python get_client_name.py
```

## Contributing

Contributions are welcome! If you find any issues or want to suggest new features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
