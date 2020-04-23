# -*- coding: utf-8 -*-

from .zodiac import Zodiac
from .constants import PLANETS, SIGNS, ASPECTS
from .modules import os, dt, tk, cos, sin, radians
from .conversions import dms_to_dd, convert_degree, dd_to_dms


class Canvas(tk.Canvas):
    def __init__(self, zodiac: Zodiac = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["bg"] = "white"
        self.zodiac = zodiac
        self.aspects = {planet: [] for planet in PLANETS}
        self.midpoint_of_houses = []
        self["width"] = self.master.winfo_screenwidth() * 3/4
        self["height"] = self.master.winfo_screenheight() * 5/6
        self.planet_positions = zodiac[0]
        self.house_positions = zodiac[1]
        self.sign_positions = zodiac[2]
        self.house_pos = [i[-1] for i in self.house_positions]
        self.sign_pos = [i[-1] for i in self.sign_positions]
        self.signs = [i[0] for i in self.sign_positions]
        self.signs = [self.signs[-1]] + self.signs[:-1]
        self.pack(side="left")
        self.draw_oval_object()
        self.draw_houses()
        self.draw_signs()
        self.draw_house_numbers()
        self.draw_sign_symbols()
        self.draw_planets()
        self.draw_aspects()
        self.draw_planet_info()
        self.draw_house_info()
        self.draw_aspect_info()

    def draw_oval_object(self, x: int = 300, y: int = 300):
        self.oval_object(x=x, y=y, r=260, dash=False)
        self.oval_object(x=x, y=y, r=210, dash=False)
        self.oval_object(x=x, y=y, r=165)
        self.oval_object(x=x, y=y, r=60, dash=False)

    @staticmethod
    def line_components(degree: float = .0, r: int = 0):
        x, y = 300, 300
        x += (r * cos(radians(degree)))
        y -= (r * sin(radians(degree)))
        return x, y

    def coordinates(self, degree: float = .0, r1: int = 0, r2: int = 0):
        x1, y1 = self.line_components(degree=degree, r=r1)
        x2, y2 = self.line_components(degree=degree, r=r2)
        return x1, y1, x2, y2

    def oval_object(
            self,
            x: float = .0,
            y: float = .0,
            r: int = 0,
            dash: bool = True
    ):
        if dash:
            dash = (1, 10)
            self.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                fill="white",
                width=2,
                dash=dash
            )
        else:
            self.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                fill="white",
                width=2,
            )

    def line_object(
            self,
            x1: float = .0,
            y1: float = .0,
            x2: float = .0,
            y2: float = .0,
            width: int = 2,
            fill: str = "black",
    ):
        self.create_line(
            x1, y1, x2, y2, width=width, fill=fill
        )

    def aspect_line_object(
            self,
            x1: float = .0,
            y1: float = .0,
            x2: float = .0,
            y2: float = .0,
            width: int = 2,
            fill: str = "black"
    ):
        self.create_line(
            x1, y1, x2, y2, width=width, fill=fill
        )

    def text_object(
            self,
            x: float = .0,
            y: float = .0,
            width: int = 0,
            _text: str = "",
            font: str = "Arial",
            fill: str = "black",
    ):
        self.create_text(
            x, y, text=_text, width=width, font=font, fill=fill
        )

    def draw_houses(self):
        self.midpoint_of_houses = []
        for i, j in enumerate(self.house_pos):
            degree = j - (self.house_pos[0] - 180)
            if degree < 0:
                degree += 360
            elif degree > 360:
                degree -= 360
            self.midpoint_of_houses.append(degree)
            x1, y1, x2, y2 = self.coordinates(
                degree=degree, r1=60, r2=210
            )
            if i == 0 or i == 3 or i == 6 or i == 9:
                self.line_object(x1, y1, x2, y2, width=4)
            else:
                self.line_object(x1, y1, x2, y2, width=2)

    def draw_signs(self):
        for i, j in enumerate(self.sign_pos):
            x1, y1, x2, y2 = self.coordinates(degree=j, r1=210, r2=260)
            self.line_object(x1, y1, x2, y2, width=2)

    def draw_house_numbers(self):
        for i, j in enumerate(self.midpoint_of_houses):
            if i == 11:
                midpoint = \
                    (self.midpoint_of_houses[i] +
                     self.midpoint_of_houses[0]) / 2
            else:
                if self.midpoint_of_houses[i] == 360:
                    midpoint = self.midpoint_of_houses[i + 1] / 2
                else:
                    if self.midpoint_of_houses[i + 1] == 0 or \
                            self.midpoint_of_houses[i + 1] < 30:
                        midpoint = \
                            (self.midpoint_of_houses[i] +
                             self.midpoint_of_houses[i + 1] + 360) / 2
                    else:
                        midpoint = \
                            (self.midpoint_of_houses[i] +
                             self.midpoint_of_houses[i + 1]) / 2
            if i == 6:
                if midpoint > 180:
                    midpoint -= 180
            x1, y1, x2, y2 = self.coordinates(
                degree=midpoint, r1=60, r2=110
            )
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            self.text_object(x=x, y=y, _text=f"{i + 1}")

    def draw_sign_symbols(self):
        for i, j in enumerate(self.signs):
            end = 30 - (self.house_pos[0] % 30) + 180
            start = end - 30
            start += (30 * i)
            end += (30 * i)
            if start > 360:
                start -= 360
            if end > 360:
                end -= 360
            if start > 330:
                midpoint = (start + end + 360) / 2
            else:
                midpoint = (start + end) / 2
            if midpoint > 360:
                midpoint -= 360
            x1, y1, x2, y2 = self.coordinates(
                degree=midpoint, r1=210, r2=260
            )
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            self.text_object(
                x=x,
                y=y,
                _text=SIGNS[j]["symbol"],
                font="Arial 25",
                fill=SIGNS[j]["color"]
            )

    def draw_planets(self):
        for ind, i in enumerate(self.planet_positions):
            for j in self.sign_positions:
                planet = convert_degree(i[-2])
                if planet[1] == j[0]:
                    degree = planet[0] + j[1]
                    x1, y1, x2, y2 = self.coordinates(
                        degree=degree, r1=210, r2=175
                    )
                    x = ((x1 + x2) / 2) + 4
                    y = ((y1 + y2) / 2) + 4
                    self.text_object(
                        x=x,
                        y=y,
                        _text=PLANETS[i[0]]['symbol'],
                        width=0,
                        font="Default 20"
                    )
                    x1, y1, x2, y2 = self.coordinates(
                        degree=degree, r1=210, r2=205
                    )
                    self.line_object(
                        x1, y1, x2, y2, width=2, fill="red"
                    )

    def create_aspect(
            self,
            value: float = .0,
            _value: float = .0,
            color: str = "",
            r1: int = 160,
            r2: int = 165
    ):
        x1, y1, x2, y2 = self.coordinates(
            degree=value, r1=r1, r2=r2
        )
        _x1, _y1, _x2, _y2 = self.coordinates(
            degree=_value, r1=r1, r2=r2
        )
        self.aspect_line_object(
            x2, y2, _x2, _y2,
            width=2,
            fill=color,
        )

    def select_aspect(
            self,
            aspect: float = .0,
            value: float = 0,
            _value: float = 0,
            planet: str = ""
    ):
        if (
                0 < aspect <
                dms_to_dd(ASPECTS["Conjunction"]["orb"]) or
                360 - dms_to_dd(ASPECTS["Conjunction"]["orb"]) <
                aspect < 360
        ):
            self.aspects[planet].append(ASPECTS["Conjunction"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="red"
            )
        elif (
                30 - dms_to_dd(ASPECTS["Semi-Sextile"]["orb"]) < aspect <
                30 + dms_to_dd(ASPECTS["Semi-Sextile"]["orb"]) or
                330 - dms_to_dd(ASPECTS["Semi-Sextile"]["orb"]) <
                aspect < 330 + dms_to_dd(ASPECTS["Semi-Sextile"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Semi-Sextile"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="#804b00"
            )
        elif (
                45 - dms_to_dd(ASPECTS["Semi-Square"]["orb"]) < aspect <
                45 + dms_to_dd(ASPECTS["Semi-Square"]["orb"]) or
                315 - dms_to_dd(ASPECTS["Semi-Square"]["orb"]) < aspect <
                315 + dms_to_dd(ASPECTS["Semi-Square"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Semi-Square"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="#80cdff"
            )
        elif (
                60 - dms_to_dd(ASPECTS["Sextile"]["orb"]) < aspect <
                60 + dms_to_dd(ASPECTS["Sextile"]["orb"]) or
                300 - dms_to_dd(ASPECTS["Sextile"]["orb"]) < aspect <
                300 + dms_to_dd(ASPECTS["Sextile"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Sextile"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="blue"
            )
        elif (
                72 - dms_to_dd(ASPECTS["Quintile"]["orb"]) < aspect <
                72 + dms_to_dd(ASPECTS["Quintile"]["orb"]) or
                288 - dms_to_dd(ASPECTS["Quintile"]["orb"]) < aspect <
                288 + dms_to_dd(ASPECTS["Quintile"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Quintile"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="purple"
            )
        elif (
                90 - dms_to_dd(ASPECTS["Square"]["orb"]) < aspect <
                90 + dms_to_dd(ASPECTS["Square"]["orb"]) or
                270 - dms_to_dd(ASPECTS["Square"]["orb"]) < aspect <
                270 + dms_to_dd(ASPECTS["Square"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Square"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="red"
            )
        elif (
                120 - dms_to_dd(ASPECTS["Trine"]["orb"]) < aspect <
                120 + dms_to_dd(ASPECTS["Trine"]["orb"]) or
                240 - dms_to_dd(ASPECTS["Trine"]["orb"]) < aspect <
                240 + dms_to_dd(ASPECTS["Trine"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Trine"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="blue"
            )
        elif (
                135 - dms_to_dd(ASPECTS["Sesquiquadrate"]["orb"]) < aspect <
                135 + dms_to_dd(ASPECTS["Sesquiquadrate"]["orb"]) or
                225 - dms_to_dd(ASPECTS["Sesquiquadrate"]["orb"]) < aspect <
                225 + dms_to_dd(ASPECTS["Sesquiquadrate"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Sesquiquadrate"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="orange"
            )
        elif (
                144 - dms_to_dd(ASPECTS["BiQuintile"]["orb"]) < aspect <
                144 + dms_to_dd(ASPECTS["BiQuintile"]["orb"]) or
                216 - dms_to_dd(ASPECTS["BiQuintile"]["orb"]) < aspect <
                216 + dms_to_dd(ASPECTS["BiQuintile"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["BiQuintile"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="purple"
            )
        elif (
                150 - dms_to_dd(ASPECTS["Quincunx"]["orb"]) < aspect <
                150 + dms_to_dd(ASPECTS["Quincunx"]["orb"]) or
                210 - dms_to_dd(ASPECTS["Quincunx"]["orb"]) < aspect <
                210 + dms_to_dd(ASPECTS["Quincunx"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Quincunx"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="pink"
            )
        elif (
                180 - dms_to_dd(ASPECTS["Opposite"]["orb"]) < aspect <
                180 + dms_to_dd(ASPECTS["Opposite"]["orb"])
        ):
            self.aspects[planet].append(ASPECTS["Opposite"]["symbol"])
            self.create_aspect(
                value=value,
                _value=_value,
                color="red"
            )
        else:
            self.aspects[planet].append(None)

    def draw_aspects(self):
        planet_degrees = {}
        for i in self.planet_positions:
            for j in self.sign_positions:
                planet = convert_degree(i[-2])
                if planet[1] == j[0]:
                    degree = planet[0] + j[1]
                    planet_degrees[i[0]] = degree
        for key, value in planet_degrees.items():
            for _key, _value in planet_degrees.items():
                aspect = abs(value - _value)
                if key != _key:
                    self.select_aspect(
                        aspect=aspect,
                        value=value,
                        _value=_value,
                        planet=key
                    )

    def modify_info(self, sign, x, i, m, count1, count2):
        if sign == SIGNS["Aries"]["symbol"] or \
                sign == SIGNS["Leo"]["symbol"] or \
                sign == SIGNS["Sagittarius"]["symbol"]:
            self.text_object(
                x=x + count1 + (m * 55),
                y=count2 + (i * 16),
                font="Arial 10",
                _text=sign,
                fill="red"
            )
        elif sign == SIGNS["Taurus"]["symbol"] or \
                sign == SIGNS["Virgo"]["symbol"] or \
                sign == SIGNS["Capricorn"]["symbol"]:
            self.text_object(
                x=x + count1 + (m * 55),
                y=count2 + (i * 16),
                font="Arial 10",
                _text=sign,
                fill="green"
            )
        elif sign == SIGNS["Gemini"]["symbol"] or \
                sign == SIGNS["Libra"]["symbol"] or \
                sign == SIGNS["Aquarius"]["symbol"]:
            self.text_object(
                x=x + count1 + (m * 55),
                y=count2 + (i * 16),
                font="Arial 10",
                _text=sign,
                fill="yellow"
            )
        elif sign == SIGNS["Cancer"]["symbol"] or \
                sign == SIGNS["Scorpio"]["symbol"] or \
                sign == SIGNS["Pisces"]["symbol"]:
            self.text_object(
                x=x + count1 + (m * 55),
                y=count2 + (i * 16),
                font="Arial 10",
                _text=sign,
                fill="blue"
            )
        else:
            self.text_object(
                x=x + count1 + (m * 55),
                y=count2 + (i * 16),
                font="Arial 10",
                _text=sign,
                fill="black"
            )

    def draw_planet_info(self, x=600):
        planets = self.zodiac[0]
        frmt = [
            (
                PLANETS[planet[0]]["symbol"],
                planet[0],
                *dd_to_dms(convert_degree(planet[2])[0]),
                SIGNS[planet[1]]["symbol"],
                planet[1]
            )
            for planet in planets if planet[0] not in ["Asc", "MC"]
        ]
        planet_symbol = ""
        planet = ""
        degree = ""
        minute = ""
        second = ""
        sign_symbol = ""
        sign = ""
        for i, j in enumerate(frmt):
            planet_symbol += f"{j[0]}\n"
            planet += f"{j[1]}\n"
            degree += f"{j[2]}\n"
            minute += f"{j[3]}\n"
            second += f"{j[4]}\n"
            sign_symbol += f"{j[5]}\n"
            sign += f"{j[6]}\n"
            for m, k in enumerate(j):
                self.modify_info(
                    sign=k, x=x, m=m, i=i, count1=10, count2=15
                )
        self.line_object(x1=x, x2=x * 1.6, y1=205, y2=205, width=1)

    def draw_house_info(self, x=600):
        houses = self.zodiac[1]
        frmt = [
            (
                f"H{house[0]}",
                "",
                *dd_to_dms(convert_degree(house[2])[0]),
                SIGNS[house[1]]["symbol"],
                house[1]
            )
            for house in houses
        ]
        house = ""
        null = ""
        degree = ""
        minute = ""
        second = ""
        sign_symbol = ""
        sign = ""
        for i, j in enumerate(frmt):
            house += f"{j[0]}\n"
            null += "\n"
            degree += f"{j[1]}\n"
            minute += f"{j[2]}\n"
            second += f"{j[3]}\n"
            sign_symbol += f"{j[4]}\n"
            sign += f"{j[5]}\n"
            for m, k in enumerate(j):
                self.modify_info(
                    sign=k, x=x, m=m, i=i, count1=10, count2=220
                )
        self.line_object(x1=x, x2=x * 1.6, y1=410, y2=410, width=1)

    def draw_aspect_info(self, x=600):
        aspects = {
            k: v[i:] for i, (k, v) in enumerate(self.aspects.items())
        }
        for i, j in enumerate(aspects):
            if i != len(aspects.items()) - 1:
                self.line_object(
                    x1=x + 25 + (i * 25),
                    y1=428 + (i * 15),
                    x2=x + 25 + (i * 25),
                    y2=624,
                    width=1
                )
                self.line_object(
                    x1=x,
                    y1=428 + (i * 15),
                    x2=x + 25 + (i * 25),
                    y2=428 + (i * 15),
                    width=1
                )
            if j == "Mars" or j == "Venus":
                if os.name == "posix":
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15),
                        _text=PLANETS[j]["symbol"],
                        font="Arial 15"
                    )
                elif os.name == "nt":
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15),
                        _text=PLANETS[j]["symbol"],
                        font="Arial 10"
                    )
            else:
                self.text_object(
                    x=x + 15 + (i * 25),
                    y=420 + (i * 15),
                    _text=PLANETS[j]["symbol"],
                    font="Arial 10"
                )
            for k, m in enumerate(aspects[j]):
                if m == ASPECTS["Sextile"]["symbol"] or \
                        m == ASPECTS["Trine"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="blue"
                    )
                elif m == ASPECTS["Conjunction"]["symbol"] or \
                        m == ASPECTS["Square"]["symbol"] or \
                        m == ASPECTS["Opposite"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="red"
                    )
                elif m == ASPECTS["Semi-Sextile"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="#804b00"
                    )
                elif m == ASPECTS["Semi-Square"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="#80cdff"
                    )
                elif m == ASPECTS["Quintile"]["symbol"] or \
                        m == ASPECTS["BiQuintile"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="purple"
                    )
                elif m == ASPECTS["Sesquiquadrate"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="orange"
                    )
                elif m == ASPECTS["Quincunx"]["symbol"]:
                    self.text_object(
                        x=x + 15 + (i * 25),
                        y=420 + (i * 15) + ((k + 1) * 15),
                        _text=m,
                        font="Arial 10",
                        fill="pink"
                    )
        self.line_object(
            x1=x + 25 + (-1 * 25),
            y1=428,
            x2=x + 25 + (-1 * 25),
            y2=624,
            width=1
        )
        self.line_object(
            x1=x,
            y1=428 + ((len(aspects) - 1) * 15),
            x2=x + 25 + ((len(aspects) - 2) * 25),
            y2=428 + ((len(aspects) - 1) * 15),
            width=1
        )
