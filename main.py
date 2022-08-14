from fastapi import FastAPI

from api.v1.scraper.keyboard_info import KeyboardInfo

app = FastAPI()

keyboards = KeyboardInfo()


@app.get("/api/v1/get_keyboard_info/{num_of_results}")
def read_keyboard(num_of_results):
    return keyboards.get_keyboard_info(num_of_results)
