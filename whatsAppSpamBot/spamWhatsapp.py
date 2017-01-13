#selenium works on websites, so to use this script you have to sign into whatsapp web (QR code)
#you may have to install selenium as well:
#pip install selenium

from selenium import webdriver
b = webdriver.Firefox() #have to check browser compatibility
b.get('https://web.whatsapp.com') #https ?
input()
elem = b.find_element_by_xpath('//span[contains(text(), "mat")]') 
elem.click()
elemTextbox = b.find_elements_by_class_name('input')
i = 0
while i < 5:
    elemTextbox[1].send_keys('test')
    b.find_element_by_class_name('send-container').click()

### I need to fix this, this at the moment does not work