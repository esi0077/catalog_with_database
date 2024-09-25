import mysql.connector # pip install mysql-connector-python

conn = mysql.connector.connect(
    host="10.2.2.136",
    user="test",
    password="test",
    database="telefonkatalog"
)
cursor = conn.cursor()
def visAlleperson():
    cursor.execute("SELECT * FROM person")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte person i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else:
        print("*****************************************"
              "*****************************************")
        for person in resultater:
            print("* Fornavn: {:15s} Etternavn: {:15s} Telfonnummer:{:8s}"
                  .format(person[0], person[1], person[2]))
        print("*****************************************"
              "*****************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()

# Funksjon som legger til en ny person i databasen
def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
    sql = f"INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES ({fornavn}, {etternavn}, {telefonnummer})"
    cursor.execute(sql)
    conn.commit()

# def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
#     cursor.execute("INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)",
#               (fornavn, etternavn, telefonnummer))
#     conn.commit()


# Funksjon som sletter en person fra databasen basert på fornavn, etternavn og telefonnummer
def slett_person_fra_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM person WHERE fornavn=? AND etternavn=? AND telefonnummer=?",
              (fornavn, etternavn, telefonnummer))
    conn.commit()


def printMeny():
    print("------------------- Telefonkatalog -------------------")
    print("| 1. Legg til ny person                              |")
    print("| 2. Søk opp person eller telefonnummer              |")
    print("| 3. Vis alle person                               |")
    print("| 4. Avslutt                                         |")
    print("------------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAlleperson()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            conn.close()
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4: ")
        utfoerMenyvalg(nyttForsoek)


def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")

    legg_til_person_i_db(fornavn, etternavn, telefonnummer) # Legger til informasjonen fra input-feltene i databasen som en ny rad
    # legg_til_person_i_db(fornavn, etternavn, telefonnummer) # Legger til informasjonen fra input-feltene i databasen som en ny rad

    print("{0} {1} er registrert med telefonnummer {2}"
          .format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


def sokPerson():
    print("1. Søk på fornavn")
    print("2. Søk på etternavn")
    print("3. Søk på telefonnummer")
    print("4. Tilbake til hovedmeny")
    sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
    if sokefelt == "1":
        navn = input("Fornavn: ")
        finnPerson("fornavn", navn)
    elif sokefelt == "2":
        navn = input("Etternavn: ")
        finnPerson("etternavn", navn)
    elif sokefelt == "3":
        tlfnummer = input("Telefonnummer: ")
        finnPerson("telefonnummer", tlfnummer)
    elif sokefelt == "4":
        printMeny()
    else:
        print("Ugyldig valg. Velg et tall mellom 1-4: ")
        sokPerson()


# typeSok angir om man søker på fornavn, etternavn, eller telefonnummer
def finnPerson(typeSok, sokeTekst): # Bonus: denne funksjonen kan skrives mye kortere. Se om du klarer å forbedre den.
    if typeSok == "fornavn":
        cursor.execute("SELECT * FROM person WHERE fornavn=?", (sokeTekst,))
    elif typeSok == "etternavn":
        cursor.execute("SELECT * FROM person WHERE etternavn=?", (sokeTekst,))
    elif typeSok == "telefonnummer":
        cursor.execute("SELECT * FROM person WHERE telefonnummer=?", (sokeTekst,))

    resultater = cursor.fetchall()

    if not resultater:
        print("Finner ingen person")
    else:
        for person in resultater:
            print("{0} {1} har telefonnummer {2}"
                  .format(person[0], person[1], person[2]))


printMeny()  # Starter programmet ved å skrive menyen første gang