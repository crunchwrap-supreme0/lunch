from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium web driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.myschoolmenus.com/organizations/803/sites/6542/menus/30214')

# Wait for the element to load
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.menu-day-wrapper.today'))
)

# Get the contents of the element
contents = element.get_attribute('innerHTML')

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')

# Find all <p> elements with the role "button"
buttons = soup.find_all('p', {'role': 'button'})

# Extract the text of each <p> element
button_text = [button.text for button in buttons]

# Write the contents to a text file
with open('Lunch/menu.txt', 'w') as f:
    f.write('\n'.join(button_text))

# Close the web driver
driver.quit()
