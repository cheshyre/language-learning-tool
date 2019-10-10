import json


def load_db():
    db_file_path = get_db_file_path()

    # Check if db file exists

    # If not create
    with open(db_file_path) as f:
        db = json.load(f)

    # Validate db with schema

    # Convert datetime_str entries to datetime objects

    return db


def write_db(db):
    # Convert datetime objects to datetime_str entries

    db_file_path = get_db_file_path()

    with open(db_file_path, "w") as f:
        json.dump(db, f, indent=2)


def get_db_file_path():
    return ""
