import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)
    @classmethod
    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(self.metadata, content)

    def __init__(self, metadata, content):
        data = metadata
        self.data = {content : "content"}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data.keys(type):
            return self.data["type"]
        else:
            return None

    @type.setter
    def type(self, data):
        data = self._data = ["type"]

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key == "content":
                data[key] = value
        return str(data)

