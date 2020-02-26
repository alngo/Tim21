from datetime import datetime


def period_converter(period):
    register = {
        "m1": 60,
        "m5": 60 * 5,
        "m15": 60 * 15,
        "m30": 60 * 30,
        "H1": 60 * 60,
        "H2": 60 * 60 * 2,
        "H3": 60 * 60 * 3,
        "H4": 60 * 60 * 4,
        "H6": 60 * 60 * 4,
        "H8": 60 * 60 * 8,
        "D1": 60 * 60 * 24
    }
    return register[period]


def compare_time_against_period(start, end, period):
