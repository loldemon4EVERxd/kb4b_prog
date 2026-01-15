import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("3. strojove_uceni/data/bmi.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in csv.DictReader(file):
        Y.append(int(row["Index"]))
        # Na vstupu mohou být jen číselné vstupy:
        if row["Gender"] == "Male":
            gender = 0
        else:
            gender = 1

        height = int(row["Height"])
        weight = int(row["Weight"])

        X.append([gender, height, weight])


neuralink = MLPClassifier(
    hidden_layer_sizes=(5, 4, 2),
    activation="relu",
    max_iter=5000,
)

x_train = X[:round(0.8 * len(X))]
y_train = Y[:round(0.8 * len(Y))]

x_test = X[round(0.8 * len(X)):]
y_test = Y[round(0.8 * len(Y)):]

neuralink.fit(x_train, y_train)
prediction = neuralink.predict(x_test)
count = len(prediction)

correct = 0
for i in range(len(prediction)):
    if y_test[i] == prediction[i]:
        correct += 1

print(f"pomer spravnych odpovedi: {round(correct)/count*100}%")