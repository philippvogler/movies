import media
import fresh_tomatoes

rogue_one = media.Movie ("Rogue One",
                         "A Star Wars Story: Rebels set out on a mission to steal the plans for the Death Star.",
                         "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                         "https://www.youtube.com/watch?v=Wji-BZ0oCwg")
doctor_strange = media.Movie ("Doctor Strange",
                              "After his career is destroyed, a brilliant but arrogant and conceited surgeon gets a new lease on life when a sorcerer takes him under her wing and trains him to defend the world against evil.",
                              "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                              "https://www.youtube.com/watch?v=wwcSki7r9cQ")
jason_bourne = media.Movie  ("Jason Bourne",
                             "Jason Bourne, now remembering who he truly is, tries to uncover hidden truths about his past.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b2/Jason_Bourne_%28film%29.jpg",
                             "https://www.youtube.com/watch?v=F4gJsKZvqE4")

movies = [rogue_one, doctor_strange, jason_bourne]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
