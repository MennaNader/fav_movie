# importing media file that we've created to access the Movie class
import media
# importing fresh_tomamtoes file to access the website generator throught the open_movies_page function
import fresh_tomatoes


# creating various movies instances

the_social_network = media.Movie(
    "The Social Network", "https://image.tmdb.org/t/p/original/ok5Wh8385Kgblq9MSU4VGvazeMH.jpg", "https://www.youtube.com/watch?v=lB95KLmpLR4")

her = media.Movie("Her",
                  "https://image.tmdb.org/t/p/original/8f8Hisd36IN8jN1OpKxsxRu8i57.jpg",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

star_wars = media.Movie("Star Wars: The Last Jedi",
                        "https://image.tmdb.org/t/p/original/aKlGvKHBoJRaDuJWiolVzAu7cMM.jpg",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

thor = media.Movie("Thor: Ragnarok", "https://image.tmdb.org/t/p/original/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")


# adding the movies to an array
movies = [the_social_network, her, star_wars, thor]

# calling the open_movies_page function from the fresh_tomamtoes file to create the website
fresh_tomatoes.open_movies_page(movies)
