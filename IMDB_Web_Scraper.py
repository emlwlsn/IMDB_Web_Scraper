import datetime
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm


print("Welcome to the Movie Recommendation Program")
print("Choose a range of years.")
year1 = input("Year 1: ")
year2 = input("Year 2: ")

while (year2 < year1):
    print("Please make sure year 1 is earlier than year 2")
    year1 = input("Year 1: ")
    year2 = input("Year 2: ")

genres = ["action", "adventure", "animation", "biography", "comedy", "crime", 
         "documentary", "drama", "family", "fantasy", "film-noir", "game-show",
         "history", "horror", "music", "musical", "mystery", "news", "reality-tv",
         "romance", "sci-fi", "sport", "talk-show", "thriller", "war", "western"]

j = 1
for genre in genres:
    if j % 3 == 0:
        print(genre + ",")
    else:
        print(genre + ",", end = " ")
    j += 1


genre = input("Please pick a genre from above: ").lower()

year = int(datetime.datetime.now().year)

url = "http://www.imdb.com/search/title?release_date=" + str(year1) + "," + str(year2) + "&genres=" + genre
ourUrl = urllib3.PoolManager(cert_reqs='CERT_NONE').request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")

i = 1

movieList = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

for div_item in tqdm(movieList):
    div = div_item.find('div', attrs={'class': 'lister-item-content'})
    print(str(i) + '.', end = '')

    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

    print(str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1
