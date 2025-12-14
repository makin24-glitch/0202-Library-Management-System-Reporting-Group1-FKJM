# runner_file.py

from catalog import Catalog
from data.sample_data import SAMPLE_BOOKS, SAMPLE_DVDS, SAMPLE_JOURNALS
from data.sample_members import SAMPLE_MEMBERS
from adapters.catalog_loader import load_sample_data_into_catalog
from adapters.member_loader import load_sample_members
from services.checkout_service import create_checkout


def run():
    # Initialize catalog
    catalog = Catalog()

    sample_items = {
        "books": SAMPLE_BOOKS,
        "dvds": SAMPLE_DVDS,
        "journals": SAMPLE_JOURNALS
    }

    load_sample_data_into_catalog(catalog, sample_items)

    # Load members
    members = load_sample_members(SAMPLE_MEMBERS)

    # Demo checkout
    member = members["MEM001"]
    item = catalog.get_item("B001")

    checkout = create_checkout(
        checkout_id="CHK001",
        member=member,
        item=item,
        checkout_date="2025-03-01"
    )
    
    print(checkout)
    print(catalog)


 # Temporary verification
    print(catalog)
    for item in catalog.get_available_items():
        print(item)
