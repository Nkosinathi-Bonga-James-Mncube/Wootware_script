from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
import time
from for_scrapping import get_scrap,get_link
from selenium.webdriver.firefox.options import Options
from decouple import config
  
def add_components(): # gets select components from user
    comp = {1:'Internal Hard Drives', 2:'Processors / CPUs', 3:'Graphics Cards', 4:'Memory / RAM'}
    print("** Please enter components needed at Wootware.co.za**\n\n1. Internal Hard Drives\n2. Processors / CPUs\n3. Graphics Cards\n4. Memory / RAM\n")
    user_components= list(map(int,input("Please enter component needed (Spaces between them e.g 1 2 3 ) : ").split())) # able to input multiple input values
    user_components=list(dict.fromkeys(user_components)) # removes duplicates
    shopping_list =[comp[x] for x, y in zip(user_components,comp)]
    print(f'{shopping_list}\nPlease wait..')
    return shopping_list

def navigate_pages(value): # navigate link to each component in list in shopping_list
    comp = {
        'Internal Hard Drives':'https://bit.ly/3ahXX66', 
        'Processors / CPUs':'https://bit.ly/3r4bfsS',
        'Graphics Cards':'https://bit.ly/37rmDY7', 
        'Memory / RAM':'https://bit.ly/37qO5oU'
    }
    links=[comp[k] for k in value]
    return links


def website_nav(driver,shopping_list):
    log_link=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/ul/li[6]/a')
    log_link.click()
    try: # Login to website
        driver.find_element_by_id('email').send_keys(config('email'))
        driver.find_element_by_id('pass').send_keys(config('password'),Keys.ENTER)
        print("-->Login Successful :)\nPlease wait...")
    except Exception as e:
        print(f'Error : {e}')
    
    time.sleep(3)
    components_links= navigate_pages(shopping_list)
    df_list = list()
    for k in components_links: #navigate to each components added
        driver.get(k)
        in_stock=driver.find_element_by_partial_link_text('In stock with Wootware')
        in_stock.click()
        sort_by = Select(driver.find_element_by_css_selector('div.sort-by php select'))
        sort_by.select_by_visible_text('Price') # Arrage by price
        dataframe_results=get_scrap(driver.current_url)
        df_list.append(dataframe_results) # create dataframe list of components (e.g list of CPU , list of GPU etc)
    print('**found***')
    for k in df_list:
        print(k[['Product','Price','Code']],'\n')
    print('\n**end***')
    while True:
        try:
            cart_components= list(input("Please enter component for cart (Spaces between them e.g e-1 e12 e-33 ) : ").split())
            get_link(df_list,cart_components,driver)
            break
        except Exception as e:
            # print(f'Error 3: {e}') # debug
            print("Please enter only valid code! Spaces between them e.g e-1 e12 e-33 ")
    driver.quit

def user_comp_search_func(): # prompts user for components
    while True:
        try:
            shopping_list =add_components()
            options = Options()
            options.add_argument('--headless')
            # driver= webdriver.Firefox(executable_path="./src/drivers/geckodriver")
            driver= webdriver.Firefox(options=options,executable_path="./src/drivers/geckodriver")
            driver.get("https://www.wootware.co.za/")
            website_nav(driver,shopping_list)
            break

        except Exception as e:
            print(f'Error: {e}')#debug
            print("Error.Please enter valid components!")
user_comp_search_func()
