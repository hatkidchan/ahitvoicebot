from typing import *
from dataclasses import dataclass, field


@dataclass
class VoiceLine:
    url: str
    name: str
    tags: str = ''

    @classmethod
    def create(cls, pack: 'VoicePack', line: List[str]) -> 'VoiceLine':
        url = pack.base_url + '/' + line[0]
        line = cls(url=url, name=line[1], tags=line[2])
        line.parent_pack = pack
        return line
    
    def __iter__(self):
        return iter([self.url, self.name, self.tags])


@dataclass
class VoicePack:
    prefix: str
    name: str
    base_url: str
    lines: List[VoiceLine]
    
    @classmethod
    def de_json(cls, data: dict) -> 'VoicePack':
        pack = cls(data['prefix'], data['name'], data['baseurl'], [])
        pack.lines = [
            VoiceLine.create(pack, line)
            for line in sorted(data['lines'], key=lambda line: line[0])
        ]
        return pack
    
    @property
    def n_lines(self):
        return len(self.lines)
    
    def __str__(self):
        return f'VoicePack#{self.prefix} {self.name!r} ({self.n_lines} items)'
    
    def __repr__(self):
        return (f'<b>Voice pack</b> <i>{self.name}</i>\n'
                f'<b>Prefix:</b> <code>{self.prefix}</code>\n'
                f'<b>Items count:</b> <code>{self.n_lines}</code>')

