def lang_genoeg(lengte: int) -> str:
    if lengte >= 120:
        return 'Je bent lang genoeg voor de attractie!'

    return 'Sorry, je bent te klein!'

print(lang_genoeg(110))