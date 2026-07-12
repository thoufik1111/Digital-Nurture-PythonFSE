"""
===========================================================
Hands-On 4
Selenium WebDriver Setup, Browser Drivers & Basic Commands
===========================================================

Selenium Components

1. WebDriver
- Controls the browser through browser drivers.
- Sends commands from Python to Chrome.

2. Selenium Grid
- Executes tests on multiple browsers and machines simultaneously.
- Used for parallel execution.

3. Selenium IDE
- Browser extension for recording and replaying test cases.
- Useful for beginners and quick automation.

Implicit Wait:
driver.implicitly_wait(10)

Implicit wait applies globally to every element lookup.
Although simple, it is generally discouraged because every
lookup waits unnecessarily. Explicit waits are more precise
and improve execution speed.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


# ----------------------------
# Headless Chrome
# ----------------------------

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.implicitly_wait(10)

# ----------------------------
# Task 1
# ----------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:")
print(driver.title)

# ----------------------------
# Task 2
# ----------------------------

driver.find_element(
    By.LINK_TEXT,
    "Simple Form Demo"
).click()

assert "simple-form-demo" in driver.current_url

print("URL Assertion Passed")

driver.back()

# ----------------------------
# Multiple Tabs
# ----------------------------

driver.execute_script(
    "window.open('https://www.google.com');"
)

print("\nWindow Handles:")

for handle in driver.window_handles:
    print(handle)

driver.switch_to.window(driver.window_handles[1])

print("\nGoogle Title:")
print(driver.title)

driver.switch_to.window(driver.window_handles[0])

print("Back to Playground")

result = driver.save_screenshot("playground_screenshot.png")

print("Screenshot Result:", result)

# ----------------------------
# Window Size
# ----------------------------

print("\nCurrent Window Size:")

print(driver.get_window_size())

driver.set_window_size(1280,800)

"""
Keeping a consistent browser window size ensures
responsive layouts behave consistently during
automation and avoids flaky UI tests.
"""

driver.close()

driver.quit()

print("\nAutomation Completed Successfully.")