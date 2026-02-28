#!/bin/bash

# ===== MIDAS environment configuration =====

export MIDASSYS="$HOME/midas"
export MIDAS_DIR="$HOME/online"
export MIDAS_EXPTAB="$HOME/exptab"
export MIDAS_EXPT_NAME="radon"

export PATH="$MIDASSYS/bin:$PATH"
export LD_LIBRARY_PATH="$MIDASSYS/lib:$LD_LIBRARY_PATH"
export PYTHONPATH="$MIDASSYS/python:$PYTHONPATH"

# ===== Create required directories if missing =====

mkdir -p "$MIDAS_DIR/radon"

echo "----------------------------------------"
echo "MIDAS environment configured:"
echo "MIDASSYS=$MIDASSYS"
echo "MIDAS_DIR=$MIDAS_DIR"
echo "Experiment name=$MIDAS_EXPT_NAME"
echo "----------------------------------------"
