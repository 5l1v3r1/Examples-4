from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit import BasicAer
#Creating quantum circuits
q = QuantumRegister(4)
c = ClassicalRegister(4)
temp = QuantumRegister(1)
qc = QuantumCircuit(q,temp,c)
qc.h(q)
qc.cx(q[0],temp)
qc.cx(q[2],temp)
qc.cx(q[3],temp)
qc.h(q)
meas = QuantumCircuit(q,temp,c)   #Making measurements
meas.measure(q,c)
t = qc + meas
#Running the quantum circuits on a QASM simulator
backend = BasicAer.get_backend('qasm_simulator')
job = execute(t ,backend, shots=1000)
result = job.result().get_counts(t)
print(result)
