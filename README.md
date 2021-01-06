# wootware_script
> Please note: The script is for learning purposes and not for any malicious intent 

<p align="center">
 <img width="500" src=https://user-images.githubusercontent.com/50704452/103077826-3be4c400-45d9-11eb-8883-1c94ca26a649.png>
</p>

 - Built a script to help me identify current components on hand at [Wootware.co.za](https://www.wootware.co.za/)
 - Also added the ability to:
     - [x] Add items to your cart
     - [x] Display total of items in cart to purchase at a later date
# Packages

- Selenium : https://pypi.org/project/selenium/
- BeautifulSoup : https://pypi.org/project/beautifulsoup4/
----
 # Table of content
 1. [How it works](#how-it-works)
 2. [Installation](#installation)
 3. [How to use script](#how-to-use-script)
 4. [Troubleshoot](#Troubleshoot)
----

 # How it works
 - `add_components()` function is used to prompt user for which component/s it need to retrieve from website stored in `shopping_list`
 - `navigate_pages()` then determines which pages it needs to navigate to based on `shopping_list`.  
 - `website_nav()` handles the selenium automation aswell use `get_scrap()` to webscrape pages to create list of conponents(e.g list of CPUs) into a dataframe called `data`
 - `cart_components` returns a list of items the users want to purchase based on code (e.g e-0,e-1,e-2 etc.)
 - `get_link()` is functions that automates adding to cart based on `cart_components` with then displaying the cart total at the end
 

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
 4. Create pipenv type
 ```
 pipenv --three
 ```
 5. Activate virtual environment type
 ```
 pipenv shell
 ```
 6. To install packages type
``` 
pip install -r requirements.txt
```
7. Install additional depencies
```
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
```
 # How to use script
 You can have two option to run the script:
 #### a) Headless state (default)
 ![woot_4](https://user-images.githubusercontent.com/50704452/103755751-fbdd0280-5016-11eb-94e8-2f56953eae63.gif)
 
 
 #### b) User-interface state
  ![woot_3](https://user-images.githubusercontent.com/50704452/103754324-e1a22500-5014-11eb-9538-4d014386df21.gif)
 > To run selium with a user-interface(i.e browser interaction) comment out these lines in `main.py`:
 ![user-interface](https://user-images.githubusercontent.com/50704452/103752538-7eaf8e80-5012-11eb-9cc6-6fce6870e7b5.png)
 
 
 > To run in Terminal:
 ```
python3 src/main.py
 ```
 ![woot_terminal](https://user-images.githubusercontent.com/50704452/103770580-ebd11d00-502e-11eb-9ee1-bb09559df46b.gif)
 
 
 > To run in VScode
 1. Open Vscode 
 2. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and select 'Python interpreter'
 3. choose python `Wootware_script:pipenv`
 4. Run
 ![woot_vscode](https://user-images.githubusercontent.com/50704452/103777087-0d370680-5039-11eb-96c8-d606da7adb99.gif)

 
 
 ## Steps
 1. User is prompted to enter values that correspond to components needed. eg
 ```python 
 1:'Internal Hard Drives', 2:'Processors / CPUs', 3:'Graphics Cards', 4:'Memory / RAM'
 ```
 2. Login with credentials (email + password) that it returns from `.env` file
 3. The script waits to retrieve list from the website of items on hand.If the user wants to add items in cart, they can enter code coresponding to item
 ```
 Please enter component for cart (Spaces between them e.g e-1 e12 e-33 )
 ```
 4. The items will added to cart with total cost displayed of cart
 
#  Troubleshoot
If you have any issue with geckodriver try installing 
```
sudo install firefox-geckodriver
```
