class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BYELLOW = '\033[43m'
    BBLUE = '\033[44m'
    BGREEN = '\033[42m'
    BRED = '\033[41m'


def warn(text):
    return(color.YELLOW + text + color.END)

def success(text):
    return(color.GREEN + text + color.END)

def error(text):
    return(color.RED + text + color.END)

def underline(text):
    return(color.UNDERLINE + text + color.END)