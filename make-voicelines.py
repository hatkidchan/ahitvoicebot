#!/bin/bash
from json import dump, load
from dataclasses import dataclass, field
from typing import *
import os, sys

if len(sys.argv) < 4:
    print('Required args: <input folder> <output json> <base url>')
    exit(1)

@dataclass
class VoiceLine:
    filename: str
    displayname: str
    tags: List[str]

    def to_json(self):
        return [
            self.filename, self.displayname, ' '.join(self.tags)
        ]

    @classmethod
    def de_json(cls, data):
        return cls(data[0], data[1], data[2].split(' '))

@dataclass
class VoicePack:
    name: str
    prefix: str
    basedir: str
    baseurl: str
    lines: List[VoiceLine] = field(default_factory=list)

    def to_json(self):
        return {
            'name': self.name,
            'prefix': self.prefix,
            'basedir': self.basedir,
            'baseurl': self.baseurl,
            'lines': [
                l.to_json() for l in self.lines
            ]
        }

    @classmethod
    def de_json(cls, data):
        return cls(name=data['name'],
                   prefix=data['prefix'],
                   basedir=data['basedir'],
                   baseurl=data['baseurl'],
                   lines=list(map(VoiceLine.de_json, data['lines'])))

data = {}
for d in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1], d)
    if os.path.isfile(path):
        continue
    url = os.path.join(sys.argv[3], d)
    pack = VoicePack(d.title(), d, path, url)
    for f in os.listdir(path):
        text = os.path.splitext(f)[0]
        text = text.replace('_', ' ')
        line = VoiceLine(f, text, [])
        pack.lines.append(line)
    data[d] = pack.to_json()

with open(sys.argv[2], 'w') as f:
    dump(data, f, indent=2, ensure_ascii=False)
