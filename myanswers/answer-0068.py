from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def comparar_svc_lineal_vs_rbf(X, y):
    model_linear = SVC(kernel="linear")
    model_rbf = SVC(kernel="rbf")

    model_linear.fit(X, y)
    model_rbf.fit(X, y)

    acc_linear = accuracy_score(y, model_linear.predict(X))
    acc_rbf = accuracy_score(y, model_rbf.predict(X))

    if acc_linear > acc_rbf:
        return "linear"
    elif acc_rbf > acc_linear:
        return "rbf"
    else:
        return "empate"
