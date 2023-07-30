### READ FIRST: Please see footnotes regarding robots.txt located at lines 51-52 before attempting to run this script ###

### import modules. pip install BeautifulSoup if needed
import requests
from bs4 import BeautifulSoup

### Prompts user to enter routing number, and stores it in a variable within a specified URL where the script will scrape for further information
routing_num = input("Please enter the routing number: ")
url = f'https://www.usbanklocations.com/routing-number-{routing_num}.html'

### Initiate a GET request with specified url and stores in a var called response
response = requests.get(url)

### Checks for status code 200 and any errors
if response.status_code == 200:

    ## Takes response text data and stores in var called html_content. Used as an argument in the below function to create a Beautiful Soup object, and uses the specified parser called html_parser
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    ## Target information is located in page title
    page_title = soup.title.text.strip()
else:
    print(f"Failed to fetch the web page. Status code: {response.status_code}")

### Identifies the relevant information and stores it in var
FI_routing = page_title.split()[3].replace(",", "")
FI_name = page_title.split(',', 1)[1].lstrip()

### Prints out the relevant information corresponding to the routing number specified by user
print(f"Institution Name: {FI_name}")
print(f"Routing Number: {FI_routing}")
print(f"EIN Number: ")


################################################ FOOTNOTES ################################################

#############################
# Version:    1.00          #
# Date:       07/30/2023    #
# Coder:      CH @chan2git  #
#############################

################################################
# Learning Resources/Guides                    #
# https://www.youtube.com/watch?v=gRLHr664tXA  #
#                                              #
# ChatGPT                                      #
################################################

### Per usbanklocation.com/robots.txt, web scraping/crawling in the manner this current script is operating appears to be compliant and allowed
### The script does not attempt to navigate to the specified 'disallowed' list. 
### However, before running this script please check usbanklocation.com/robots.txt to stay up to date and confirm 




