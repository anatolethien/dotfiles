# github.com/anatolethien/dotfiles

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from rich import pretty
pretty.install()

def clear():
    import os
    import platform
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
