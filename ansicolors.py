class AnsiColors:

    # Reset
    reset = "\u001b[0m"

    # === Cores de frente ===

    # Cores básicas
    fg_black = "\u001b[30m"
    fg_red = "\u001b[31m"
    fg_green = "\u001b[32m"
    fg_yellow = "\u001b[33m"
    fg_blue = "\u001b[34m"
    fg_magenta = "\u001b[35m"
    fg_cyan = "\u001b[36m"
    fg_white = "\u001b[37m"

    # Cores brilhantes
    fg_bright_black = "\u001b[30;1m"
    fg_bright_red = "\u001b[31;1m"
    fg_bright_green = "\u001b[32;1m"
    fg_bright_yellow = "\u001b[33;1m"
    fg_bright_blue = "\u001b[34;1m"
    fg_bright_magenta = "\u001b[35;1m"
    fg_bright_cyan = "\u001b[36;1m"
    fg_bright_white = "\u001b[37;1m"

    # === Cores de fundo ===

    # Cores básicas
    bg_black = "\u001b[40m"
    bg_red = "\u001b[41m"
    bg_green = "\u001b[42m"
    bg_yellow = "\u001b[43m"
    bg_blue = "\u001b[44m"
    bg_magenta = "\u001b[45m"
    bg_cyan = "\u001b[46m"
    bg_white = "\u001b[47m"

    # Cores brilhantes
    bg_bright_black = "\u001b[40;1m"
    bg_bright_red = "\u001b[41;1m"
    bg_bright_green = "\u001b[42;1m"
    bg_bright_yellow = "\u001b[43;1m"
    bg_bright_blue = "\u001b[44;1m"
    bg_bright_magenta = "\u001b[45;1m"
    bg_bright_cyan = "\u001b[46;1m"
    bg_bright_white = "\u001b[47;1m"

    # === Decorations ===
    font_bold = "\u001b[1m"
    font_underline = "\u001b[4m"
    font_reversed = "\u001b[7m"

    # Reseta a cor do console
    def reset_terminal():
        print(f'{AnsiColors.reset}', end='')

# Exemplo de uso -> print(AnsiColors.red + "Este texto será imprimido vermelho! ")