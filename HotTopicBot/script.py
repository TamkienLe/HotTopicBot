
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


this_email = "physicalcookie@gmail.com"
phone_number = "6138839903"
first_name = "Tamkien"
last_name = "Le"
this_address = "8 Danby ct"
this_city = "NEPEAN"
this_zipCode = "K2R 1C9"

cardNameT = "TK"
cardNumberT = "4030000010001234"
cardExpireT = "0424"
cardCVNT = "123"
link = "https://www.hottopic.com/product/marvel-doctor-strange-in-the-multiverse-of-madness-pop-rintrah-6-inch-vinyl-figure/16749141.html"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)





def addToCart(link):

        driver.implicitly_wait(10)
        driver.get(link)
        add_to_cart = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[5]/div[8]/div/div[1]/button')
        add_to_cart.click()
        proceed_to_checkout = driver.find_element_by_class_name('mini-cart-checkout-btn')
        proceed_to_checkout.click()

        return link


def checkOut(email,number,firstName,lastName, address,city,zipcode):
        
            typemail = driver.find_element_by_id("email")
            typemail.send_keys(email)

            typenumber = driver.find_element_by_id("shippingPhoneNumberdefault")
            typenumber.send_keys(number)

            typeFirstname = driver.find_element_by_id("shippingFirstNamedefault")
            typeFirstname.send_keys(firstName)

            typeLastname = driver.find_element_by_id("shippingLastNamedefault")
            typeLastname.send_keys(lastName)

            typeAddress = driver.find_element_by_id("shippingAddressOnedefault")
            typeAddress.send_keys(address)

            typeCity = driver.find_element_by_id("shippingAddressCitydefault")
            typeCity.send_keys(city)

            country = driver.find_element_by_id("shippingCountrydefault")
            selectCountry = Select(country)
            selectCountry.select_by_value("CA")

            state = driver.find_element_by_id("shippingStatedefault")
            selectState = Select(state)
            selectState.select_by_value("ON")

            typezipCode = driver.find_element_by_id("shippingZipCodedefault")
            typezipCode.send_keys(zipcode)




            return email,number,firstName,lastName,address,city,zipcode

def dropDown(cardName,cardNumber,cardExpire,cardCVN):
            continueToPayment = driver.find_element_by_xpath('//*[@id="checkout-main"]/div[3]/div[1]/div[11]/div/div/button[1]')
            continueToPayment.click()

            name = driver.find_element_by_id('first-data-payment-field-name')
            name.send_keys(cardName)

            firstDataPay = driver.find_element_by_id('first-data-payment-field-card')
            firstDataPay.send_keys(cardNumber)

            expire = driver.find_element_by_id('first-data-payment-field-exp')
            expire.send_keys(cardExpire)

                
            cvn = driver.find_element_by_id('cvn')
            cvn.send_keys(cardCVN)

            
            finalReview = driver.find_element_by_class_name("submit-payment")
            finalReview.click()

            time.sleep(2)
            purchaseMe = driver.find_element_by_xpath('//*[@id="checkout-main"]/div[3]/div[1]/div[11]/div/div/button[4]')
            driver.execute_script("window.scrollTo(0, 60)") 

            purchaseMe.click()




#addToCart(link)
#checkOut(this_email,phone_number,first_name,last_name,this_address,this_city,this_zipCode)
#dropDown(cardNameT,cardNumberT,cardExpireT,cardCVNT)




    






    

        
        





    




 








  




    










