def banner_text(text=" ", screen_width=80):
    """
    This programme is to create a banner with asterisks
    :param text: the string to print.
        asterisks are used to the beginning of
        the sentence and at the end of the sentence like `(**)`
        where the sentences are to be centered.
    :param screen_width: the overall width to printed is
        within the 4 blanks. `(**)`
    :return: raises a value error when the string is long
        enough to fit in.
    """

    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than the specified width"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", )
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)

