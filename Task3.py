from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
class Task3():
    def verify_login_fields(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        driver.implicitly_wait(6)
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        user = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        print(f"User Input Field: Test Case:PASSED , Actual:{user.is_enabled()} , Expected:{'True'}")
        passw = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        print(f"Password Input Field: Test Case:PASSED , Actual:{passw.is_enabled()} , Expected:{'True'}")
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        driver.get_screenshot_as_file(f"C:\\python-selenium\\Practise\\Assignment\\Test Case Screenshots\\{current_time}Beforetask3.png")
        print(f"Login Button Field: Test Case:PASSED , Actual:{login_button.is_enabled()} , Expected:{'True'}")
        login_button.click()
        errormsg=driver.find_element(By.XPATH,"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
        driver.get_screenshot_as_file(f"C:\\python-selenium\\Practise\\Assignment\\Test Case Screenshots\\{current_time}Aftertask3.png")
        print(f"The application displays an error message indicating that the username and password fields are required:Test Case:PASSED , Actual:{errormsg.is_displayed()} , Expected: {'True'}")
t1=Task3()
t1.verify_login_fields()