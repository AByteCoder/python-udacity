#!/usr/bin/python3
import sys
import json
import random

#used to generate movies list in html
def createMoviesHTML(movies):
    html_string = ''
    colors = ["#F44336","#E91E63","#9C27B0","#673AB7","#3F51B5","#1E88E5",
    "#0288D1","#0097A7","#009688","#43A047","#558B2F","#827717","#E65100",
    "#F4511E","#795548"]
    for movie in movies:
        color = colors[random.randint(0,len(colors))]
        movie_string = '''
        <article class="movie" title="{name}" data-url="{trailer}">
          <img class="movie-image" src="{poster}" alt="{name} Image" />
          <div class="movie-review" style="background-color:{color};">
            <div class="movie-rating">
              <img src="https://ia.media-imdb.com/images/M/MV5BMjQ4NjkwOTUxNl5BMl5BcG5nXkFtZTgwNTEzODM2OTE@._V1_.png" class="review-logo"/>
              <span class="movie-review-text" >IMDB {imdb}</span>
              <img class="review-logo" src="http://www.clipartsfree.net/vector/small/Star-349834968906_Clipart_Free.png" />
            </div>
            <div class="movie-storyline">
            {story}
            </div>
          </div>
      </article>'''.format(name = movie['name'],trailer = movie['trailer'],poster = movie['poster'],imdb = movie['imdb'],story = movie['storyline'],color = color)
        html_string = html_string + movie_string
    return html_string

#used to build entire html page
def main():
    header_string = r'''<!DOCTYPE html>
    <html>
    <head>
      <title>My Favorite Movies </title>
      <meta charset="utf-8" />
      <meta name="author" content="Abytecoder"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link media="screen" href="style.css" rel="stylesheet" />
      <script type="text/javascript" src="script.js">
      </script>
    </head>
    <body>
      <header class="header">
        <span class="header-title">My Favourite Movies</span>
      </header>
      <div class="movie-container">'''
    footer_string = r'''
    </div>
    <section class="dialog">
      <iframe class="movie-trailer" frameborder="0"></iframe>
    </section>
    </body>
    </html>'''
    arg_l = len(sys.argv)
    if  arg_l > 1:
        try:
            json_file = open(sys.argv[1])
            json_data = json_file.read()
            json_file.close()
            movies = json.loads(json_data)
            movies_string = createMoviesHTML(movies)
            output_filename = 'index.html' if arg_l < 2 else sys.argv[2]
            output_file = open(output_filename,'w')
            output_file.write(header_string + movies_string + footer_string)
            output_file.close()
        except Exception as e:
            print(e)
    else:
        print("USAGE: python3 fav_movies.py data.json [index.html]")


if __name__ == "__main__":
    main()
