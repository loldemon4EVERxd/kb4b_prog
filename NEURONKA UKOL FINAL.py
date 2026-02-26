import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("data/games.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        gamedur = float(row["gameDuration"])
        winner = int(row["winner"])

        firstBlood = int(row["firstBlood"])
        firstTower = int(row["firstTower"])
        firstInhibitor = int(row["firstInhibitor"])
        firstBaron = int(row["firstBaron"])
        firstDragon = int(row["firstDragon"])
        firstRiftHerald = int(row["firstRiftHerald"])

        t1_champ1id = int(row["t1_champ1id"])
        t1_champ1_sum1 = int(row["t1_champ1_sum1"])
        t1_champ1_sum2 = int(row["t1_champ1_sum2"])
        t1_champ2id = int(row["t1_champ2id"])
        t1_champ2_sum1 = int(row["t1_champ2_sum1"])
        t1_champ2_sum2 = int(row["t1_champ2_sum2"])
        t1_champ3id = int(row["t1_champ3id"])
        t1_champ3_sum1 = int(row["t1_champ3_sum1"])
        t1_champ3_sum2 = int(row["t1_champ3_sum2"])
        t1_champ4id = int(row["t1_champ4id"])
        t1_champ4_sum1 = int(row["t1_champ4_sum1"])
        t1_champ4_sum2 = int(row["t1_champ4_sum2"])
        t1_champ5id = int(row["t1_champ5id"])
        t1_champ5_sum1 = int(row["t1_champ5_sum1"])
        t1_champ5_sum2 = int(row["t1_champ5_sum2"])

        t1_towerKills = int(row["t1_towerKills"])
        t1_inhibitorKills = int(row["t1_inhibitorKills"])
        t1_baronKills = int(row["t1_baronKills"])
        t1_dragonKills = int(row["t1_dragonKills"])
        t1_riftHeraldKills = int(row["t1_riftHeraldKills"])

        t1_ban1 = int(row["t1_ban1"])
        t1_ban2 = int(row["t1_ban2"])
        t1_ban3 = int(row["t1_ban3"])
        t1_ban4 = int(row["t1_ban4"])
        t1_ban5 = int(row["t1_ban5"])

        t2_champ1id = int(row["t2_champ1id"])
        t2_champ1_sum1 = int(row["t2_champ1_sum1"])
        t2_champ1_sum2 = int(row["t2_champ1_sum2"])
        t2_champ2id = int(row["t2_champ2id"])
        t2_champ2_sum1 = int(row["t2_champ2_sum1"])
        t2_champ2_sum2 = int(row["t2_champ2_sum2"])
        t2_champ3id = int(row["t2_champ3id"])
        t2_champ3_sum1 = int(row["t2_champ3_sum1"])
        t2_champ3_sum2 = int(row["t2_champ3_sum2"])
        t2_champ4id = int(row["t2_champ4id"])
        t2_champ4_sum1 = int(row["t2_champ4_sum1"])
        t2_champ4_sum2 = int(row["t2_champ4_sum2"])
        t2_champ5id = int(row["t2_champ5id"])
        t2_champ5_sum1 = int(row["t2_champ5_sum1"])
        t2_champ5_sum2 = int(row["t2_champ5_sum2"])

        t2_towerKills = int(row["t2_towerKills"])
        t2_inhibitorKills = int(row["t2_inhibitorKills"])
        t2_baronKills = int(row["t2_baronKills"])
        t2_dragonKills = int(row["t2_dragonKills"])
        t2_riftHeraldKills = int(row["t2_riftHeraldKills"])

        t2_ban1 = int(row["t2_ban1"])
        t2_ban2 = int(row["t2_ban2"])
        t2_ban3 = int(row["t2_ban3"])
        t2_ban4 = int(row["t2_ban4"])
        t2_ban5 = int(row["t2_ban5"])  

        X.append ([gamedur, firstBlood, firstTower, firstInhibitor, firstBaron, firstDragon, firstRiftHerald,
                  t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2,
                  t1_champ3id, t1_champ3_sum1, t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2,
                  t1_champ5id, t1_champ5_sum1, t1_champ5_sum2,
                  t1_towerKills, t1_inhibitorKills, t1_baronKills, t1_dragonKills, t1_riftHeraldKills,
                  t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5,
                  t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2,
                  t2_champ3id, t2_champ3_sum1, t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2,
                  t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
                  t2_towerKills, t2_inhibitorKills, t2_baronKills, t2_dragonKills, t2_riftHeraldKills,
                  t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5])
        # X.append ([gamedur, firstBlood, firstTower, firstInhibitor, firstBaron, firstDragon, firstRiftHerald,
        #           t1_champ1id, t1_champ1_sum1, t1_champ1_sum2, t1_champ2id, t1_champ2_sum1, t1_champ2_sum2,
        #           t1_champ3id, t1_champ3_sum1, t1_champ3_sum2, t1_champ4id, t1_champ4_sum1, t1_champ4_sum2,
        #           t1_champ5id, t1_champ5_sum1, t1_champ5_sum2,
        #           t1_towerKills, t1_inhibitorKills, t1_baronKills, t1_dragonKills, t1_riftHeraldKills,
        #           t1_ban1, t1_ban2, t1_ban3, t1_ban4, t1_ban5,
        #           t2_champ1id, t2_champ1_sum1, t2_champ1_sum2, t2_champ2id, t2_champ2_sum1, t2_champ2_sum2,
        #           t2_champ3id, t2_champ3_sum1, t2_champ3_sum2, t2_champ4id, t2_champ4_sum1, t2_champ4_sum2,
        #           t2_champ5id, t2_champ5_sum1, t2_champ5_sum2,
        #           t2_towerKills, t2_inhibitorKills, t2_baronKills, t2_dragonKills, t2_riftHeraldKills,
        #           t2_ban1, t2_ban2, t2_ban3, t2_ban4, t2_ban5])
        Y.append(winner)


# ---------- Ruční rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(32, 16, 8, 4),
    activation="logistic",
    max_iter=400,
    verbose=True
)

test_number = 1
for i in range(test_number):
    neural_network.fit(trening_X, trening_Y)

    # ---------- Vyhodnocení ----------
    results = neural_network.predict(test_X)

    correct = 0
    for i in range(len(results)):
        if test_Y[i] == results[i]:
            correct += 1
    print(correct / len(results))

    print(confusion_matrix(test_Y, results))
    ConfusionMatrixDisplay.from_predictions(test_Y, results)
    plt.show()