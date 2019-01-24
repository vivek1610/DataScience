from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup

############################## For Flipkart ####################################################

my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on"

############ Request to a URL for getting all the data
vClient =  urlReq(my_url)
############ Read all the content of that page
page_html = vClient.read()
############ Close request object
vClient.close()
########## Parse all the html data by beautifull Soup
page_soup = soup(page_html,"html.parser")
########## Find all the content of any div by class name
containers = page_soup.find_all("div",{"class":"_1UoZlX"})

#print(len(containers))
########## Will convert all the data at html form which is written
#print(soup.prettify(containers[0]))
#for one product
#container = containers[0]
#print(container)
########## Product Name
#prdname = container.find("div",{"class":"_3BTv9X"})
#print(soup.prettify(prdname))
#prod_name = prdname.img["alt"]
#print(prod_name)

########### Rating#################################

#Rating  = container.find("div",{"class":"hGSR34 _2beYZw"})
#print(Rating.text)
#price = container.find("div",{"class":"_1vC4OE _2rQ-NK"})
#print(price.text)
fw = open("Output/flip.txt",'w', encoding = 'utf-8')
for container in containers:
    prdname = container.find("div", {"class": "_3BTv9X"})
    prod_name = prdname.img["alt"]
    Rating = container.find("div", {"class": "hGSR34 _2beYZw"})
    new_rating = Rating.text;
    price = container.find("div", {"class": "_1vC4OE _2rQ-NK"})
    new_price = price.text.strip()
    #print(prod_name)
    #print(new_rating)
    #print(new_price)
    #print(prod_name+' | '+new_price+' | '+new_rating)
    fw.write(prod_name+" | "+new_price+" | "+new_rating+"\n")
    #print("===============================")
fw.close()
#################################################################################

amazon_Url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone"

urlObj =  urlReq(amazon_Url)
page_html = urlObj.read()
urlObj.close()
page_data = soup(page_html,"html.parser")
alldataarrays = page_data.find_all("div",{"class":"s-item-container"})

print(len(alldataarrays))
# dataarray = alldataarrays[0]
# #print(soup.prettify(dataarray))
# prd_amz = dataarray.find("div", {"class":"a-link-normal a-text-normal"})
# prod_amz = prdname.img["alt"]
# print(prod_amz)
# Rating_amz = dataarray.find("i", {"class":"a-icon a-icon-star a-star-4"})
# new_rating_amz = Rating_amz.text
# price_amz = dataarray.find("span", {"class":"a-size-base a-color-price s-price a-text-bold"})
# new_price_amz = price_amz.text.strip()
# print(new_price_amz)
# print(new_rating_amz)

fam = open("Output/amazon.txt",'w',encoding = 'utf-8')

for dataarray in alldataarrays:
    print(soup.prettify(dataarray))
    prd_amz = dataarray.find("div", {"class": "a-column a-span12 a-text-center"})
    prod_amz = prd_amz.img["alt"]
    # Rating_amz = dataarray.find("i", {"class":"a-icon a-icon-star a-star-4"})
    # new_rating_amz = Rating_amz.text
    price_amz = dataarray.find("span", {"class": "a-size-base a-color-price s-price a-text-bold"})
    new_price_amz = price_amz.text.strip()
    #print(new_price_amz)
    #print(new_rating_amz)
    # print(prod_amz)
    if 'Apple iPhone' in prod_amz:
        print(prod_amz+' | '+new_price_amz)
        fam.write(prod_amz + " | " + new_price_amz + "\n")
fam.close()
