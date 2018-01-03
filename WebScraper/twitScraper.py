from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

# PART ONE: NUMBER OF CHARACTERS
# Using Beautiful Soup, the script will parse through each tweet, grab the text and count the number of characters used,
# and then display the information using a data visualization tool (matplotlib / Seaborn).

# NEEDS:
# map out how to get to tweet information on twitter []
# read up how twitter allows you to use its data (check for another way to accomplish same goal) []
# pull tweet data from twitter []
# learn how data is used by matplotlib & Seaborn []
# look into real time tracking to pull information from a certain feed over a short time interval []
# look into storing data to an online database and pulling information from data base to show long term data set information []

#---------------------------------------------------------- CODE --------------------------------------------------------------------#

# URL for twitter (Accurate way to access? Check if I need to log in through an account to access information) Done?[]
twit_url = 'https://twitter.com/?lang=en'

# open connection to twitter
uClient = uReq(twit_url)

# offload content from page into a variable
    # check to be sure that the page will only read what is immediately loaded and will not refresh at bottom of page (initially) []
page_html = uClient.read()

# close the client
uClient.close()

# use beautiful soup html parser --> allows us to parse through the elements of a page
page_soup = soup(page_html, "html.parser")

# now that we have the page information, we can find all the parts that contain text from tweets
containers = page_soup.findAll("div", {"class":"js-tweet-text-container"})

# FOR NOW
    # create a csv to store tweet data into
filename = "tweetLength.csv"
f = open(filename, "w")

#create the headers
    # end each row with a new line (\n)
headers = "numChars\n"
f.write(headers)

# iterate through each container and pull information
for container in containers:
    # returns the text within the tweet
    tweet_text = container.p.text
    # count each character in the extracted text
    count = 0
    for c in tweet_text:
        count += 1

    f.write(count + "\n")

# if not closed we cannot use
f.close()