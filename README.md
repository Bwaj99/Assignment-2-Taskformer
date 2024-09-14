# LinkedIn Scraper & Automated Cold Outreach System

This project automates the process of scraping LinkedIn profiles from a Google Sheet, generating personalized cold outreach messages using OpenAI, and sending the outreach messages via email. The primary goal is to introduce a business automation tool, Taskformer, and schedule a demo with potential clients.

## Features

- Scrapes LinkedIn profile information such as name, headline, company, and email.
- Generates personalized cold outreach messages using OpenAI's GPT-3.5-turbo model.
- Automates email delivery with the generated message.
- Integrates with Google Sheets API to extract LinkedIn profile URLs.

## Prerequisites

Before running this project, you must have the following set up:

1. **Google Sheets API Credentials**:
   - Enable the Google Sheets API and generate a `credentials.json` file from the Google Cloud Platform.
   - Place the JSON file in the root directory of your project.

2. **Selenium WebDriver**:
   - Download and install the appropriate ChromeDriver version for your system.
   - Ensure the path to the ChromeDriver is set correctly in the script.

3. **OpenAI API Key**:
   - Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys) and insert it in the script.

4. **SMTP Server**:
   - Set up an email account (e.g., Gmail) with SMTP enabled to send automated emails.
   - If using Gmail, make sure to allow less secure apps or use OAuth2 for more secure authentication.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bwaj99/Assignment-2-Taskformer
   cd linkedin-outreach
2. **Install required dependencies**:
   You can install the required Python libraries by running the following command:
   ```bash
   pip install -r requirements.txt
3. **Create Google Sheets API credentials**:
   - Follow [this guide](https://developers.google.com/sheets/api/quickstart/python) to set up your Google Sheets API credentials.
   - Place your credentials JSON file in the project root and update the script to reference it.
4. **Configure environment variables**:
   Create a `.env` file or update the script with your credentials and API keys:
   - OpenAI API key
   - Email account (SMTP) credentials
   - Google Sheets credentials
5. **Configure ChromeDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Add the correct ChromeDriver path to your script.

## Configuration

Before running the script, make sure you replace the following placeholders in the script:

- `your.json` - Path to your Google Sheets API credentials JSON file.
- `yourlink` - The ID of your Google Sheets document containing LinkedIn profile URLs.
- `yourname` - Your LinkedIn email address.
- `yourpassword` - Your LinkedIn password.
- `insert_open_api_key` - Your OpenAI API key.
- `youremail@example.com` - Your email address for sending the outreach.
- `yourpassword` - Your email account password for SMTP.

## How to Run

1. **Run the script**:
   Once all configuration steps are completed, you can run the script using Python:
   ```bash
   python linkedin_outreach.py
   ```

2. **Output**:
   - The script will scrape LinkedIn profiles, generate a personalized outreach message, and send an email to the respective contact.

## Troubleshooting

1. **Email not sending**: 
   - Ensure that the SMTP server details are correct and that your email provider allows automated emails.
   - For Gmail, enable "Less secure apps" if you're using a password-based SMTP login, or use OAuth2 for better security.

2. **LinkedIn scraping issues**:
   - LinkedIn may block automated scraping or require you to handle Captchas.
   - If email scraping is not working, check that the XPath used in the script matches LinkedIn’s structure.

3. **Google Sheets API issues**:
   - Ensure that your Google Sheets API credentials are correct and the spreadsheet link is properly referenced in the script.



### Steps to Implement:

1. **Create a file** named `README.md` in your project directory.
2. **Copy and paste the above content** into the file.
3. Adjust the repository link and any other placeholders as necessary.

This README file gives an overview of the project, installation steps, prerequisites, how to run the script, and troubleshooting tips.






