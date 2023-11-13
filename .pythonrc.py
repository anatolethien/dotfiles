# github.com/anatolethien/dotfiles

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from rich import pretty
pretty.install()

def clear():
    os.system('clear')

def exit():
    os._exit(0)

K = 1_000
M = 1_000_000
G = 1_000_000_000
