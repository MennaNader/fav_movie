### Movie Trailer website
###### -- first project in the fullstack nanodegree program

**Movie Trailer website is a website to show my favourite movies and their trailers.**

This project consists of three files:
- media.py
- entertainment_center.py
- fresh_tomatoes.py (provided by udacity)

##### media.py
In this file we create the `Movie` class that takes _title_, _poster_image_url_, _trailer_youtube_url_ as paramters to initialize.


##### entertainment_center.py
In this file we create a number of movies, insert them in an array and finally we call the `open_movies_page` function from the fresh_tomatoes.py file to create the website.

##### fresh_tomatoes.py
This file is provided by Udacity. It consists of two functions; `create_movie_tiles_content` and `open_movies_page`. On running `open_movies_page`, it creates an html file that shows the movies array we provided earlier.


### To run this code 

First make sure you have Python installed on your machine then navigate using your terminal to the project folder then run 
`python entertainment_center.py`
