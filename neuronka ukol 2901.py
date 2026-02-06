import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("data/MatchStatsTbl.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        win = int(row["Win"])

        X.append(pass)
        Y.append([win])


# ---------- Ruční rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(64, 32, 16, 8, 4),
    activation="relu",
    max_iter=1000,
    # verbose=True
)


test_number = 20
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

