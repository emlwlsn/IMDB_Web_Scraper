import urllib3
from urllib3.exceptions import InsecureRequestWarning
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# finds desired range of years to search from
print("Welcome to the Movie Recommendation Program")
print("Choose a range of years.")
year1 = input("Year 1: ")
year2 = input("Year 2: ")

# makes sure the first year is not later than the second year
while (year2 < year1):
    print("Please make sure year 1 is earlier than year 2")
    year1 = input("Year 1: ")
    year2 = input("Year 2: ")

# all genres to display
genres = ["action", "adventure", "animation", "biography", "comedy", "crime", 
         "documentary", "drama", "family", "fantasy", "film-noir", "game-show",
         "history", "horror", "music", "musical", "mystery", "news", "reality-tv",
         "romance", "sci-fi", "sport", "talk-show", "thriller", "war", "western"]

# display all genres for user to decide
j = 1
for genre in genres:
    if j % 3 == 0:
        print(genre + " | ")
    else:
        print(genre + " | ", end = " ")
    j += 1

print(" ")

# finds desired genre
genre = input("Please pick a genre from above: ").lower()

# disables warning for bypassing SSL certification requirement
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# inputs all inputted values to IMDB top 50 search URL
url = "http://www.imdb.com/search/title?release_date=" + str(year1) + "," + str(year2) + "&genres=" + genre
# gets the data from the URL and bypasses SSL certification
ourUrl = urllib3.PoolManager(cert_reqs='CERT_NONE').request('GET', url).data
# turns data into easily scrapable information using XML parser
soup = BeautifulSoup(ourUrl, "lxml")

i = 1

# finds HTML div's containing movie titles
movieList = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

print("Finding movies...")
# loops through div's with the atrribute of a movie title and displays it in a digestible way
for div_item in tqdm(movieList):
    div = div_item.find('div', attrs={'class': 'lister-item-content'})
    print(str(i) + '.', end = '')

    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

    print(str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1
