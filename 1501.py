# Neuronová síť predikující BMI kategorii 
# Jedná se pouze o učební ukázku - pro BMi je jinak využití neuronky nevhodné
# MAX ZATIM 0.8292682926829268

import csv

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("3. strojove_uceni/data/heart.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = float(row["age"])
        sex = float(row["sex"])
        cp = float(row["cp"])
        trestbps = float(row["trestbps"])
        chol = float(row["chol"])
        # fbs = float(row["fbs"])
        restecg = float(row["restecg"])
        thalach = float(row["thalach"])
        exang = float(row["exang"])
        # oldpeak = float(row["oldpeak"])
        # slope = float(row["slope"])
        ca = float(row["ca"])
        thal = float(row["thal"])
        # Na vstupu mohou být jen číselné vstupy:
        heart_disease = int(row["heart_disease"])

        X.append([age, sex, cp, trestbps, chol, restecg, thalach, exang, ca, thal])
        Y.append(heart_disease)


# ---------- Ruční rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(100, 1, 200),
    activation="logistic",
    max_iter=400,
    verbose=False
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

    # print(confusion_matrix(test_Y, results))

