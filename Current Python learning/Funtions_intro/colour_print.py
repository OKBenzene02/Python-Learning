import colorama

# some `ANSI` escape sequences for colours and effects

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'



def colour_print(text: str, *effects: str) -> None:
    """
    To print out texts with effects using ANSI sequence.
    :param text: to print out texts.
        using the ANSI sequence.
    :param effects: this will print out the effects the we
        want to our texts
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello red", RED)
colour_print("Hello red in bold", RED, BOLD, REVERSE)
print("this should be in default terminal colour")
colour_print("Hello white", BLACK)
colour_print("Hello black", WHITE)
colour_print("Hello cyan", CYAN)

colour_print("Hello, hello reverse", REVERSE)
colour_print("Hello underlined", UNDERLINE)
colorama.deinit()




