import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mcmakler.de/immobilienpreise/nordrhein-westfalen/duesseldorf?address=&center=6.808027422858231%2C51.21474386826614&zoom=1"

driver = webdriver.Chrome()
driver.get(url)

# The problem was that there was a button on the website. This had to be clicked several times for the table to load completely.
# The solution here was Selenium. This library can automate web applications. This is how the website is opened via google chrome and the "mehr" button is clicked.
while True:
    try:
        mehr_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Mehr')]")))
        mehr_button.click()
    except:
        break

html_text = driver.page_source
soup = BeautifulSoup(html_text, "html.parser")

tables = soup.find_all("table")
for i, table in enumerate(tables):
    df = pd.read_html(str(table))[0]
    df[['Stadtteil', 'Ø Mietpreis (€/m²)']].to_csv(f"table_{i}.csv", index=False, header=False)

driver.quit()

# In the end we have extract the table. The problem was that both columns were output. Since we had problems with the comma being recognized as a separator, we simply deleted the values
# because we wanted to deal with the next problems first. In the future, this code will be updated so that the table is output correctly

