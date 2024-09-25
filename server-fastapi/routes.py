from fastapi import APIRouter, HTTPException, Path, Query
from models import Item, Category
from data import items

router = APIRouter()


@router.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@router.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    return items[item_id]


@router.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, dict | list[Item]]:
    def check_item(item: Item):
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category is category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }


@router.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")
    items[item.id] = item
    return {"added": item}


@router.put(
    "/update/{item_id}",
    responses={404: {"description": "Item not found"}, 400: {"description": "No arguments specified"}},
)
def update(
    item_id: int = Path(title="Item ID", description="Unique integer that specifies an item.", ge=0),
    name: str | None = Query(default=None, title="Name", description="New name of the item.", min_length=1, max_length=8),
    price: float | None = Query(default=None, title="Price", description="New price of the item in Euro.", gt=0.0),
    count: int | None = Query(default=None, title="Count", description="New amount of instances of this item in stock.", ge=0),
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    if all(info is None for info in (name, price, count)):
        raise HTTPException(status_code=400, detail="No parameters provided for update.")

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@router.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    item = items.pop(item_id)
    return {"deleted": item}
