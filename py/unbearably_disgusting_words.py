import random as rand

emo_noun = ["момент", "небо", "океан", "страницы", "море", "боль",
            "обрывки", "раны", "мир", "слёзы", "розы", "вены", "картины",
            "дождь", "километры", "осень", "вены", "ложь", "отражение",
            "рассвет", "x-ладони", "солнце", "пепел", "ангел"]

emo_attr = ["твоей", "фамили", "твоей", "вашей", "вскрытой", "истлевшей",
            "внутри", "после", "нашей", "потерянной", "среди", "глубине",
            "моей", "догоревшей", "покинутой", "растерзанной", "убитой",
            "зарытой", "забытой", "умирающей", "изнутри", "утраченной",
            "каждой", "разбитой", "догоревшей", "сгоревшей" ]

emo_noun2 = ["вечности", "бездейственности", "апатии", "глупости",
            "реальности", "страсти", "смерти", "любви", "гордости",
            "нежности", "боли", "смерти", "печали", "ненависти",
            "привязанности", "надежды", "зависти", "скорби", "эйфории",
            "ярости", "безмятежности", "веры", "мечты", "тревоги", "крови",
            "могилы", "игры", "пустоты", "бесконечности", "легкости"]

def emo_band_name():
    return emo_noun[rand.randint(0, len(emo_noun) - 1)] + " " + emo_attr[rand.randint(0, len(emo_attr) - 1)] + " " + emo_noun2[rand.randint(0, len(emo_noun2) - 1)]

if __name__ == '__main__':
    print(emo_band_name())
