# runner_file.py

from data.sample_data import SAMPLE_BOOKS
from runner_methods import load_sample_data_into_catalog
from models.catalog import Catalog


def run():
    """
    Entry point:
    - Initialize catalog
    - Load installed sample data
    - Start dashboard workflow
    """
    catalog = Catalog("Main Library Catalog")

    load_sample_data_into_catalog(
        catalog=catalog,
        sample_records=SAMPLE_BOOKS
    )

    # dashboard / CLI would start here
    pass
