from typing import List

from readyapi import ReadyAPI
from pydantic import BaseModel, HttpUrl

app = ReadyAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
