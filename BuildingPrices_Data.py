import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mcmakler.de/immobilienpreise/nordrhein-westfalen/duesseldorf?address=&center=6.808027422858231%2C51.21474386826614&zoom=1"

# Start a selenium session
driver = webdriver.Chrome()
driver.get(url)

# Wait for the "Mehr" button to be visible and then click it until all data is loaded
while True:
    try:
        # Wait for the "Mehr" button to be visible
        mehr_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Mehr')]")))
        # Click the "Mehr" button to load more data
        mehr_button.click()
    except:
        # Stop the loop when there are no more "Mehr" buttons to click
        break

# Extract the HTML of the table
html_text = driver.page_source
soup = BeautifulSoup(html_text, "html.parser")

# Extract the table and convert it to a pandas dataframe
tables = soup.find_all("table")
for i, table in enumerate(tables):
    df = pd.read_html(str(table))[0]
    filename = f"table_{i}.csv"
    df.to_csv(filename, index=False)

# Close the selenium session
driver.quit()

