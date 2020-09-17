from dataclasses import dataclass


@dataclass
class Entry(object):
    name: str
    description: str
    url: str
    icon_url: str
