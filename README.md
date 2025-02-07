# Quickstart 2025
Some code examples for the Quickstart 2025 Winter School on QML.

Makes sure you create a local virtual environment by suing [uv](https://docs.astral.sh/uv/) or simply installing the _requirements.txt_ file.

```
python3 -m venv .venv
source .venb/bin/activate
(.venv) pip install -r requirements.txt
```

## Outline

Under the [notebooks](./notebooks/) folder, you will find a set of notebooks and some exercises to master some basic concepts in order to master the field.

* _Section 0_: [Basic stuff](./notebooks/0%20-%20Qubits%20and%20gates.ipynb) around qubits and gates so that you can practice simulating using pure Numpy, specialized software like QuTip or Qiskit (among others). Also, a 101 on [Adiabatic Quantum Computing](./notebooks/0.1%20-%20Adiabatic%20Quantum%20Computing.ipynb).
* _Section 1_: We should understand that working with classical data requires some transformations. Going down the [Quantum Embeddings](./notebooks/1%20-%20Quantum%20embeddings.ipynb) and how to evaluate their fitness to the task at hand with metrics such as [Target Alignment](./notebooks/1.1%20-%20Target%20alignment%20on%20quantum%20kernels.ipynb).
* _Section 2_: On [dimensionality reduction](./notebooks/2%20-%20Dimensionality%20reduction.ipynb) and how to squeeze all the information that is available into a set of qubits we can easily simulate using our devices.
* _Section 3_: Understanding [trainable embeddings](./notebooks/3.1%20-%20Trainable%20embeddings.ipynb) and how these can be used to improve hybrid (quantum and classical) models like [QSVMs](./notebooks/3.2%20-%20Trainable%20Kernels%20and%20classical%20models.ipynb).
* _Section 4_: Pure quantum approaches like [Quantum Neural Networks](./notebooks/4%20-%20Quantum%20Neural%20Networks.ipynb).