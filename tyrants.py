from __future__ import annotations
import calendar
from argparse import ArgumentParser, Namespace
from datetime import date, datetime
from typing import Optional, List
import random

def format_names(names:List[str]) -> List[str]:
    # strip the newlines
    names = [n.strip() for n in names]

    # Add spaces after the name to make the output easier to read
    max_chars = len(max(names, key=len))
    formatted_names = []
    for name in names:
        formatted = name + ' '*(max_chars-len(name))
        formatted_names.append(formatted)

    return formatted_names


def get_start_month_index(start_date:Optional[str]) -> int:
    # If a month was specified return its index
    if start_date is not None:
        # Full name tyrants.py December
        if start_date in calendar.month_name:
            return list(calendar.month_name).index(start_date)

        # Abbreviated name tyrants.py Dec
        if start_date in calendar.month_abbr:
            return list(calendar.month_abbr).index(start_date)

    # If not, use the current month
    return date.today().month

def main(start_date:Optional[str]):
    month_index = get_start_month_index(start_date=start_date)

    tyrants = []
    with open('tyrants.txt') as f:
        tyrants = f.readlines()

    tyrants = format_names(names=tyrants)
    random.shuffle(tyrants)

    for tyrant in tyrants:
        m = calendar.month_name[month_index]
        print(f'{tyrant} is tyrant for {m}')
        # The index of the next month is between 1 and 12
        # get the index of the next month.
        month_index = 1 + (month_index%12)


parser : ArgumentParser = ArgumentParser()
parser.add_argument('start',nargs='?')
args : Namespace= parser.parse_args()
main(args.start)
