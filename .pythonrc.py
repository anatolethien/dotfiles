# github.com/anatolethien/dotfiles

import os
import sys
import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from rich import pretty
pretty.install()

def clear():
    match platform.system():
        case 'Linux':
            os.system('clear')
        case 'Darwin':
            os.system('clear')
        case 'Windows':
            os.system('cls')

K = 1_000
M = 1_000_000
G = 1_000_000_000
