from pywebio.input import (
    textarea,
    input as input_pw,
    NUMBER,
    DATE,
    TEXT,
    select,
    slider,
    checkbox,
    radio,
)
from pywebio.output import put_text, put_image, put_html, put_success, put_warning


from utils import reload_page, start_server
import constants
import config

reviews_info = []


def show_thank_you(username: str, rating: int) -> None:
    if rating > 5:
        put_success(constants.MESSAGE_GOOD_MOVIE.format(username=username))
    else:
        put_warning(constants.MESSAGE_BAD_MOVIE.format(username=username))


def main():
    username = input_pw(constants.REQUEST_USERNAME, required=True)

    movie_name = input_pw(constants.REQUEST_MOVIE, required=True)
    movie_category = select(
        constants.REQUEST_MOVIE_CATEGORY, constants.MOVIE_CATEGORIES
    )
    movie_review = textarea(constants.REQUEST_MOVIE_REVIEW)
    movie_rating = slider(constants.REQUEST_MOVIE_RATING, min_value=1, max_value=10)
    movie_emotion = checkbox(constants.REQUEST_USER_EMOTION, constants.MOVIE_EMOTION)
    movie_recommendation = radio(
        constants.REQUEST_RECOMMENDATION, constants.MOVIE_RECOMMENDATION
    )

    reviews_info.append([username, movie_name, movie_rating, movie_recommendation])
    show_thank_you(username, movie_rating)
    reload_page(config.PAGE_RELOAD_INTERVAL_MS)
    pass


start_server(main, config.SERVER_PORT, __name__)
