import requests
import urllib.request  
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
def get_link(df,cart_items,driver): # find matching code in list,add to cart and display total items in cart
    pd.set_option('display.max_colwidth', None)
    print('\n')
    for j in df:
        for k in cart_items:
            x= j[j['Code'] == k]
            if not x.empty: 
                try:
                    driver.get(x['Link'].item())
                    cart_button=driver.find_element_by_id('product-addtocart-button').click()
                    wait = WebDriverWait(driver,3)
                    close_popup_notification = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Continue Shopping"]'))).click()
                    print('-->Added to cart : ',x['Product'].item())
                except Exception as e:
                    print(f'Error: {e}')
    y=driver.find_element_by_css_selector('div.subtotal span.price')
    print('------------------------\nTotal in cart: ' ,y.get_attribute('innerHTML'),'\n------------------------\nBye!')                                                      

def get_scrap(woot_page_url): # Scrap Wootware website
    response= requests.get(woot_page_url)
    # data=BeautifulSoup(open("./src/test1.html"),'html.parser')
    data=BeautifulSoup(response.content,'html.parser')
    woot_site_product =data.find_all(attrs={"product-name"})
    woot_site_price = data.select("span[id*='product-price']")
    arr_price = [(k.text).strip() for k in woot_site_price]
    arr_product = [(k.text).strip() for k in woot_site_product]
    arr_links = [k.a['href'] for k in woot_site_product]
    global count
    arr_code = [ 'e-'+str(count) for count,k in enumerate(woot_site_product,count)]                                                                                                                                                                                                                                                                                                                                                                                              
    count = count + len(woot_site_product)
    data_df = { 
        'Product': arr_product,
        'Price' : arr_price,
        'Link': arr_links,
        'Code': arr_code
        }
   
    df=pd.DataFrame(data_df,columns = ['Product','Price','Link','Code'])
    df.style.set_properties(subset=['Link'], **{'width': '800px'}) # adjusting with for get_link function
    return df