# To be run on EC2 Run server 

#!/bin/sh
set -xe

aws ecr get-login-password --region ap-south-1 \
    | sudo docker login --username AWS --password-stdin 603077400146.dkr.ecr.ap-south-1.amazonaws.com \
    || echo "[!] Failed to login"

sudo docker-compose -f docker-compose-shlok-ai-run.yml pull \
    || echo "[!] Failed to pull latest images"
sudo docker-compose -f docker-compose-shlok-ai-run.yml up -d \
    || echo "[!] Failed to bring up containers"