OPENQASM 3.0;
include "qelib1.inc";
qreg q[32];
creg c[32];
x q[0];
measure q[0]->c[0];