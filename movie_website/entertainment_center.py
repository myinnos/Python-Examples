import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story",
                        "https://s-media-cache-ak0.pinimg.com/736x/7f/05/de/7f05decaa12b9da157243662a4555f68.jpg",
                        "https://www.youtube.com/watch?v=PUOkjWOGWkc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A story",
                        "https://s-media-cache-ak0.pinimg.com/736x/f2/88/5b/f2885b98e1bf97f798c5891f1cc06ef1.jpg",
                        "https://www.youtube.com/watch?v=WrBGHqe_8iI")

#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
