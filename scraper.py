from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time, json, os

load_dotenv()

mail = os.getenv("MAIL")
password = os.getenv("PASSWORD")

job_links = [
    ''
]

def expand_review(driver):
    # Click show all to get the full list of reviews
    while True:
        more_btn = driver.find_elements(By.CLASS_NAME,'js-show-more')
        if more_btn:
            more_btn[0].click()
        else:
            break
    print('review list expanded')
    # Click more to get the full length of reviews
    more_btn = driver.find_elements(By.CLASS_NAME,'up-truncation-label')
    for i in range(0, len(more_btn)):
        btn = more_btn[i].text
        if(btn=='more'):
            more_btn[i].click()
    print('review expanded')

def remove_popup(driver):
    print('removing popup')
    try:
        #popup_exit_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/button')
        popup_exit_btn = driver.find_element(By.CSS_SELECTOR,'button.up-btn-primary:nth-child(2)')
        popup_exit_btn.click()
        print('popup blocked')
    except Exception as e:
        print('no popups')

# new data function for client
def get_data(driver, job_link):
    print('scraping data from : '+job_link)
    # driver.get(job_link)
    # time.sleep(10)
    try:
        driver.get(job_link)
        # Wait for the page to load for a maximum of 5 seconds
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/header/div/div[1]/div/a/span[2]/svg")))
    except:
        print("Page loaded by timeout of 10 seconds")
    remove_popup(driver)
    time.sleep(1)

    #     Get the skills
    try:
        skills_element_temp = driver.find_element(By.XPATH,"//section[@class='up-card-section']//h4[contains(text(), 'Skills and Expertise')]")
        skills_element = skills_element_temp.find_element(By.XPATH, "..")
        skills = skills_element.find_elements(By.TAG_NAME,'a')
        skill_list = []
        for skill in skills:
            skill_list.append(skill.text)
    #         print(skill.text)
        expertise = ', '.join(skill_list)
    except:
        expertise = 'ERROR'
        print('error getting skills')
    time.sleep(1)

    try:
        job_title_element = driver.find_element(By.CSS_SELECTOR,'.my-0')
        job_title = job_title_element.text
    except:
        print('error getting job title')
        job_title = 'ERROR'
    try:
        description_element = driver.find_element(By.CSS_SELECTOR,'.job-description > div:nth-child(1)')
        description = description_element.text
    except:
        description = 'ERROR'
        print('error getting description')
    expand_review(driver)
    
    # Get the reviews in a list
    try:
        review_section = driver.find_element(By.CSS_SELECTOR,'.js-jobs')
        review_body = review_section.find_elements(By.CLASS_NAME,'mt-5')
        review_list = []
        for i in range(0, len(review_body), 2):
            #print(i)
            review = review_body[i].text
            if "No feedback given" in review:
                continue
            lines = review.splitlines()
            review = "\n".join(lines[1:])
            try:
                review = review.replace(" \n  \nless","",1)
            except ValueError:
                pass
            #print(review)
            review_list.append(review)
            review_list = list(filter(None, review_list))
    except:
        review_list = 'NO REVIEWS'
    
    return job_title,description,review_list, expertise

def login_with_credentials(driver):
    print("logging in with credentials")
    #driver.get('https://www.upwork.com/ab/account-security/login')
    try:
        driver.get("https://www.upwork.com/ab/account-security/login")
        # Wait for the page to load for a maximum of 5 seconds
        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/header/div/div[1]/div/a/span[2]/svg")))
    except:
        print("Page loaded by timeout of 10 seconds")
    #print('page loaded')
    try:
        username = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "login_username"))
        )
        username.send_keys(mail)
        print("sent username")
    except:
        driver.refresh()
        print('refreshing and trying again slowly')
        username = driver.find_element(By.ID,"login_username")
        print('sent username')
        username.send_keys(mail)
    
    time.sleep(1.5)
    login_button = driver.find_element(By.ID,'login_password_continue')
    login_button.click()
    time.sleep(1.5)
    login_password = driver.find_element(By.ID,"login_password")
    login_password.send_keys(password)
    time.sleep(1.5)
    remember_btn = driver.find_element(By.CLASS_NAME,'up-checkbox-replacement-helper')
    remember_btn.click()
    final_login_button = driver.find_element(By.ID,'login_control_continue')
    final_login_button.click()
    print('logged in with credentials')
    time.sleep(5)

def main():
    # options = webdriver.FirefoxOptions()
    # options.headless = True
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    login_with_credentials(driver)

    for idx, job_link in enumerate(job_links):
        title,desc,review,expertise = get_data(driver,job_link)
        output = {"title":title,
                "expertise":expertise,
                "desc":str(desc),
                "review":review}
        # print(output)
        with open(f"outputs\outputs-{idx}.json", "w") as fp:
            json.dump(output, fp)
        time.sleep(5)
        
    driver.close()
    print('done')

if __name__ == "__main__":
    main()
