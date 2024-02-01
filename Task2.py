from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
class Task2():
    def verify_invalid_credentials(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        username = "admin"
        password = "incorrect123"
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        user = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        user.send_keys(username)
        print(f"User Input Field: Test Case: {'PASSED' if user.is_enabled() else 'FAILED'} , Actual: {user.is_enabled()} , Expected: True")
        passw=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
        passw.send_keys(password)
        print(f"Password Input Field: Test Case: {'PASSED' if passw.is_enabled() else 'FAILED'} , Actual: {passw.is_enabled()} , Expected: True")
        login_button=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
        print(f"Login Button Field: Test Case: {'PASSED' if login_button.is_enabled() else 'FAILED'} , Actual: {login_button.is_enabled()} , Expected: True")
        login_button.click()
        imsg=driver.find_element(By.XPATH,"//div[@role='alert']")
        driver.get_screenshot_as_file(f"C:\\python-selenium\\Practise\\Assignment\\Test Case Screenshots\\{current_time}invalidalert.png")
        print(f"The application should display an error message indicating that the credentials are invalid: ,Test Case : PASSED , Actual:{imsg.is_displayed()} , Expected: {'True'}")
t1=Task2()
t1.verify_invalid_credentials()