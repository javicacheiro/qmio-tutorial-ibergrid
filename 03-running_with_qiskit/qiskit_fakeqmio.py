from qiskit import QuantumCircuit, transpile
from qmiotools.integrations.qiskitqmio import FakeQmio

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc.draw()

backend = FakeQmio()

qct = transpile(qc, backend)
qct.draw(idle_wires=False)

job = backend.run(qct, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("FakeQmio Counts:", counts)
