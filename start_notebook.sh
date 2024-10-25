#!/bin/bash

module load gcc/12.3.0 qiskit/1.2.4-python-3.9.9 qiskit-experiments/0.7.0-python-3.9.9
module load qmio-tools/0.1.3-python-3.9.9

jupyter-lab --no-browser --ip=$(hostname -i) --log-level='WARN' --notebook-dir='.'
