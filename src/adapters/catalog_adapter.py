"""
Adapter functions that convert raw data into domain objects.
"""

from library_items import Book, DVD, Journal


def load_sample_data_into_catalog(catalog, sample_records):
    """
    Adapter function that populates a Catalog with LibraryItem objects
    created from raw sample data records.

    Args:
        catalog (Catalog): An initialized Catalog instance
        sample_records (list[dict]): Raw sample data records

    Returns:
        Catalog: The populated catalog
    """
    for record in sample_records:
        item_type = record.get("type")

        if item_type == "Book":
            item = Book(
                item_id=record["item_id"],
                title=record["title"],
                author=record["author"],
                status=record.get("status", "available")
            )

        elif item_type == "DVD":
            item = DVD(
                item_id=record["item_id"],
                title=record["title"],
                runtime_minutes=record["runtime_minutes"],
                status=record.get("status", "available")
            )

        elif item_type == "Journal":
            item = Journal(
                item_id=record["item_id"],
                title=record["title"],
                volume=record["volume"],
                issue=record["issue"],
                status=record.get("status", "available")
            )

        else:
            # Unknown item type — skip safely
            continue

        catalog.add_item(item)

    return catalog
