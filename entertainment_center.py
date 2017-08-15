import media
import fresh_tomatoes


# Create the movies to be rendered on the website
get_out = media.Movie(
    "Get Out",
    "2017",
    "Young interracial couple visit a family retreat house",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",  # NOQA
    "https://www.youtube.com/watch?v=sRfnevzM9kQ")  # NOQA

kubo_and_the_two_strings = media.Movie(
    "Kubo and the Two Strings",
    "2016",
    "Young boy on a quest to discover the secrets of his family",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/c/c4/Kubo_and_the_Two_Strings_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=p4-6qJzeb3A")  # NOQA

the_big_sick = media.Movie(
    "The Big Sick",
    "2017",
    "Young interracial couple when parents don't approve",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",  # NOQA
    "https://www.youtube.com/watch?v=jcD0Daqc3Yw")  # NOQA

finding_dory = media.Movie(
    "Finding Dory",
    "2016",
    "Dory goes out to find her parents",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",  # NOQA
    "https://www.youtube.com/watch?v=MKJA-VLpiCo")  # NOQA

the_incredibles = media.Movie(
    "The Incredibles",
    "2004",
    "A super-powered family fight off villains",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eZbzbC9285I")  # NOQA
coach_carter = media.Movie(
    "Coach Carter",
    "2003",
    "A basketbal coach for troubled youths",
    "PG-13",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Coach_Carter_poster.JPG",  # NOQA
    "https://www.youtube.com/watch?v=znyAnWUYf2g")  # NOQA

# Append the movies to a list so that open_movies_page function can be called
movies = [get_out, kubo_and_the_two_strings, the_big_sick, 
          finding_dory, the_incredibles, coach_carter]

# Call the Open_movies_page function to create the HTML Page
fresh_tomatoes.open_movies_page(movies)
