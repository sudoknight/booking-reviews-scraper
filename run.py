from typing import Literal

import typer
from typing_extensions import Annotated

from data_models import Input
from scrape import Scrape

app = typer.Typer()


@app.command()
def execute(
    hotel_name: Annotated[
        str, typer.Argument(default=..., help="Hotel name from booking.com url")
    ],
    country: Annotated[
        str,
        typer.Argument(
            default=...,
            help="Two character country code (ALPHA-2 code) e.g. 'us'. Visit this link: https://www.iban.com/country-codes",
        ),
    ],
    sort_by: Annotated[
        str,
        typer.Option(
            help="Sort reviews by 'most_relevant', 'newest_first', 'oldest_first', 'highest_scores' or 'lowest_scores'",
            rich_help_panel="Secondary Arguments",
        ),
    ] = "most_relevant",
    n_reviews: Annotated[
        int,
        typer.Option(
            help="Number of reviews to scrape from the top. -1 means scrape all. The reviews will be scraped according to the 'sort_by' option",
            rich_help_panel="Secondary Arguments",
        ),
    ] = -1,
    stop_criteria_username: Annotated[
        str,
        typer.Option(
            help="username of the review. Stop further scraping when review of this username is found",
            rich_help_panel="Secondary Arguments",
        ),
    ] = None,
    stop_criteria_review_title: Annotated[
        str,
        typer.Option(
            help="Review title to find. Stop further scraping when given username and review title is found",
            rich_help_panel="Secondary Arguments",
        ),
    ] = None,
    save_review_to_disk: Annotated[
        bool,
        typer.Option(
            help="Whehter to save reviews on the local disk or not",
            rich_help_panel="Secondary Arguments",
        ),
    ] = True,
):
    input_params = {
        "hotel_name": hotel_name,
        "country": country,
        "sort_by": sort_by,
        "n_rows": n_reviews,
    }

    if stop_criteria_username:
        stop = {"username": stop_criteria_username}

        if stop_criteria_review_title:
            stop["review_text_title"] = stop_criteria_review_title

        input_params["stop_critera"] = stop

    s = Scrape(input_params, save_data_to_disk=save_review_to_disk)
    ls_reviews = s.run()
    print(f"Scrapping Complete: Total Reviews  {len(ls_reviews)}")


if __name__ == "__main__":
    typer.run(execute)


# python run.py 'paramount-new-york' 'us'
# python run.py 'paramount-new-york' 'us' --sort-by 'newest_first' --n-reviews 20
# python run.py 'paramount-new-york' 'us' --stop-criteria-username 'Al' --stop-criteria-review-title 'المكان جدا جميل ويستحق الرجوع له مره اخرى'