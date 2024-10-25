from qiskit import QuantumCircuit, transpile
from qmiotools.integrations.qiskitqmio import QmioBackend

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc.draw()

backend = QmioBackend()
qct = transpile(qc, backend)

job = backend.run(qct, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("QmioBackend Counts:", counts)
