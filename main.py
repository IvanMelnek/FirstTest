from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


#class MyListener(AbstractEventListener):

  #  def before_find(self, by, value, driver):
   #     print(by, value)
   # def after_find(self, by, value, driver):
   #     print(by, value, "found")
   # def on_exception(self, exception, driver):
   #     print(exception)



driver = webdriver.Chrome()
driver.get('https://infotouch.em70.ru/kiosk?id=14')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 30) # seconds
element = driver.find_elements_by_xpath("//a[@class='main-doc_category main-doc link']")

#txt = element1.get_attribute("textContent")
#print(txt," ",i)


j = 0
print("Валидные сылки:")
for element1 in element:
    elements = driver.find_elements_by_xpath("//a[@class='main-doc_category main-doc link']")
    txt = elements[j].get_attribute("textContent")
    elements[j].click()
    driver.back()
    j += 1
    print(txt)







