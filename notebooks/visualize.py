import matplotlib.pylab as plt
from matplotlib.lines import Line2D
import numpy as np

def plot_data_in_feature_space(X, y, highlight_rows):
    X_m = np.ma.array(X, mask=False)
    X_m.mask[highlight_rows] = True

    y_m = np.ma.array(y, mask=False)
    y_m.mask[highlight_rows] = True

    fig, ax = plt.subplots(figsize=(12, 8))
    s1 = ax.scatter(X_m[:, 0], X_m[:, 1], c=y_m, cmap=plt.cm.tab10, marker="o", s=10)
    s2 = ax.scatter(
        X[highlight_rows, 0],
        X[highlight_rows, 1],
        c=y[highlight_rows],
        cmap=plt.cm.tab10,
        marker="X",
        s=80,
        edgecolors="k",
        vmin=0,
        vmax=9,
    )
    ax.legend(
        [
            Line2D(
                [0],
                [0],
                color="w",
                marker="X",
                markerfacecolor="w",
                markeredgecolor="k",
                markersize=10,
            ),
            Line2D(
                [0],
                [0],
                color="w",
                marker="o",
                markerfacecolor="w",
                markeredgecolor="k",
                markersize=6,
            ),
        ],
        ["Samples", "Dataset"],
        loc="lower right",
    )
    cbar = fig.colorbar(s2, ticks=(0.5 + np.arange(10)) * 10 / 11)
    cbar.ax.set_yticklabels(np.arange(10, dtype=int))
    cbar.ax.tick_params(size=0, labelsize="large")


def plot_dataset(X, y, rows=5):
    indices = np.stack(
        [
            np.random.choice(np.argwhere(y == i).ravel(), size=rows, replace=False)
            for i in range(10)
        ]
    )
    fig, axs = plt.subplots(rows, 11)
    for i in range(rows):
        axs[i][0].axis("off")
        axs[i][0].set_aspect("equal")
        for j in range(10):
            axs[i][j + 1].imshow(X[indices[j, i], :].reshape(8, 8), cmap="Greys")
            axs[i][j + 1].axis("off")
            axs[i][j + 1].set_aspect("equal")

    axs[0][0].set_title("label:")

    for j in range(10):
        axs[0][j + 1].set_title(f"{j}")

    fig.subplots_adjust(wspace=0, hspace=0)


def plot_numbers(X, y, title: str = None):
    fig, axs = plt.subplots(
        1,
        X.shape[0] + int(title != None),
        figsize=(X.shape[0] + int(title != None) + 1, 2),
    )
    fig.suptitle("Samples")
    if title:
        axs[0].axis("off")
        axs[0].set_title(title)
        axs[0].set_aspect("equal")
    if not isinstance(X, np.ndarray):
        X = X.to_numpy()
    if not isinstance(y, np.ndarray):
        y = y["class"]
    for i, (data, label) in enumerate(zip(X, y)):
        axs[i + int(title != None)].imshow(data.reshape(8, 8), cmap="Greys")
        axs[i + int(title != None)].axis("off")
        axs[i + int(title != None)].set_title(label)


def plot_results(
    clf, X_train, y_train, X_test, y_test, X_highlight, y_highlight, X_range, resolution
):
    xx, yy = np.meshgrid(
        np.linspace(X_range[0][0], X_range[0][1], resolution),
        np.linspace(X_range[0][0], X_range[0][1], resolution),
    )

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots(figsize=(12, 8))
    pc = ax.pcolor(xx, yy, Z.astype(int), cmap=plt.cm.tab10, alpha=0.5)

    s1 = ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.tab10, s=20, edgecolors="k"
    )
    s2 = ax.scatter(
        X_test[:, 0],
        X_test[:, 1],
        c=y_test,
        cmap=plt.cm.tab10,
        marker="v",
        s=30,
        edgecolors="k",
    )
    s3 = ax.scatter(
        X_highlight[:, 0],
        X_highlight[:, 1],
        c=y_highlight,
        cmap=plt.cm.tab10,
        marker="X",
        s=80,
        edgecolors="w",
        linewidth=2,
        vmin=0,
        vmax=9,
    )

    ax.legend(
        [
            Line2D(
                [0],
                [0],
                color="w",
                marker="o",
                markerfacecolor="w",
                markeredgecolor="k",
                lw=0,
            ),
            Line2D(
                [0],
                [0],
                color="w",
                marker="v",
                markerfacecolor="w",
                markeredgecolor="k",
                lw=0,
            ),
            Line2D(
                [0],
                [0],
                color="w",
                marker="X",
                markerfacecolor="w",
                markeredgecolor="k",
                markersize=10,
                lw=0,
            ),
        ],
        ["Training", "Test", "Samples"],
        loc="lower right",
    )

    cbar = fig.colorbar(s2, ticks=(0.5 + np.arange(10)) * 10 / 11)
    cbar.ax.set_yticklabels(np.arange(10, dtype=int))
    cbar.ax.tick_params(size=0, labelsize="large")