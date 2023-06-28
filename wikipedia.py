import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#DANE TESTOWE

user_name = "MartaKwiat1989"
incorrect_password = "qwt123K!"
correct_password = "wsb1@!KqZ"

class FirstTest(unittest.TestCase):
    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://pl.wikipedia.org")
        self.driver.implicitly_wait(10)
        
    def test_incorrect_login(self):
        #kliknij "zaloguj się"
        login_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zaloguj się")
        login_link.click()
    

        user_name_element = self.driver.find_element(By.ID, "wpName1")
        user_name_element.clear()

        user_name_element.send_keys(user_name)

        user_password = self.driver.find_element(By.NAME, "wpPassword")
        user_password.send_keys(incorrect_password)
        
        logout_checkbox = self.driver.find_element(By.ID, "wpRemember")
        logout_checkbox.click()

        login_button = self.driver.find_element(By.ID, "wpLoginAttempt")
        login_button.click()
        
        self.driver.save_screenshot('screenshot-testcase1.png')
        
        #Oczekiwany rezultat
        #1. Użytkownik otrzymuje komunikat „Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz."
        
        user_error_message = self.driver.find_elements(By.XPATH, '//div[@class="mw-message-box-error mw-message-box"]')
        #Sprawdzam, czy liczba komunikatów o błędzie wynosi 1
        self.assertEqual(1, len(user_error_message))
        #Sprawdzam, czy treść komunikatu jest widoczna i brzmi "Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz."
        self.assertEqual("Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.", user_error_message[0].text)
        
        sleep(3)

    def test_no_password(self):
        #kliknij "zaloguj się"
        login_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zaloguj się")
        login_link.click()
    

        user_name_element = self.driver.find_element(By.ID, "wpName1")
        user_name_element.clear()

        user_name_element.send_keys(user_name)
        
        logout_checkbox = self.driver.find_element(By.ID, "wpRemember")
        logout_checkbox.click()

        login_button = self.driver.find_element(By.ID, "wpLoginAttempt")
        login_button.click()
        
        self.driver.save_screenshot('screenshot-testcase2.png')
        
        #Oczekiwany rezultat
        #Użytkownik otrzymuje komunikat „Wypełnij to pole" pod hasłem
        #nie można spr.czy komunikat się wyświetlil wiec jest screenshot
        
        #pole hasło jest puste
        
        password_element = self.driver.find_element(By.NAME, "wpPassword") 
        
        self.assertEquals(password_element.text, '') 
        
        login_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zaloguj się") 
        
        self.assertTrue(login_element)

        sleep(3)
        
    def test_correct_login(self):

        login_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zaloguj się")
        login_link.click()
    

        user_name_element = self.driver.find_element(By.ID, "wpName1")
        user_name_element.clear()

        user_name_element.send_keys(user_name)

        user_password = self.driver.find_element(By.NAME, "wpPassword")
        user_password.send_keys(correct_password)
        
        logout_checkbox = self.driver.find_element(By.ID, "wpRemember")
        logout_checkbox.click()

        login_button = self.driver.find_element(By.ID, "wpLoginAttempt")
        login_button.click()
        
        self.driver.save_screenshot('screenshot-testcase3.png')

        #Oczekiwany rezultat
        #Sprawdzam, czy nazwa użytkownika jest widoczna i brzmi "MartaKwiat1989"
        
        user = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MartaKwiat1989")
        
        self.assertEqual("MartaKwiat1989", user.text)

        sleep (3)
        
        
    #driver.quit() wyłączanie przeglądarki po każdym teście     
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    # Uruchom testy
    unittest.main(verbosity=2)
