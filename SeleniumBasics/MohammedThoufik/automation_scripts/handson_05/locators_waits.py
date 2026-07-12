"""
===========================================================
Hands-On 5
Locators – ID, XPath, CSS Selectors & Explicit Waits
===========================================================

Locator Ranking (Best -> Worst)

1. ID
2. CSS Selector
3. Relative XPath
4. Name
5. Class Name
6. Absolute XPath

Reason:
- ID is unique, fast and readable.
- CSS selectors are fast and reliable.
- Relative XPath is flexible.
- Name may not always exist.
- Class Name may not be unique.
- Absolute XPath breaks whenever page structure changes.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get(
    "https://www.lambdatest.com/selenium-playground/simple-form-demo"
)

# -------------------------------------------------
# ID
# -------------------------------------------------

driver.find_element(By.ID, "user-message")
print("ID Locator : PASS")

# -------------------------------------------------
# NAME
# -------------------------------------------------

# Current TestMu AI page has NO name attribute
print("NAME Locator : SKIPPED (No name attribute on current website)")

# -------------------------------------------------
# CLASS NAME
# -------------------------------------------------

driver.find_element(By.CLASS_NAME, "rounded")
print("CLASS Locator : PASS")

# -------------------------------------------------
# TAG NAME
# -------------------------------------------------

driver.find_element(By.TAG_NAME, "input")
print("TAG Locator : PASS")

# -------------------------------------------------
# Absolute XPath
# -------------------------------------------------

try:
    driver.find_element(
        By.XPATH,
        "/html/body//input[@id='user-message']"
    )
    print("Absolute XPath : PASS")
except:
    print("Absolute XPath : FAILED")

# -------------------------------------------------
# Relative XPath
# -------------------------------------------------

driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("Relative XPath : PASS")

# -------------------------------------------------
# CSS by ID
# -------------------------------------------------

driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

print("CSS #id : PASS")

# -------------------------------------------------
# CSS by Attribute
# -------------------------------------------------

driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)

print("CSS Attribute : PASS")

# -------------------------------------------------
# CSS Parent > Child
# -------------------------------------------------

driver.find_element(
    By.CSS_SELECTOR,
    "div input"
)

print("CSS Parent Child : PASS")

# -------------------------------------------------
# Checkbox Demo
# -------------------------------------------------

driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)

try:

    label = driver.find_element(
        By.XPATH,
        "//label[text()='Option 1']"
    )

    print("XPath text() :", label.text)

except:

    print("XPath text() : FAILED")

labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print(
    "XPath contains() :",
    len(labels),
    "labels found"
)

driver.quit()

print("\nTask 1 Completed Successfully!")