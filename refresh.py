from selenium import webdriver
from selenium.webdriver.common.keys import Keys

psnID # = 'insert PSN ID here'
driver = webdriver.PhantomJS()
driver.get('http://www.psnprofiles.com')
assert 'PSNProfiles' in driver.title
elem = driver.find_element_by_id('psnId')
elem.send_keys(psnID + Keys.RETURN)
driver.quit()