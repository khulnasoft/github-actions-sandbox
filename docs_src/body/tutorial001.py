from typing import Union

from readyapi import ReadyAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

print("hello")