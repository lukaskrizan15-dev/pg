def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    # 1. Kontrola, zda je pozice na šachovnici.
    radek, sloupec = cilova_pozice
    if radek < 1 or radek > 8 or sloupec < 1 or sloupec > 8:
        return False

    # 2. Kontrola, zda je cílové políčko volné.
    if cilova_pozice in obsazene_pozice:
        return False

    rozdil_radku = abs(radek - aktualni_pozice[0])
    rozdil_sloupce = abs(sloupec - aktualni_pozice[1])

    # 3. Pohyb krále.
    if typ == "král":
        return (rozdil_radku <= 1 and rozdil_sloupce <= 1
                and (rozdil_radku != 0 or rozdil_sloupce != 0))

    # 4. Pohyb jezdce.
    elif typ == "jezdec":
        return ((rozdil_radku == 2 and rozdil_sloupce == 1)
                or (rozdil_radku == 1 and rozdil_sloupce == 2))

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))
    print(je_tah_mozny(jezdec, (4, 5), obsazene_pozice))
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice))