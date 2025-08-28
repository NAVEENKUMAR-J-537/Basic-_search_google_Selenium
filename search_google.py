from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query, wait_time=3):
    # Start Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Google
    driver.get("https://www.google.com")
    time.sleep(2)

    # Accept cookies if prompted (optional)
    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(),'I agree')]")
        accept_button.click()
        time.sleep(1)
    except:
        pass

    # Find the search box and enter query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(wait_time)

    # Print first 5 search result titles
    results = driver.find_elements(By.XPATH, "//h3")[:5]
    print(f"Top 5 results for '{query}':")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result.text}")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    google_search("Selenium with Python")
