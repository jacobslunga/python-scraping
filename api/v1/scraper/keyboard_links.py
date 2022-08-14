from requests_html import HTMLSession


class KeyboardLinks:
    def get_keyboard_links(self, num_of_results):
        url = f"https://www.komplett.se/category/21635/gaming/spelutrustning/gamingtangentbord?nlevel=10431%C2%A721603%C2%A721635&hits={str(num_of_results)}"
        s = HTMLSession()
        r = s.get(url)

        keyboard_links = []

        links = r.html.find("a.product-link.image-container")
        for i, link in enumerate(links):
            clean_link = "https://www.komplett.se" + link.attrs["href"]
            keyboard_links.append(
                clean_link.replace(f"?productList=notSet&position={i+1}", "")
            )

        return keyboard_links


# obj = KeyboardLinks()
# obj.get_keyboard_links(10)
