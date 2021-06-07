from selenium import webdriver
import pandas as pd
import time
import re
import selenium
driver = webdriver.Chrome()

baseurl='https://www.futurelearn.com/reviews'

driver.get(baseurl)
filename=input("Set atteribute the enter File Name: -")

name=[]
date=[]
rating=[]
heading=[]
review=[]
coursename=[]
helpfull=[]
nothelpfull=[]

c=0
tot=0
while True:
    for i in range(3,13):
        reviewIDele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]'.format(i))
        reviewID=reviewIDele.get_attribute('data-review-id')
        nameele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[1]/div[1]/span[1]'.format(i))
        dateele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[1]/div[2]/span'.format(i))
        ratingele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[1]/div[1]/span[2]/span[6]'.format(i))
        headingele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[2]/div[1]'.format(i))
        reviewele=driver.find_element_by_xpath('//*[@id="{0}"]'.format(reviewID))
        reviewtext=reviewele.text.split("...")[0]
        try:
            readmoreele=driver.find_element_by_xpath('//*[@id="{0}"]/span[1]'.format(reviewID))
            readmoreele.click()
            review2ele=driver.find_element_by_xpath('//*[@id="{0}"]/p'.format(reviewID))
            reviewtext=reviewtext+review2ele.text.split(" Read Less")[0]
        except selenium.common.exceptions.NoSuchElementException:
            pass
        coursenameele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[2]/a/div'.format(i))
        helpfullele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[3]/div[3]/span[2]'.format(i))
        nothelpfullele=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[{0}]/div[3]/div[3]/span[3]'.format(i))


        name.append(nameele.text)
        date.append(dateele.text)
        nums=re.findall(r"[-+]?\d*\.\d+|\d+",ratingele.text)
        ratings=0
        for number in nums:
            try:
                ratings=int(number)
            except ValueError:
                ratings=float(number)
        rating.append(ratings)
        heading.append(headingele.text)
        review.append(reviewtext)
        coursename.append(coursenameele.text)
        helpfull.append(helpfullele.text)
        nothelpfull.append(nothelpfullele.text)
        tot=tot+1
    button=driver.find_element_by_xpath('//*[@id="yotpo-testimonials-product-reviews"]/div[13]/a[11]')
    if button.is_enabled():
        button.click()
        time.sleep(8)
    else:
        break
    c=c+1
    print("Scraping Page=====>>>>>",c,"..............","review Scraped Yet====>",tot)
driver.quit()
print("Total review Scraped====>",tot)
df=pd.DataFrame()
df["ReviwerName"]=name
df["DateOfReview"]=date
df["Rating"]=rating
df["HeadindOfReview"]=heading
df["Review"]=review
df["CourseName"]=coursename
df["Like"]=helpfull
df["DisLike"]=nothelpfull
df.to_csv(filename)














