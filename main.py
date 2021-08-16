from bs4 import BeautifulSoup
import requests

def find_movies(page):
    html_page = requests.get(f'https://ffbox.org/filter/page/{page}/?dtyear=2021&type=Movies&filter=1').text
    soup = BeautifulSoup(html_page, 'lxml')

    movies = soup.find_all('div', class_='item')
    with open('movies.txt', 'w') as f:
        for movie in movies:
            movie_name = movie.h3.a.text
            rating = movie.find('span', class_='imdb').text
            trailer_page = requests.get(f'https://www.google.com/search?q={movie_name}+trailer&tbm=vid').text
            s = BeautifulSoup(trailer_page, 'lxml')
            trailer = s.find('div',class_='kCrYT')

            f.write(f'Movie Name: {movie_name}\n')
            f.write(f"Trailer:  {trailer.a.get('href')}\n")
            f.write(f'Rating:  {rating}\n\n')
            

find_movies(1)
print(f'Program Successfull, Please visit movies.txt to view data')
print('Would you like to scrape the next page?')
response = input('y/n>')

if response == 'y':
    find_movies(2)

print(f'Program Successfull, Please visit movies.txt to view data')