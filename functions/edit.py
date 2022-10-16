class Tables():
    def __init__(self, table_1, table_2):
        self.table_1 = table_1
        self.table_2 = table_2


    # Merging some table_1 informations to table_2
    def merge(self):
        #Handeling more Skladba or Žáci then the rest
        for i in range(len(self.table_1["Autor"])):
            if self.table_1["Č."][i] == 0.0 and self.table_1["Autor"] != 0:
                self.table_1["Autor"][i-1] = self.table_1["Autor"][i-1] + " \n" + self.table_1["Autor"][i]
                self.table_1["Skladba"][i - 1] = self.table_1["Skladba"][i - 1] + " \n" + self.table_1["Skladba"][i]
                self.table_1["Autor"][i] = 0
                self.table_1["Skladba"][i] = 0
        #Deleting empty strings
        for i in range(len(self.table_1["Autor"])):
            try:
                if self.table_1["Autor"][i] == 0:
                    del self.table_1["Autor"][i]
                    del self.table_1["Skladba"][i]
                    del self.table_1["Č."][i]

            except:
                i = i - 1
                if self.table_1["Autor"][i] == 0:
                    del self.table_1["Autor"][i]
                    del self.table_1["Skladba"][i]
                    del self.table_1["Č."][i]

        del self.table_2["Skladby"]
        #Merging itself
        self.table_2.update({"Skladba": []})
        self.table_2.update({"Autor": []})
        self.table_2["Skladba"] += self.table_1["Skladba"]
        self.table_2["Autor"] += self.table_1["Autor"]
        return(self.table_2)

    def sort(self):
        # Deletes unused lists
        del self.table_2["Poznámka"]
        del self.table_2["Učitel"]
        del self.table_2["Délka"]
        # Orders table corectly
        order = ("Číslo", "Autor", "Skladba", "Žák (žáci)", "Ročník", "Předmět")
        final_table = {}
        for i in order:
            final_table[i] = self.table_2[i]
        return (final_table)


    def format(self, type="korepetice"):
        # Merging Poznámka cells to Předmět cells and editing numbering system
        if type == "korepetice":
            for i in range(len(self.table_2["Poznámka"])):
                if self.table_2["Poznámka"][i] != 0.0:
                    self.table_2["Předmět"][i] = self.table_2["Předmět"][i] + " \n" + self.table_2["Poznámka"][i]
                self.table_2["Číslo"][i] = f'{self.table_2["Číslo"][i]}.'
        #editing number system only
        elif type == "numbers":
            for i in range(len(self.table_2["Číslo"])):
                self.table_2["Číslo"][i] = f'{self.table_2["Číslo"][i]}.'

    def get_class(self, classes):
        for i in range(len(self.table_2["Ročník"])):
            if "," not in self.table_2["Žák (žáci)"][i]:
                name = self.table_2["Žák (žáci)"][i].split(" ")
                for j in range(len(classes["Příjmení"])):
                    if classes["Příjmení"][j] == name[1] and classes["Jméno"][j] == name[0]:
                        if "," not in classes["Ročník"][j]:
                            self.table_2["Ročník"][i] = classes["Ročník"][j]
                        else:
                            rocnik = classes["Ročník"][j].split(",")
                            predmety = classes["Studium"][j].split(",")
                            for k in range(len(predmety)):
                                if predmety[k] == self.table_2["Předmět"][i]:
                                    self.table_2["Ročník"][i] = rocnik[k]
