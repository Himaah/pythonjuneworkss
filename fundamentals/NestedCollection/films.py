movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


#q1 total_number_of_movies

total_movies= len(movies)
# print("movie count",total_movies)

#q2 movies with genre Drama

genre_filter= [m.get("title") for m in movies if "Drama" in m.get("genres")]
# print(genre_filter)

#q3 latest movie
def get_year(mov):
    return mov.get("year")
latest_movie_data=max(movies,key=get_year)
movie_year_filter=[m.get("title") for m in movies if m.get("year")==latest_movie_data.get("year")]
# print(movie_year_filter)

#q4 top movie (movie with higest rating)

#q5 movies with language malayalam
malayalam_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)
#q6 movies released after year 2016
year_filter=[m.get("title") for m in movies if m.get("year")>2016]
# print(year_filter)

#q7 movie with lowest rating

#q8 malayalam movies with genere Action

#q9 movies releasd in same years

# q10 oldest movie
movie_dictionary={}
for m in movies:
    release_year=m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))
    else:
        movie_dictionary[release_year]=[m.get("title")]
# print(movie_dictionary)

oldest_moviedata= min(movies,key=get_year)
oldest_movie_names=[m.get("title")  for m in movies if m.get("year")==oldest_moviedata.get("year")]
# print(oldest_movie_names)

# movie name with generes either Drama or Comedy

genres=set()

for m in movies:
    for g in  m.get("genres"):
        genres.add(g)
# print(genres)

genres={g for m in movies for g in m.get("genres")}
# print(genres)

# action:2, drama:2

all_genres=[g for m in movies for g in m.get("genres")]
genre_count={g:all_genres.count(g) for g in all_genres}
# print(genre_count)


# print the title of movies in alphabetic order

def get_title(m):
    return m.get("title")
sorted_movies=sorted(movies,key=get_title)
sorted_movie_title=[m.get("title") for m in sorted_movies]
print(sorted_movie_title)


# mo vies released in each yr
# years=[m.get("year") for m in movies]
# print(years)

# year_count={y:years.count(y) for y in years}
# print(year_count)




# lst=[10,20,10,20,10,11,12]
# number_count={num:lst.count(num) for num in lst}
# print(number_count)

# text=["hello hai hello"]
# words=text.split(" ")
# word_count={w:words.count(w) for w in words}
# print(word_count)


















