# -*- coding: utf-8 -*-

import json
import os


class SimpleDB:
    def __init__(self, db_path: str = "", auto_dump: bool = True):
        self.db = {}
        self.db_path = os.path.expanduser(db_path)
        self._load_or_create_db()

    def _load_or_create_db(self):
        if not os.path.isdir(self.db_path):
            if os.path.exists(self.db_path):
                try:
                    self.db = json.load(open(self.db_path))
                except ValueError as e:  # for load
                    raise ValueError("Can't load db")
            else:
                self.dump_to_file()
        else:
            raise FileNotFoundError("Expect file path, not a dir")

    def dump_to_file(self):
        with open(self.db_path, "w") as f:
            json.dump(self.db, f)

    def drop_db(self):
        self.db = {}
        self.dump_to_file()

    def get(self):
        pass

    def set(self):
        pass

    def delete(self):
        pass

    def pop(self):
        pass
