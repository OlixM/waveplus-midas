#!/bin/bash
# Auto-start MIDAS dla eksperymentu radon

source ~/waveplus-midas/setup_env.sh

# Start MIDAS server
echo "Starting mserver..."
mserver -e radon &
sleep 2

# Start logger
echo "Starting mlogger..."
mlogger -e radon &
sleep 2

# Start web server
echo "Starting mhttpd..."
mhttpd -e radon &
sleep 2

# Start frontend
echo "Starting Radon frontend..."
python3 ~/waveplus-midas/midas_radon.py &
