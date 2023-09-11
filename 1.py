import sys
from typing import NamedTuple


class LegoSet(NamedTuple):
    number: int
    name: str
    theme: str
    pieces: int


def from_line(line: str) -> LegoSet:
    tokens=line.strip("\n").split(";")
    return LegoSet(int(tokens[0]),tokens[1],tokens[2],int(tokens[3]))


def to_line(lego: LegoSet) -> str:
    return f"{lego.name}({lego.number}) : {lego.pieces} - {lego.theme}"


def order(lego: list[LegoSet]) -> list[LegoSet]:
    return sorted(lego,key=lambda lego:(-lego.pieces,lego.theme,lego.name,lego.number))


def main():
    lines=sys.stdin.readlines()
    lego=[]
    for line in lines:
        lego.append(from_line(line))
    sorted_lego=order(lego)
    for m in sorted_lego:
        print(to_line(m))


if __name__ == '__main__':
    main()