from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *
def readFile(reservatiesysteem, fileName):
    """
    Leest een bestand met de geven naam in

    Preconditie: Het bestand moet bestaan
    Postconditie: Het bestand is ingelezen adhv de content worden er wijzigingen in het reservatiesysteem gedaan

    :param fileName: De naam van het in te lezen bestand
    :return: True als de operatie is gelukt, False als het niet gelukt is.
    """
    # open het bestand
    with open(fileName, "r") as file:
        # lees elke regel in het bestand
        for line in file:
            # als de regel begint met '#' sla de regel over
            if line.startswith("#"):
                continue
            else:
                # Kijk of de regel start met gebruiker zo ja dan maak je een gebruiker aan
                if (line.startswith("gebruiker")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    voornaam = parts[2]
                    achternaam = parts[3]
                    email = parts[4]
                    # Maak de gebruiker aan
                    gebruiker = Gebruiker(id, voornaam, achternaam, email)
                    tableItem = reservatiesysteem.users.createItem(gebruiker.id, gebruiker)
                    reservatiesysteem.users.tableInsert(tableItem)

                # Kijk of de regel start met zaal zo ja dan maak je een zaal aan
                if (line.startswith("zaal")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    zaalNummer = parts[1]
                    aantalPlaatsen = parts[2]
                    # Maak de zaal aan
                    zaal = Zaal(zaalNummer, aantalPlaatsen)
                    tableItem = reservatiesysteem.rooms.createItem(zaal.roomNumber, zaal)
                    reservatiesysteem.rooms.tableInsert(tableItem)

                # Kijk of de regel start met film zo ja dan maak je een film aan
                if (line.startswith("film")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    titel = parts[2]
                    rating = parts[3]
                    # Maak de film aan
                    film = Film(id, titel, rating)
                    tableItem = reservatiesysteem.movies.createItem(film.id, film)
                    reservatiesysteem.movies.tableInsert(tableItem)

                # Kijk of de regel start met vertoning zo ja dan maak je een vertoning aan
                if (line.startswith("vertoning")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    zaalNummer = parts[2]
                    slot = parts[3]
                    datum = parts[4]
                    filmId = parts[5]
                    vrijePlaatsen = parts[6]
                    # Maak de vertoning aan
                    vertoning = Vertoning(id, zaalNummer, slot, datum, filmId, vrijePlaatsen)
                    tableItem = reservatiesysteem.screenings.createItem(vertoning.id, vertoning)
                    reservatiesysteem.screenings.tableInsert(tableItem)