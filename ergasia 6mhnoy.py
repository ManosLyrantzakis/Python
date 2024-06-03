import json
import os.path


def InsertPerson(_persons):
    print("\n ΕΙΣΑΓΩΓΗ ΣΤΟΙΧΕΙΩΝ ΑΝΘΡΩΠΟΥ \n")

    while True:
        person = {}
        found = False

        while True:
            found = False
            code = input(
                "Πληκτολογήστε έναν αριθμό ή '0' για επιστροφή στο αρχικό μενού : "
            )
            for p in _persons:
                if p["code"] == code:
                    found = True
                    break
            if found == False:
                break
        person["code"] = code
        if person["code"] == "0":
            break
        person["name"] = input("Εισάγετε όνομα χρήστη : ")
        person["surname"] = input("Εισάγετε επώνυμο χρήστη : ")
        person["email"] = input("Εισάγετε το  Email σας : ")
        person["phone"] = input("Εισάγετε τον αριθμό κινητού τηλεφώνου σας : ")
        _persons.append(person)
        print("\t\tΤα στοιχεία καταχωρήθηκαν επιτυχώς !\n")


def EditPerson(_persons):
    print("\n ΔΙΟΡΘΩΣΗ ΣΤΟΙΧΕΙΩΝ ΑΝΘΡΩΠΟΥ \n")
    while True:
        ViewPerson(persons)
        code = input(
            "Εισάγετε έναν αριθμό ανθρώπου  ή '0' για επιστροφή στο κύριο μενού: "
        )

        if code == "0":
            break
        for p in _persons:
            if p["code"] == code:
                print(
                    f"""
                Ποιο στοιχείο θέλετε να επεξεργαστείτε ; ")
                1. Id 
                2. Όνομα
                3. Επώνυμο
                4. Email
                5. Αριθμός κινητού τηλεφώνου
                """
                )
                epilogi = int(input("Διάλεξτε απο 1 εως 5: "))
                match epilogi:
                    case 1:
                        p["code"] = input("Εισάγετε νέο Id :")
                    case 2:
                        p["name"] = input("Εισάγετε νέο όνομα: ")
                    case 3:
                        p["surname"] = input("Εισάγετε νέο επώνυμο : ")
                    case 4:
                        p["email"] = input("Εισάγετε νέο Email : ")
                    case 5:
                        p["phone"] = input("Εισάγετε νέο αριθμό κινητού : ")
                print("\tΤα στοιχεία επεξεργάστηκαν επιτυχώς !")
                print(
                    f"""Θέλετε οι αλλαγές να αποθηκευτούν και στο αρχείο ;
                1.Ναι
                2.Οχι
                 """
                )
                choice = input(" ")
                if choice == "1":
                    SavePerson(_persons)
                elif choice == "2":
                    break


def DeletePerson(_persons):
    print("\n ΔΙΑΓΡΑΦΗ KΑΤΑΧΩΡΙΜΕΝΩΝ ΣΤΟΙΧΕΙΩΝ \n")
    ViewPerson(persons)
    while True:

        code = input("Πληκτρολογήστε αριθμό για διαγραφή ή '0' για έξοδο: ")
        if code == "0":
            break
        for p in _persons:
            if p["code"] == code:
                print(
                    f="""
                Είστε σίγουρος οτι θέλετε να διαγράψετε τα στοιχεία ;
                1.Ναι 
                2.Οχι
                """
                )
            choice = input("")
            if choice == "1":
                persons.remove(p)
                print("\t\tΤα στοιχεία διαγράφηκαν επιτυχώς")
                print(
                    """Θέλετε οι αλλαγές να αποθηκευτούν ;
                               1.Ναι
                               2.Οχι
                                """
                )
                choice2 = input(" ")
                if choice2 == "1":
                    SavePerson(_persons)
                elif choice2 == "2":
                    break
            else:
                break


def SavePerson(_persons):
    print("\n  ΑΠΟΘΗΚΕΥΣΗ ΣΤΟΙΧΕΙΩΝ  \n")

    f = open("persons.txt", "w")
    for p in _persons:
        str_p = json.dumps(p)
        f.write(str_p + "\n")
    f.close()
    print("\n\t\t\tΗ αποθήκευση ολοκληρώθηκε ! \n")


def ViewPerson(persons):
    for p in persons:
        print(
            f""""
        Pin : {p["code"]}
        Όνομα : {p["name"]}
        Επώνυμο : {p["surname"]}  
        Email : {p["email"]}
        Αριθμός Κινητού : {p["phone"]}  """
        )


def ReadPerson():
    persons = []
    if os.path.isfile("persons.txt"):
        f = open("persons.txt", "r")
        for line in f.readlines():
            persons.append(json.loads(line))
    return persons


persons = ReadPerson()
while True:
    print(
        f"""
          1.Εισαγωγή Στοιχείων!
          2.Αποθηκεύση Στοιχείων!
          3.Διαγραφή Στοιχείων!
          4.Διώρθωση Στοιχείων!
          5.Εμφάνιση Στοιχείων!
          6.Εξοδος απο την εφαρμογή!
         """
    )
    option = int(input("Δώσε επιλογή απο 1 έως 6 : "))
    match option:
        case 1:
            InsertPerson(persons)
        case 2:
            SavePerson(persons)
        case 3:
            DeletePerson(persons)
        case 4:
            EditPerson(persons)
        case 5:
            ViewPerson(persons)
        case 6:
            exit()
