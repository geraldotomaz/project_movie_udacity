import fresh_tomatoes
import video
import media
import TvShow


# Instance class TvShow category
stranger_things = TvShow.TvShow(
                "Stranger Things",
                "160min",
                "TV Show",
                "https://www.youtube.com/watch?v=XWxyRG_tckY",
                "http://www.gstatic.com/tv/thumb/tvbanners/12991665/p12991665_b_v8_aa.jpg",     # noqa
                "4",
                "10",
                "http://pipocacombo.com/wp-content/uploads/2009/11/avatar-poster-fake.jpg")     # noqa

game_of_thornes = TvShow.TvShow(
                "Game Of Thrones",
                "130min",
                "Tv Show",
                "https://www.youtube.com/watch?v=4Cmk9ACwc7w",
                "https://pmcdeadline2.files.wordpress.com/2016/02/got-poster-2.jpg",        # noqa
                "7",
                "7",
                "Game of Thrones is an American fantasy drama television" \
                " series created by David Benioff and D. B. Weiss")

suits = TvShow.TvShow(
      "Suits",
      "150min",
      "Tv Show",
      "https://www.youtube.com/watch?v=G-xIql-qiwU",
      "http://www.impawards.com/tv/posters/suits_ver2.jpg",     # noqa
      "2",
      "5",
      "Mike Ross (Patrick J. Adams) is a genius college dropout, who," \
      "with his natural intelligence and eidetic memory")

narcos = TvShow.TvShow(
      "Narcos",
      "160min",
      "Tv Show",
      "https://www.youtube.com/watch?v=U7elNhHwgBU",
      "https://static.omelete.uol.com.br/media/extras/conteudos/Escobar.jpg",       # noqa
      "4",
      "10",
      "Set and filmed in Colombia, season 1 tells the story of notorious" \
      "drug kingpin Pablo Escobar")

# Instance class media category
avatar = media.Movie(
      "Avatar",
      "160min",
      "Movie",
      "https://www.youtube.com/watch?v=nFjAEJQfVKo",
      "http://pipocacombo.com/wp-content/uploads/2009/11/avatar-poster-fake.jpg",       # noqa
      "Epic science fiction film directed, written," \
      "produced, and co-edited by James Cameron.")

apocalypto = media.Movie(
          "Apocalypto",
          "130min",
          "Movie",
          "https://www.youtube.com/watch?v=ngWBddVNVZs",
          "http://www.impawards.com/2006/posters/apocalypto.jpg",       # noqa
          "Epic science fiction film directed, written," \
          "produced, and co-edited by James Cameron.")

django = media.Movie(
      "Django Unchained",
      "120min",
      "Movie",
      "https://www.youtube.com/watch?v=tivv135aGbc",
      "http://www.newdvdreleasedates.com/images/posters/large/django-unchained-2012-05.jpg",        # noqa
      "Epic science fiction film directed, written,"\
      "produced, and co-edited by James Cameron.")

fight_club = media.Movie(
          "Fight Club",
          "140min",
          "Movie",
          "https://www.youtube.com/watch?v=Fs0-4NLSO2Y",
          "http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg",       # noqa
          "Epic science fiction film directed, written,"\
          "produced, and co-edited by James Cameron.")

# go through parameter for generate view in fresh_tomatoes
movies = [stranger_things, game_of_thornes, suits,
          narcos, avatar, apocalypto, django, fight_club]
fresh_tomatoes.open_movies_page(movies)
