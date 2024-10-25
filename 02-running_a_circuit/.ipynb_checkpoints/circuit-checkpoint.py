from qmio import QmioRuntimeService

with open('circuit.qasm', 'r') as file:
    circuit = file.read()
    
service = QmioRuntimeService()
with service.backend(name="qpu") as backend:
    result = backend.run(circuit=circuit, shots=1000)

# result has the following structure:
#    {
#        'results': {
#            'c': {
#                '00000000000000000000000000000000': 406,
#                '10000000000000000000000000000000': 594
#            }
#        },
#        'execution_metrics': {
#            'optimized_circuit': 'OPENQASM 3.0;\ninclude "qelib1.inc";\nqreg q[32];\ncreg c[32];\nx q[0];\nmeasure q[0]->c[0];',
#            'optimized_instruction_count': 14
#        }
#    }

print("The counts per state are:")
print(result["results"]["c"])
