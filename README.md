
# wootware_script
> Please note: The script is for learning purposes and not for any malicious intent

> Script working as of 6 Jan 2021



<p align="center">
 <img width="500" src=https://user-images.githubusercontent.com/50704452/103077826-3be4c400-45d9-11eb-8883-1c94ca26a649.png>
</p>

 - Built a script to retrieve prices of current PC components on hand at [Wootware.co.za](https://www.wootware.co.za/)
 - Also added the ability to:
     - [x] Add items to your cart to purchase at a later date
     - [x] Display total cost at the end of adding items
----
# Packages

- Selenium :      https://pypi.org/project/selenium/
- BeautifulSoup : https://pypi.org/project/beautifulsoup4/
- Pandas:         https://pypi.org/project/pandas/
- Python-decouple: https://pypi.org/project/python-decouple/
----
 # Table of content
 1. [How it works](#how-it-works)
 2. [Installation](#installation)
 3. [How to use script(Demo)](#how-to-use-script)
 4. [Troubleshoot](#Troubleshoot)
----

 # How it works
 - `add_components()` function prompts user which component/s it needs to retrieve from website to be stored in `shopping_list`
```python
def add_components():
    comp = {1:'Internal Hard Drives', 2:'Processors / CPUs', 3:'Graphics Cards', 4:'Memory / RAM'}
    print("** Please enter components needed at Wootware.co.za**\n\n1. Internal Hard Drives\n2. Processors / CPUs\n3. Graphics Cards\n4. Memory / RAM\n")
    user_components= list(map(int,input("Please enter component needed (Spaces between them e.g 1 2 3 ) : ").split())) 
    user_components=list(dict.fromkeys(user_components)) # removes duplicates
    shopping_list =[comp[x] for x, y in zip(user_components,comp)]
```
 - `navigate_pages()` creates array on which pages it needs to navigate to based on `shopping_list`. 
 ```python
 def navigate_pages(value):
    comp = {
        'Internal Hard Drives':'https://bit.ly/3ahXX66', 
        'Processors / CPUs':'https://bit.ly/3r4bfsS',
        'Graphics Cards':'https://bit.ly/37rmDY7', 
        'Memory / RAM':'https://bit.ly/37qO5oU'
    }
    links=[comp[k] for k in value]
 ```
 - `website_nav()` handles the selenium automation aswell as use `get_scrap()` to webscrape pages on Wootware.co.za to create list of conponents(e.g list of CPUs) into a dataframe called `dataframe_results`
 ```python
dataframe_results=get_scrap(driver.current_url)
df_list.append(dataframe_results)  
 ```
 - `cart_components` returns a list of items the users want to purchase based on code (e.g e-0,e-1,e-2 etc.)
 ```python
 list(input("Please enter component for cart (Spaces between them e.g e-1 e12 e-33 ) : ").split())
 ```
 - In `for_scrapping.py` the `get_link()` function handles automating adding to cart based on `cart_components` which then displays the cart total at the end
 ```python
 cart_button=driver.find_element_by_id('product-addtocart-button').click()
 y=driver.find_element_by_css_selector('div.subtotal span.price')
 print('------------------------\nTotal in cart: ' ,y.get_attribute('innerHTML'),'\n------------------------\nBye!')  
 ```
 

 # Installation
 1. Install pipenv
 ```
 pip install pipenv
 ```
 2. Clone repo
 3. Open `.env` (it will be hidden in terminal) and enter registered user details for Wootware.co.za (email and password) to be used to sign in
```
//Example
email=test@gmail.com
password=123
```
 4. Create pipenv
 ```
 pipenv --three
 ```
 5. Activate virtual environment
 ```
 pipenv shell
 ```
 6. To install packages
``` 
pip install -r requirements.txt
```
7. Install additional dependencies
```
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
```
8. To deactivate virtual environment when you are done with the script
```
deactivate
```
 # How to use script
 You can have two options on how to use the script:
 #### a) Headless state (default)
 ![woot_4](https://user-images.githubusercontent.com/50704452/103755751-fbdd0280-5016-11eb-94e8-2f56953eae63.gif)
 
 
 #### b) User-interface state
  ![woot_3](https://user-images.githubusercontent.com/50704452/103754324-e1a22500-5014-11eb-9538-4d014386df21.gif)
 > To run Selenium with a user-interface(i.e browser interaction) comment out these lines in `main.py`:
 ![user-interface](https://user-images.githubusercontent.com/50704452/103752538-7eaf8e80-5012-11eb-9cc6-6fce6870e7b5.png)
 
 ## Run
 > To run in Terminal
 ```
python3 src/main.py
 ```
 
 > To run in VScode:
 1. Open VScode 
 2. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and select 'Python interpreter'
 3. Choose python 'Wootware_script:pipenv'
 4. Open `main.py` and run
 
#  Troubleshoot
If you have any issue with geckodriver try installing 
```
sudo install firefox-geckodriver
```

