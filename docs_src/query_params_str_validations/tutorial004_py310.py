from readyapi import ReadyAPI, Query

app = ReadyAPI()


@app.get("/items/")
async def read_items(
    q: str
    | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results