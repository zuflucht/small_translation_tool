# C:\Scripts\Shopify Upload Tool\init_paths.py

import sys
import os
from icecream import ic


def add_data_classes_to_path():
    data_classes_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data_classes")
    )
    ic(data_classes_path)
    if data_classes_path not in sys.path:
        sys.path.append(data_classes_path)


def add_API_classes_to_path():
    API_classes_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "APIs")
    )
    ic(API_classes_path)
    if API_classes_path not in sys.path:
        sys.path.append(API_classes_path)


def add_all_to_path():
    add_data_classes_to_path()
    add_API_classes_to_path()
    ic(sys.path)


# immer ausführen wenn datei importiert wird
add_all_to_path()
