from requests_html import HTMLSession
from .keyboard_links import KeyboardLinks
import re


class KeyboardInfo:
    def get_keyboard_info(self, num_of_results):
        keyboard_links = KeyboardLinks()
        links = keyboard_links.get_keyboard_links(num_of_results)
        keyboard_info = []

        for i, link in enumerate(links):
            s = HTMLSession()
            r = s.get(url=link)

            try:
                title = r.html.find("h1.product-main-info-webtext1", first=True).text
                price = float(
                    re.sub(
                        r"(\d)\s+(\d)",
                        r"\1\2",
                        r.html.find("span.product-price-now", first=True)
                        .text.replace(" ", "")
                        .replace(":-", ""),
                    )
                )

                keyboard_highlights = []
                keyboard_reviews = []
                highlights = r.html.find("li.product-highlights__item")
                reviews = r.html.find("div.review-item")
                overall_stars = float(
                    r.html.find(
                        "div.product-main-info-review.new-arrangement > a > span",
                        first=True,
                    ).attrs["title"][0]
                )

                for review in reviews:
                    review_title = review.find("h3.review-title", first=True).text
                    body = review.find("p.review-text", first=True).text.replace(
                        "Läs mer", ""
                    )
                    stars = float(
                        review.find("span.stars > span", first=True).attrs["title"][0]
                    )
                    complete_review = {
                        "title": review_title,
                        "body": body,
                        "stars": stars,
                    }
                    keyboard_reviews.append(complete_review)

                for highlight in highlights:
                    keyboard_highlights.append(highlight.text.strip())

                complete_keyboard_info = {
                    "title": title,
                    "price": price,
                    "overall_stars": overall_stars,
                    "highlights": keyboard_highlights,
                    "reviews": keyboard_reviews,
                }
                keyboard_info.append(complete_keyboard_info)

            except Exception as e:
                print("Error: ", e)

        return keyboard_info


info_obj = KeyboardInfo()
info_obj.get_keyboard_info(10)
