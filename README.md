#Project Title

Upwork Scraper

#Description

Upwork Scraper is a Python script that allows you to scrape job details from Upwork.com. You can scrape job descriptions, titles, and reviews by providing a list of job links to the script. The script logs in to Upwork.com to access jobs that require authentication, and saves the scraped data to a JSON file.
<br>
Additionally, the project includes a second script that scans the freelancer reviews of a job and retrieves the name of the job poster. The project is a part of a client project and is designed to make job searching on Upwork.com more efficient.

#Installation

    Clone the repository:

bash

```git clone https://github.com/<username>/upwork-scraper.git```

    Install the dependencies:

```pip install -r requirements.txt```

    Create a .env file with your Upwork credentials:

```MAIL=<your email>
PASSWORD=<your password>```

    Provide a list of job links in job_links list in upwork_scraper.py.

#Usage

To use the script, simply run upwork_scraper.py. The script will automatically log in to Upwork.com and scrape job details for the provided links. The scraped data will be saved in a JSON file named data.json.

The get_job_poster.py script is used to scan freelancer reviews and retrieve the name of the job poster. To use this script, provide the URL of the job to be scanned as the argument. For example:

```python get_job_poster.py https://www.upwork.com/jobs/Sample-Job-Title~0123456789abcdef01
```
#License

This project is licensed under the MIT License.