# -*- coding: utf-8 -*-

from functools import wraps
import json
import os
from warnings import warn


def check_is_hashable():
    def decorator(func):
        @wraps(func)
        def inner(self, *args):
            should_warn = False
            for item in args:
                # TODO add list support, maybe
                if not getattr(item, "__hash__", None):
                    should_warn = True
                    break
            if should_warn:
                warn("Not hashable key or value")
                return False
            return func(self, *args)

        return inner

    return decorator


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

    @check_is_hashable()
    def get(self, key):
        return self.db.get(key, None)

    @check_is_hashable()
    def set(self, key, value):
        self.db[key] = value
        return True

    @check_is_hashable()
    def delete(self, key):
        self.db.pop(key)
        return True

    @check_is_hashable()
    def pop(self, key):
        return self.db.pop(key, None)

    @check_is_hashable()
    def has(self, key):
        return key in self.db
