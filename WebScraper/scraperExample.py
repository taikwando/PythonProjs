from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

#From example in Introduction to Web Scraping (With Python and Beautiful Soup)

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38'

#opening up connection, grabbing the page
uClient = uReq(my_url)

#offload content into variable
page_html = uClient.read()

#close the client
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")


#Once we have the page_soup as an html parser, we can parse through the elements of the page

#finds each element within a div tag with class item-container
##grabs each product from the page
containers = page_soup.findAll("div", {"class":"item-container"})

#creates a new file or writes to an existing with this name
filename = "products.csv"
f = open(filename, "w")

#creates the headers in the csv
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    #returns the brand from the page
    brand = container.div.div.a.img["title"]

    #finds the product title
    ##use .text because the title does not fall within a tag or attribute
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    #shipping price
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()



    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    #write to the csv
    ##deliminated by commas
    ###must replace commas in inputs or will create unnecessary categories
    ####ended with a new line
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

#always close the file
f.close()