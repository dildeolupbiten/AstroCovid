# -*- coding: utf-8 -*-

from .constants import SIGNS


def convert_degree(degree: float = 0):
    for i in range(12):
        if i * 30 <= degree < (i + 1) * 30:
            return degree - (30 * i), [*SIGNS][i]


def reverse_convert_degree(degree: float = 0, sign: str = ""):
    return degree + 30 * [*SIGNS].index(sign)


def dms_to_dd(dms: str = ""):
    dms = dms.replace(" ", "")
    dms = dms.replace("\u00b0", " ").replace("\'", " ").replace("\"", " ")
    degree = int(dms.split(" ")[0])
    minute = float(dms.split(" ")[1]) / 60
    second = float(dms.split(" ")[2]) / 3600
    return degree + minute + second


def dd_to_dms(dd: float):
    degree = int(dd)
    minute = int((dd - degree) * 60)
    second = int((dd - degree - minute / 60) * 3600)
    return [f"{degree}\u00b0", f"{minute}'", f'{second}"']
