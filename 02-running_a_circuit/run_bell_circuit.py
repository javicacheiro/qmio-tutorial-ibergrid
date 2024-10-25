from qmio import QmioRuntimeService
from qmio.circuits import bell as circuit

service = QmioRuntimeService()

# Number of shots
shots = 1000
# Repetition period: if None picks internal default
repetition_period = 500*10**-6
# Optimization level for the circuit transpiler
optimization = 0
# Result format
res_format = "binary_count"

with service.backend(name="qpu") as backend:
    result = backend.run(circuit=circuit, shots=shots, repetition_period=repetition_period, optimization=optimization, res_format=res_format)

print(result["results"]["c"])
