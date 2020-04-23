# -*- coding: utf-8 -*-

from .zodiac import Zodiac
from .canvas import Canvas
from .modules import (
    tk, plt, mean, array, num2date, button_press_handler,
    FigureCanvasTkAgg, NavigationToolbar2Tk
)


def on_key_press(event, canvas, toolbar, lat, lon):
    if event.dblclick:
        toplevel = tk.Toplevel(master=None, bg="white")
        toplevel.resizable(width=False, height=False)
        date = num2date(event.xdata)
        frame = tk.Frame(master=toplevel, bg="white")
        frame.pack(side="left", fill="both")
        for i, (j, k, m) in enumerate(
                zip(
                    ["Date", "Latitude", "Longitude"],
                    [":"] * 3,
                    [date.strftime("%Y.%m.%d %H:%M:%S"), lat, lon]
                )
        ):
            title = tk.Label(
                master=frame, text=j, font="Default 11 bold", bg="white"
            )
            title.grid(row=i, column=0, sticky="w")
            dot = tk.Label(
                master=frame, text=k, font="Default 11 bold", bg="white"
            )
            dot.grid(row=i, column=1, sticky="w")
            label = tk.Label(master=frame, text=m, bg="white")
            label.grid(row=i, column=2, sticky="w")
        try:
            zodiac = Zodiac(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=date.hour,
                minute=date.minute,
                second=date.second,
                lat=lat,
                lon=lon,
                hsys="P"
            ).patterns()
        except AttributeError:
            zodiac = Zodiac(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=date.hour,
                minute=date.minute,
                second=date.second,
                lat=19.63,
                lon=15.99,
                hsys="P"
            ).patterns()
        Canvas(master=toplevel, zodiac=zodiac)
        button_press_handler(event, canvas, toolbar)


def plot_data(
        master: tk.Frame = None,
        x: tuple = (), 
        y: tuple = (),
        country: str = "",
        title: str = "",
        compare: bool = False,
        coordinates: list = []
):
    lat = round(sum(i[0] for i in coordinates) / len(coordinates), 2)
    lon = round(sum(i[1] for i in coordinates) / len(coordinates), 2)
    for child in master.winfo_children():
        child.destroy()
    master.master.update()
    x = array(x)
    if compare:
        y = [array(i) for i in y]
    else:
        y = [array(y)]
    ax = plt.subplot2grid((1, 1), (0, 0))
    colors = [
        "#F005D1",
        "#0525F0",
        "#5EFF00",
        "#F7FF00",
        "#FF8900",
    ]
    countries = country.split(",")
    for i in range(len(y)):
        if compare:
            ax.plot_date(
                x=x,
                y=y[i],
                fmt="-",
                color=colors[i],
                label=countries[i].split("(")[0],
                linewidth=0.7
            )
        else:
            ax.plot_date(
                x=x,
                y=y[i],
                fmt="-",
                color=colors[i],
                label=country.split("(")[0],
                linewidth=0.7
            )
            ax.fill_between(
                x,
                y[i],
                mean(y[i]),
                where=(y[i] > mean(y[i])),
                color="green",
                alpha=0.7,
                label="above average"
            )
            ax.fill_between(
                x,
                y[i],
                mean(y[i]),
                where=(y[i] < mean(y[i])),
                color="red",
                alpha=0.7,
                label="below average"
            )
            ax.axhline(mean(y[i]), color="cyan", linewidth=2)
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)
        ax.tick_params(axis="x", colors="red")
        ax.tick_params(axis="y", colors="purple")
    plt.grid(
        True,
        color="black",
        linestyle="-",
        linewidth=1
    )
    plt.subplots_adjust(
        left=0.2,
        bottom=0.2,
        right=0.9,
        top=0.9,
        wspace=0.2,
        hspace=0
    )
    plt.xlabel("Timeline")
    plt.ylabel(title)
    plt.title(country)
    plt.legend()
    canvas = FigureCanvasTkAgg(ax.figure, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP)
    toolbar = NavigationToolbar2Tk(canvas, master)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP)
    canvas.mpl_connect(
        "button_press_event",
        lambda event: on_key_press(event, canvas, toolbar, lat, lon)
    )
