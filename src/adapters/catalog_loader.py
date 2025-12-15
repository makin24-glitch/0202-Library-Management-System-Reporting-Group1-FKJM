# adapters/catalog_loader.py

from LibraryItem import Book, DVD, Journal


def load_sample_data_into_catalog(catalog, sample_records):
    """
    Adapter function that converts raw sample records into
    domain objects and loads them into the catalog.

    Args:
        catalog (Catalog): The catalog instance to populate
        sample_records (dict): Dictionary containing raw sample data
            {
                "books": [...],
                "dvds": [...],
                "journals": [...]
            }
    """

    # Load books
    for record in sample_records.get("books", []):
        book = Book(
            item_id=record["item_id"],
            title=record["title"],
            author=record["author"],
            status=record.get("status", "available")
        )
        catalog.add_item(book)

    # Load DVDs
    for record in sample_records.get("dvds", []):
        dvd = DVD(
            item_id=record["item_id"],
            title=record["title"],
            runtime_minutes=record["runtime_minutes"],
            status=record.get("status", "available")
        )
        catalog.add_item(dvd)

    # Load journals
    for record in sample_records.get("journals", []):
        journal = Journal(
            item_id=record["item_id"],
            title=record["title"],
            volume=record["volume"],
            issue=record["issue"],
            status=record.get("status", "available")
        )
        catalog.add_item(journal)
