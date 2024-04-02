def cprint(text, color='white'):
    """
    Prints text in color.
    :param text: The text to print.
    :param color: The color to print the text in.
    """
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
    }
    print(colors[color] + text + colors['reset'])


cprint(f'\n>>> add liquidity GPX | {address_wallet} | {error}', 'red')
