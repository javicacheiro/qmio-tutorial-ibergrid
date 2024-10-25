#!/bin/bash
#SBATCH -J single-circuit   # Job name
#SBATCH -o %x.o%j           # Name of stdout output file (%x -> jobname, %j -> jobId)
#SBATCH -e %x.e%j           # Name of stderr output file
#SBATCH --partition qpu     # Partition where to run the job (use 'qpu' for the real QPU)
#SBATCH --nodes 1           # Number of nodes
#SBATCH --ntasks 1          # Total number of MPI tasks (if omitted, n=<node_total_cores>)
#SBATCH --cpus-per-task 1   # Cores per task
#SBATCH --mem-per-cpu 4G    # Memory per core
#SBATCH --time 00:05:00     # Max run time (hh:mm:ss)

module load qmio-run

python circuit.py
