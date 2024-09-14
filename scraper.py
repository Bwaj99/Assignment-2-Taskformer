import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import openai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Set up Google Sheets API authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('your.json', scope) #credentials.json
client = gspread.authorize(creds)

# Open the Google Sheet using its ID
spreadsheet_id = 'yourlink'  # Extracted from your Google Sheets link
sheet = client.open_by_key(spreadsheet_id).sheet1  # Opening the first sheet
linkedin_links = sheet.col_values(1)  # Assuming LinkedIn links are in the first column

# Set up the webdriver (Make sure you have the appropriate ChromeDriver version installed)
service = Service('/usr/local/bin/chromedriver')  # Include your chromedriver path
driver = webdriver.Chrome(service=service)

# Open LinkedIn and log in
driver.get('https://www.linkedin.com/login')
time.sleep(2)

# Enter your LinkedIn username and password
username = driver.find_element(By.ID, 'username')
username.send_keys('yourname')  # Insert your email
password = driver.find_element(By.ID, 'password')
password.send_keys('yourpassword')  # Insert your password

# Click the login button
login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
login_button.click()
time.sleep(3)

# Set up OpenAI API key
openai.api_key = "insert_open_api_key"

# Email sender details
sender_email = "youremail@example.com"
sender_password = "yourpassword"

# Email SMTP setup (example with Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Loop through the LinkedIn profile links and scrape data
for profile_url in linkedin_links:
    driver.get(profile_url)
    time.sleep(3)

    try:
        # Scrape name, headline, company, and email address
        name = driver.find_element(By.XPATH, '//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]').text
        headline = driver.find_element(By.XPATH, '//div[@class="text-body-medium break-words"]').text
        company = driver.find_element(By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/ul/li[1]/button').text

        # Scrape email (You need to find a reliable way to get the email from LinkedIn, depending on its structure)
        email = driver.find_element(By.XPATH, '//a[contains(@href, "mailto:")]').text

        # Generate personalized outreach message using OpenAI
        prompt = f"Write a personalized cold outreach message to {name} who works at {company} as {headline}. The goal is to introduce Taskformer, a business automation tool, and schedule a demo."
        
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Write a personalized cold outreach message to {name} who works at {company} as {headline}. The goal is to introduce Taskformer, a business automation tool, and schedule a demo."
                }
            ]
        )

        outreach_message = chat_completion['choices'][0]['message']['content'].strip()

        # Create email content
        subject = f"Let's Schedule a Demo for Taskformer, {name}"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(outreach_message, 'plain'))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())

        # Print confirmation
        print(f"Email sent to {name} at {email}\n")

    except Exception as e:
        print(f"Error scraping {profile_url}: {e}")

# Close the driver
driver.quit()
