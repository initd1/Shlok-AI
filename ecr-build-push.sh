# To be run on EC2 Build server

#!/bin/sh
set -xe

sudo docker-compose -f docker-compose-shlok-ai-build.yml build \
    || echo "[!] Failed to build docker images"

# ECR Login
aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin 603077400146.dkr.ecr.ap-south-1.amazonaws.com

sudo docker tag shlok-ai-shlok-ui:latest 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-ui:latest
sudo docker tag shlok-ai-shlok-api:latest 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-api:latest


sudo docker push 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-ui:latest \
    || echo "[!] Failed to push shlok-ui image"
sudo docker push 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-api:latest \
    || echo "[!] Failed to push shlok-api image"