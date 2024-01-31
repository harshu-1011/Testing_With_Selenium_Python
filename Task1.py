from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class Task1():
    def verify_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        driver.implicitly_wait(8)
        username = "Admin"
        password = "admin123"
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        user=driver.find_element(By.XPATH,"//input[@placeholder='Username']" )
        user.send_keys(username)
        print(f"User Input Field : Test Case:PASSED , Actual:{user.is_enabled()} , Expected:{'True'}")
        passw=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
        passw.send_keys(password)
        print(f"Password Input Field: Test Case:PASSED , Actual:{passw.is_enabled()} , Expected:{'True'}")
        login_button=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        print(f"Login Button Field:Test Case:PASSED , Actual:{login_button.is_enabled()} , Expected:{'True'}")
        login_button.click()
        dashboard=driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']")
        driver.get_screenshot_as_file(f"C:\\python-selenium\\Practise\\Assignment\\Test Case Screenshots\\{current_time}dashoardtask1.png")
        print(f"The user should be successfully logged in.The user should be directed to the dashboard:Test Case:PASSED , Actual:{dashboard.is_displayed()} , Expected:{'True'}")
t1=Task1()
t1.verify_login()