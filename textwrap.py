import textwrap  # to format text


def wrapfunc(text):
    """
    this func wraps text so it prints more nicely in the terminal. 
    Then it prints it.
    """
    paragraphs = text.split("\n")
    for paragraph in paragraphs:
        paragraph = textwrap.dedent(paragraph)  # this removes any tabs
        paragraph = "\t" + paragraph  # this adds indents at the start of each para
        lines = textwrap.wrap(paragraph, width=120, drop_whitespace=False)
        for line in lines:
            print(line)
