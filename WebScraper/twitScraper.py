from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
from threading import Timer

# PART ONE: NUMBER OF CHARACTERS
# Using Beautiful Soup, the script will parse through each tweet, grab the text and count the number of characters used,
# and then display the information using a data visualization tool (matplotlib / Seaborn).

# NEEDS:
# map out how to get to tweet information on twitter [x]
# read up how twitter allows you to use its data (check for another way to accomplish same goal) [x]
# pull tweet data from twitter [x]
# remove picture information from tweet because it adds to character count[x]
# learn how data is used by matplotlib & Seaborn []
# look into real time tracking to pull information from a certain feed over a short time interval []
    # potentially could have the program run in the background and pull tweets every certain interval of time
        # would need to add a check to make sure each tweet read is unique
        # need to store additional information on each tweet (timestamp, author, etc)
# look into storing data to an online database and pulling information from data base to show long term data set information []

#---------------------------------------------------------- CODE --------------------------------------------------------------------#

# FOR NOW until it can be moved to a server
# create a csv to store tweet data into
filename = "tweetLength.csv"
f = open(filename, "w")

#create the headers
    # end each row with a new line (\n)
headers = "numChars\n"
f.write(headers)

# URL for twitter (Accurate way to access? Check if I need to log in through an account to access information) Done?[x]
twit_url = 'https://twitter.com/?lang=en'


# number of times we want the function to run
loops = 1

# once the script is called, this is the only part that we want to loop through multiple times
# that way we do not repeatedly create the headers. Look into reading a file and continuing where it leaves off
def scrapeLoop():

    # open connection to twitter
    uClient = uReq(twit_url)

    # offload content from page into a variable
        # check to be sure that the page will only read what is immediately loaded and will not refresh at bottom of page (initially) [x]
    page_html = uClient.read()

    # close the client
    uClient.close()

    # use beautiful soup html parser --> allows us to parse through the elements of a page
    page_soup = soup(page_html, "html.parser")

    # now that we have the page information, we can find all the parts that contain text from tweets
    containers = page_soup.findAll("div", {"class":"js-tweet-text-container"})

    # iterate through each container and pull information
    for container in containers:
        # returns the text within the tweet
        tweet_text = container.p.text
        # count each character in the extracted text

        # remove the pic.twitter text
        # start by finding the index of pic.twitter
        pic_sub = "pic.twitter"
        index = tweet_text.find(pic_sub)

        if index > -1:
            count = index
            f.write(str(count) + "\n")

        else:
            count = 0
            for c in tweet_text:
                count += 1

            f.write(str(count) + "\n")

    global loops
    loops = loops - 1
    # recursively call the timer. 
    # That way we can collect data for a certain number of intervals.
    if loops > 0:
        timer = Timer(600.0, scrapeLoop)
        timer.start()
    else:
        # if not closed we cannot use
        f.close()


# create a timer [x]
# only run code once the timer hits certain time (test is 10 minutes, probably better to run it once every half hour)
timer = Timer(0.0, scrapeLoop)
timer.start()