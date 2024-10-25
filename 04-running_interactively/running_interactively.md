# Running interactively
With the new version of `qmio-run` it is not only possible to submit non-interactive batch jobs to SLURM, but it is also very easy to run code interactively using a Jupyter notebook.

## Step 1: Create an interactive session
First create a interactive session with the resources that you need:
```
compute --cores 4 --mem-per-cpu 2G
```

## Step 2: Launch an interactive notebook
Then, in this interactive session, you can use the provided script to start an interactive Jupyter notebook:
```
./start_notebook.sh
```
