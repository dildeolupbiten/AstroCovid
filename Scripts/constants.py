# -*- coding: utf-8 -*-

from .modules import swe

CONFIRMED = "time_series_covid19_confirmed_global.csv"
DEATHS = "time_series_covid19_deaths_global.csv"
RECOVERED = "time_series_covid19_recovered_global.csv"
URL = "https://raw.githubusercontent.com/CSSEGISandData/"\
    "COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
URL_CONFIRMED = URL + CONFIRMED
URL_DEATHS = URL + DEATHS
URL_RECOVERED = URL + RECOVERED
SIGNS = {
    "Aries": {
        "symbol": "\u2648",
        "color": "#FF0000"
    },
    "Taurus": {
        "symbol": "\u2649",
        "color": "#00FF00"
    },
    "Gemini": {
        "symbol": "\u264A",
        "color": "#FFFF00"
    },
    "Cancer": {
        "symbol": "\u264B",
        "color": "#0000FF"
    },
    "Leo": {
        "symbol": "\u264C",
        "color": "#FF0000"
    },
    "Virgo": {
        "symbol": "\u264D",
        "color": "#00FF00"
    },
    "Libra": {
        "symbol": "\u264E",
        "color": "#FFFF00"
    },
    "Scorpio": {
        "symbol": "\u264F",
        "color": "#0000FF"
    },
    "Sagittarius": {
        "symbol": "\u2650",
        "color": "#FF0000"
    },
    "Capricorn": {
        "symbol": "\u2651",
        "color": "#00FF00"
    },
    "Aquarius": {
        "symbol": "\u2652",
        "color": "#FFFF00"
    },
    "Pisces": {
        "symbol": "\u2653",
        "color": "#0000FF"
    }
}
PLANETS = {
    "Sun": {
        "number": swe.SUN,
        "symbol": "\u2299"
    },
    "Moon": {
        "number": swe.MOON,
        "symbol": "\u263E"
    },
    "Mercury": {
        "number": swe.MERCURY,
        "symbol": "\u263F"
    },
    "Venus": {
        "number": swe.VENUS,
        "symbol": "\u2640"
    },
    "Mars": {
        "number": swe.MARS,
        "symbol": "\u2642"
    },
    "Jupiter": {
        "number": swe.JUPITER,
        "symbol": "\u2643"
    },
    "Saturn": {
        "number": swe.SATURN,
        "symbol": "\u2644"
    },
    "Uranus": {
        "number": swe.URANUS,
        "symbol": "\u2645"
    },
    "Neptune": {
        "number": swe.NEPTUNE,
        "symbol": "\u2646"
    },
    "Pluto": {
        "number": swe.PLUTO,
        "symbol": "\u2647"
    },
    "Chiron": {
        "number": swe.CHIRON,
        "symbol": "\u26B7"
    },
    "True": {
        "number": swe.TRUE_NODE,
        "symbol": "\u260A"
    },
    "Asc": {
        "number": None,
        "symbol": "Asc"
    },
    "MC": {
        "number": None,
        "symbol": "MC"
    }
}
ASPECTS = {
    "Conjunction": {
        "degree": 0,
        "orb": "10\u00b0 0\' 0\"",
        "symbol": "\u260C"
    },
    "Semi-Sextile": {
        "degree": 30,
        "orb": "3\u00b0 0\' 0\"",
        "symbol": "\u26BA"
    },
    "Semi-Square": {
        "degree": 45,
        "orb": "3\u00b0 0\' 0\"",
        "symbol": "\u2220"
    },
    "Sextile": {
        "degree": 60,
        "orb": "6\u00b0 0\' 0\"",
        "symbol": "\u26B9"
    },
    "Quintile": {
        "degree": 72,
        "orb": "2\u00b0 0\' 0\"",
        "symbol": "Q"
    },
    "Square": {
        "degree": 90,
        "orb": "10\u00b0 0\' 0\"",
        "symbol": "\u25A1"
    },
    "Trine": {
        "degree": 120,
        "orb": "10\u00b0 0\' 0\"",
        "symbol": "\u25B3"
    },
    "Sesquiquadrate": {
        "degree": 135,
        "orb": "3\u00b0 0\' 0\"",
        "symbol": "\u26BC"
    },
    "BiQuintile": {
        "degree": 144,
        "orb": "2\u00b0 0\' 0\"",
        "symbol": "bQ"
    },
    "Quincunx": {
        "degree": 150,
        "orb": "3\u00b0 0\' 0\"",
        "symbol": "\u26BB"
    },
    "Opposite": {
        "degree": 180,
        "orb": "10\u00b0 0\' 0\"",
        "symbol": "\u260D"
    }
}
