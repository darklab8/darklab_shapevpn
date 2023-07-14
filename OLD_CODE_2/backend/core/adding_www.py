def adding_www(allowed_origin):
    """
    >>> adding_www("https://light-search.com")
    "https://www.light-search.com"
    """
    return allowed_origin.replace("//", "//www.")


print(adding_www("https://light-search.com"))
