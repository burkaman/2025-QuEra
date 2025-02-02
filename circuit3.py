from bloqade import move
from iquhack_scoring import MoveScorer
from kirin.passes import aggressive
from utils import pi, make_gif

qubit_tracker = {
    0: 0,
    1: 1,
    2: 2,
    3: 3
}

code = """
@move.vmove()
def circuit3():
    q = move.NewQubitRegister(4)
    state = move.Init(qubits=[q[0],q[1],q[2],q[3]], indices=[0,1,2,3])
"""

def ry(qubit, exponent):
    code += f"    state = move.LocalXY(atom_state=state, x_exponent={exponent}*pi, axis_phase_exponent=-pi/2, indices=[{qubit_tracker[qubit]}])"

def rx(qubit, exponent):
    code += f"    state = move.LocalXY(atom_state=state, x_exponent={exponent}*pi, axis_phase_exponent=0., indices=[{qubit_tracker[qubit]}])"

def rz(qubit, exponent):
    code += f"    state = move.LocalRz(atom_state=state, phi={exponent}*pi,indices=[{qubit_tracker[qubit]}])"

code += "    move.Execute(state)"
exec(code)

expected_qasm = """
// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3)]
qreg q[4];


h q[0];
h q[1];
h q[2];
h q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[1];
sx q[0];
cx q[0],q[1];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[1];
cx q[1],q[0];
sxdg q[1];
s q[1];
cx q[0],q[1];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[1];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[0];
cx q[0],q[3];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[3];
cx q[3],q[0];
sxdg q[3];
s q[3];
cx q[0],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[2];
sx q[0];
cx q[0],q[2];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[2];
cx q[2],q[0];
sxdg q[2];
s q[2];
cx q[0],q[2];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[2];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[1];
u3(pi*0.5,0,pi*0.75) q[2];
sx q[1];
cx q[1],q[2];
rx(pi*0.4223785852) q[1];
ry(pi*0.5) q[2];
cx q[2],q[1];
sxdg q[2];
s q[2];
cx q[1],q[2];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[1];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[2];

rx(pi*0.1766811937) q[0];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[1];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[1];
cx q[1],q[3];
rx(pi*0.4223785852) q[1];
ry(pi*0.5) q[3];
cx q[3],q[1];
sxdg q[3];
s q[3];
cx q[1],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[1];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[2];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[2];
cx q[2],q[3];
rx(pi*0.4223785852) q[2];
ry(pi*0.5) q[3];
cx q[3],q[2];
sxdg q[3];
s q[3];
cx q[2],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[2];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

rx(pi*0.1766811937) q[1];
rx(pi*0.1766811937) q[2];
rx(pi*0.1766811937) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[1];
sx q[0];
cx q[0],q[1];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[1];
cx q[1],q[0];
sxdg q[1];
s q[1];
cx q[0],q[1];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[1];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[0];
cx q[0],q[3];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[3];
cx q[3],q[0];
sxdg q[3];
s q[3];
cx q[0],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[2];
sx q[0];
cx q[0],q[2];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[2];
cx q[2],q[0];
sxdg q[2];
s q[2];
cx q[0],q[2];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[2];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[1];
u3(pi*0.5,pi*1.0,pi*1.25) q[2];
sx q[1];
cx q[1],q[2];
rx(pi*0.3570808194) q[1];
ry(pi*0.5) q[2];
cx q[2],q[1];
sxdg q[2];
s q[2];
cx q[1],q[2];
u3(pi*0.5,pi*0.3929191806,0) q[1];
u3(pi*0.5,pi*1.8929191806,0) q[2];

rx(pi*0.0931081293) q[0];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[1];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[1];
cx q[1],q[3];
rx(pi*0.3570808194) q[1];
ry(pi*0.5) q[3];
cx q[3],q[1];
sxdg q[3];
s q[3];
cx q[1],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[1];
u3(pi*0.5,pi*1.8929191806,0) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[2];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[2];
cx q[2],q[3];
rx(pi*0.3570808194) q[2];
ry(pi*0.5) q[3];
cx q[3],q[2];
sxdg q[3];
s q[3];
cx q[2],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[2];
u3(pi*0.5,pi*1.8929191806,0) q[3];

rx(pi*0.0931081293) q[1];
rx(pi*0.0931081293) q[2];
rx(pi*0.0931081293) q[3];
"""
aggressive.Fold(move.vmove)(circuit3)
scorer = MoveScorer(circuit3, expected_qasm)
print(scorer.score())

make_gif(scorer, "circuit3.gif")