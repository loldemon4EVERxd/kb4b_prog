import csv
import matplotlib.pyplot as plt

def teploty_v_cr():
    path = "2. prace_se_soubory/data/teploty.csv"
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        temps = []
        years = []

        max_temp = 0
        max_year = 0
        for line in reader:
            if line["TIME"] == "AVG":
                temp = float(line["TEMPERATURE"])

                temps.append(temp)
                years.append(line["YEAR"])

                if temp > max_temp:
                    max_temp = temp
                    max_year = line["YEAR"]
        print(f"nejvyssi teplota: {max_temp}, v roce: {max_year}")

        plt.plot(years, temps, color="hotpink")
        plt.title("avg teploty v CR za roky 1961-2022")
        plt.xlabel("rok")
        plt.ylabel("teplota [°C]")
        plt.xticks(years[::5], rotation=45)
        plt.show()

def viry():
    path = "2. prace_se_soubory/data/vira_v_cesku.csv"
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        max_hodnota = 0
        nejlepsi_vira = 0
        naboz = 0

        for line in reader:
            if line["uzemi_txt"] == "Brno":
                hodnota = int(line["hodnota"])
                naboz += 1
                if hodnota > max_hodnota:
                    max_hodnota = hodnota
                    nejlepsi_vira = line["vira_txt"]
                

        print(f"{max_hodnota}, nejlepsi vira: {nejlepsi_vira}")
        print(f"pocet nabozenstvi pro Brno: {naboz-1}")


# teploty_v_cr()
viry()