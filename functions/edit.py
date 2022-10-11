class Tables():
    def __init__(self, table_1, table_2):
        self.table_1 = table_1
        self.table_2 = table_2


    # Merging some table_1 informations to table_2
    def merge(self):
        #Handeling more Skladba or Žáci
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
        #formats number and korepetice
        if type == "korepetice":
            for i in range(len(self.table_2["Poznámka"])):
                if self.table_2["Poznámka"][i] != 0.0:
                    self.table_2["Předmět"][i] = self.table_2["Předmět"][i] + " \n" + self.table_2["Poznámka"][i]
                self.table_2["Číslo"][i] = f'{self.table_2["Číslo"][i]}.'
        #formats only number
        elif type == "numbers":
            for i in range(len(self.table_2["Číslo"])):
                self.table_2["Číslo"][i] = f'{self.table_2["Číslo"][i]}.'
        #I will continue here tommorow

