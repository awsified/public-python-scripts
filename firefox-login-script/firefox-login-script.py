import time
from selenium import webdriver # See: https://crossbrowsertesting.com/blog/test-automation/automate-login-with-selenium/

# Download appropriate Selenium Driver and PATH it: 
# https://www.selenium.dev/downloads/

# This code will open the AWS account creation page and enter 
# some information. It will click the button, wait, and enter some
# more information at the captcha. Obviously this won't go through,
# it's only an example.

driver = webdriver.Firefox()
driver.get('https://portal.aws.amazon.com/billing/signup#/start')

pwstore = 'Fakepassword1!' # just so I don't have to type it twice.

# See: https://selenium-python.readthedocs.io/locating-elements.html
driver.find_element_by_id('ccEmail').send_keys('fakeemail@fakeemail.com')
driver.find_element_by_id("ccPassword").send_keys(pwstore)
driver.find_element_by_id('ccRePassword').send_keys(pwstore)
driver.find_element_by_id('ccUserName').send_keys('aws_account_name')
driver.find_element_by_name('submit').click() # Clicks submit
time.sleep(5)
driver.find_element_by_id('guess').send_keys('I AM NOT A ROBOT')
