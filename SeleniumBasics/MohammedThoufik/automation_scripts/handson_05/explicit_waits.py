import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get(
    "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
)

# -------------------------------------------------------
# Explicit Wait Demo
# -------------------------------------------------------

start = time.time()

button = WebDriverWait(driver,10).until(

    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            ".btn-success-manual"
        )
    )

)

button.click()

alert = WebDriverWait(driver,10).until(

    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            ".alert-success-manual"
        )
    )

)

assert "normal success message" in alert.text.lower()

end = time.time()

print("------------------------------------")
print("Explicit Wait Passed")
print("Alert Text :", alert.text)
print("Execution Time :", round(end-start,2),"seconds")

# -------------------------------------------------------
# Clickable Demo
# -------------------------------------------------------

button = WebDriverWait(driver,10).until(

    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            ".btn-success-manual"
        )
    )

)

print("Button is Clickable")

# -------------------------------------------------------
# Fluent Wait
# -------------------------------------------------------

fluent_wait = WebDriverWait(

    driver,

    timeout=10,

    poll_frequency=0.5,

    ignored_exceptions=[NoSuchElementException]

)

print("Fluent Wait Configured Successfully")

driver.quit()

print("\nTask 2 Completed Successfully")