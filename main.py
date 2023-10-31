from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
list_email = ['hoxuanthinh68@gmail.com', 'hoxuanthinh728@gmail.com','hoxuanthinh78@gma2il.com','hoxuanthin2h78@gmail.com','hoxuan2thinh78@gmail.com','hoxuanthin2h78@gmail.com','hoxuanthinh782@gmail.com','hoxuanthinh78@gmail.com','hoxuanthin2h78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh68@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com', 'hoxuanthinh12@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh68@gmail.com', 'hoxuanthinh78@gmail.com', 'hoxuanthinh12@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com','hoxuanthinh78@gmail.com']
def check_login( ):
    chrome_options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/95.0.4638.69 Safari/537.36"
    chrome_options.add_argument(f'user-agent={user_agent}')
    # chrome_options.add_argument("--headless")
    try:
        driver = webdriver.Chrome()
        driver.get("https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F")
        number = 0
        driver.implicitly_wait(20)
        for i in list_email:
            driver.find_element(By.ID, "userid").clear()
            driver.find_element(By.ID, "userid").send_keys(i)
            driver.find_element(By.ID, "signin-continue-btn").click()
            # wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây
            # element = wait.until(EC.presence_of_element_located((By.ID, "signin-error-msg")))
            time.sleep(1)
            try:
                # element = driver.find_element(By.ID, "signin-error-msg")
                soup = BeautifulSoup(driver.page_source, 'lxml')
                text = soup.find("p", id = "errormsg")
                if text is None:
                    time.sleep(1)
                    print(f"{i}: Tài khoản tồn tại")
                    driver.find_element(By.ID, "switch-account-anchor").click()
                else:
                    print(f"{i}: {text.text}")
                number += 1
                print(str(number))
            except Exception as ex:
                print(ex)



        # boxmess = driver.find_element(By.ID, "errormsg").text
        # print(email+" : " + element.text)
        driver.quit()
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    try:
        start = time.time()
        for i in range (3):
            list_email += list_email
        print(len(list_email))
        check_login()

        # with ThreadPoolExecutor(max_workers = 4) as executor:
        #     for i in list_email:
        #         executor.submit(check_login,i)
        print("end time: " + str(time.time() - start))
    except Exception as ex:
        print(ex)
# import time
# from seleniumbase import SB
# from bs4 import BeautifulSoup
# def verify_success(sb):
#     sb.assert_element('img[alt="Logo Assembly"]', timeout=8)
#     sb.sleep(4)
#
# with SB(uc_cdp=True, guest_mode=True ) as sb:
#
#     sb.open("https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F")
#     time.sleep(10)
#     soup = BeautifulSoup(sb.get_page_source(), 'lxml')
#     print(soup)
#     print(soup.find("div", "checkbox"))
#     time.sleep(100)
#     sb.click('')
    # try:
    #     verify_success(sb)
    # except Exception:
    #     if sb.is_element_visible('input[value*="Verify"]'):
    #         sb.click('input[value*="Verify"]')
    #     elif sb.is_element_visible('iframe[title*="challenge"]'):
    #         sb.switch_to_frame('iframe[title*="challenge"]')
    #         sb.click("span.mark")
    #     else:
    #         raise Exception("Detected!")
    #     try:
    #         verify_success(sb)
    #     except Exception:
    #         raise Exception("Detected!")
    # finally:
    #     soup = BeautifulSoup(sb.get_page_source(), 'lxml')
    #     i1 = soup.find('div',"reading-content")
    #     print(i1.find_all("img")[0]['src'])
