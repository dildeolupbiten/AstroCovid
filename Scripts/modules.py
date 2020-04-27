# -*- coding: utf-8 -*-

import os
import csv
import ssl
import tkinter as tk
import swisseph as swe
import matplotlib.pyplot as plt

from os import listdir
from dateutil import tz
from numpy import array
from pytz import timezone
from os.path import exists
from statistics import mean
from math import cos, sin, radians
from urllib.request import urlopen
from datetime import datetime as dt
from matplotlib.dates import num2date
from tkinter.ttk import Treeview as Tv
from tkinter.messagebox import showinfo
from xlsxwriter.workbook import Workbook
from timezonefinder import TimezoneFinder
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk
)
from tkinter.filedialog import askopenfilename as ask
from matplotlib.backend_bases import button_press_handler

