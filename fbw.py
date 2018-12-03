import pymysql


class DBConnect:
    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost","root","N3uromancer","fbw")
            print("POLACZENIE USTANOWIONE")
            self.menu()
            self.conn.close()
        except:
            print("POLACZENIE NIEUDANE, PODAJ PONOWNIE DANE")

    def menu(self):

        print("########################################")
        print("### WITAJ W SYSTEMIE ZARZADZANIA FBW ###")
        print("########################################")

        dec = input("podaj tabele na której chcesz pracować 1-pracownicy, 2-klienci, 3-samoloty, q-wyjśie")

        while (True):
            if (dec == "1"):
                self.emplo()
                dec = input(
                    "podaj tabele na której chcesz pracować 1-pracownicy, 2-klienci, 3-samoloty, q-wyjśie")
            elif (dec == "2"):
                self.clien()
                dec = input(
                    "podaj tabele na której chcesz pracować 1-pracownicy, 2-klienci, 3-samoloty, q-wyjśie")
            elif (dec == "3"):
                self.planes()
                dec = input(
                    "podaj tabele na której chcesz pracować 1-pracownicy, 2-klienci, 3-samoloty, q-wyjśie")
            elif (dec == "q"):
                print("KONIEC PROGRAMU")
                break
            else:
                print("NIEPOPRAWNY INPUT")

    ########################
    ########################
    #### MODOL EMPLOYEE ####
    ########################
    ########################

    def emplo(self):
        print("########################")
        print("### MODUŁ PRACOWNICY ###")
        print("########################")

        dec = input("Podaj polecenie do wykonania\ns-pokaż pracowników\ni-dodaj pracownika\nd-usuń pracownika\nq-powrót do menu głównego")
        while (True):
            if (dec == "s"):
                self.selectEmplo()
                dec = input("\n Podaj polecenie do wykonania s-pokaż pracowników\ni-dodaj pracownika\nd-usuń pracownika\nq-powrót do menu głównego")
            elif (dec == "i"):
                self.insertEmplo()
                dec = input("\n Podaj polecenie do wykonania s-pokaż pracowników\ni-dodaj pracownika\nd-usuń pracownika\nq-powrót do menu głównego")
            elif (dec == "d"):
                self.deleteEmplo()
                dec = input("\n Podaj polecenie do wykonania s-pokaż pracowników\ni-dodaj pracownika\nd-usuń pracownika\nq-powrót do menu głównego")
            elif (dec == "q"):
                print("POWRÓT DO MENU")
                self.menu()
            else:
                print("NIEPOPRAWNY INPUT")



    def selectEmplo(self):
        self.cursor.execute("SELECT * FROM fbw.pracownicy;")
        pracownicy = self.cursor.fetchall()
        i = 1
        for row in pracownicy:
            print(i, row[1], row[2], row[3], row[4])
            i += 1
        self.emplo()


    def insertEmplo(self):
        imie = input("Podaj Imie")
        nazwisko=input("Podaj Nazwisko")
        stanowisko=input("podaj stanowisko")
        id_licencji_p=input("podaj id licencji")

        self.cursor.execute("INSERT INTO pracownicy (imie, nazwisko, pesel, data_ur) VALUES (%s,%s,%s,%s)", (imie,nazwisko,stanowisko,id_licencji_p))
        self.conn.commit()

    def _check_emplo_valid_id(self, pesel):

        pracownik = self.cursor.execute("SELECT * FROM pracownicy WHERE pesel = %s", pesel)

        allResults = self.cursor.fetchall()

        if (len(allResults) == 1):
            return True
        else:
            return False

    def deleteEmplo(self):
        id = input("Podaj Id pracownika do usuniecia")
        self.select()
        if (self._check_emplo_valid_id(id) == True):
            self.cursor.execute("DELETE FROM pracownicy WHERE id = %s", id)

            dec = input("CZY NA PEWNO USUNAC? T/N")

            if (dec == "T"):
                self.conn.commit()
                print("usunieto pracownika")
            else:
                self.conn.rollback()
                print("cofnieto zmiany")
        else:
            print("\n Błędne ID \n")
            self.deleteEmplo()

    ########################
    ########################
    #### MODOL CLIENT ######
    ########################
    ########################

    def clien(self):
        print("########################")
        print("### MODUŁ KLIENCI ######")
        print("########################")

        dec = input("Podaj polecenie do wykonania\ns-pokaż klientów\ni-dodaj klienta\nd-usuń klienta\nq-powrót do menu głównego")
        while (True):
            if (dec == "s"):
                self.selectClien()
                dec = input("\n Podaj polecenie do wykonania\ns-pokaż klientów\ni-dodaj klienta\nd-usuń klienta\nq-powrót do menu głównego")
            elif (dec == "i"):
                self.insertClien()
                dec = input("\n Podaj polecenie do wykonania\ns-pokaż klientów\ni-dodaj klienta\nd-usuń klienta\nq-powrót do menu głównego")
            elif (dec == "d"):
                self.deleteClien()
                dec = input("\n Podaj polecenie do wykonania\ns-pokaż klientów\ni-dodaj klienta\nd-usuń klienta\nq-powrót do menu głównego")
            elif (dec == "q"):
                print("POWRÓT DO MENU")
                self.menu()
            else:
                print("NIEPOPRAWNY INPUT")

    def selectClien(self):
        self.cursor.execute("SELECT * FROM fbw.klienci;")
        klienci = self.cursor.fetchall()
        i = 1
        for row in klienci:
            print(i, row[1], row[2], row[3])
            i += 1
        self.clien()


    def insertClien(self):
        imie = input("Podaj Imie")
        nazwisko=input("Podaj Nazwisko")
        id_licencji=input("podaj podaj id licencji klienta")

        self.cursor.execute("INSERT INTO klienci (imie_k, nazwisko_k, id_licencji_k) VALUES (%s,%s,%s)", (imie,nazwisko,id_licencji))
        self.conn.commit()

    def _check_clien_valid_id(self, id):

        klient = self.cursor.execute("SELECT * FROM pracownicy WHERE id = %s", id)

        allResults = self.cursor.fetchall()

        if (len(allResults) == 1):
            return True
        else:
            return False

    def deleteClien(self):
        id = input("Podaj Id klienta do usuniecia")
        self.select()
        if (self._check_clien_valid_id(id) == True):
            self.cursor.execute("DELETE FROM klienci WHERE id = %s", id)

            dec = input("CZY NA PEWNO USUNAC? T/N")

            if (dec == "T"):
                self.conn.commit()
                print("usunieto klienta")
            else:
                self.conn.rollback()
                print("cofnieto zmiany")
        else:
            print("\n Błędne ID \n")
            self.deleteClien()




db = DBConnect()


