# -*- coding: utf-8 -*-

import os
import csv
import ssl
import tkinter as tk
import matplotlib.pyplot as plt
import swisseph as swe

from math import cos, sin, radians
from dateutil import tz
from pytz import timezone
from numpy import array
from os import listdir
from os.path import exists
from statistics import mean
from urllib.request import urlopen
from matplotlib.dates import num2date
from matplotlib.figure import Figure
from datetime import datetime as dt
from tkinter.ttk import Treeview as Tv
from tkinter.messagebox import showinfo
from xlsxwriter.workbook import Workbook
from timezonefinder import TimezoneFinder
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk
)
from tkinter.filedialog import askopenfilename as ask
from matplotlib.backend_bases import button_press_handler

