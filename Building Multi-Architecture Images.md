
sudo nano ~/.docker/config.json
```
{
  ...
  "experimental": "enabled"
}
```

sudo docker buildx create --use

aws ecr get-login-password --region ap-south-1 | sudo docker login --username AWS --password-stdin 603077400146.dkr.ecr.ap-south-1.amazonaws.com

sudo docker buildx build --platform linux/amd64,linux/arm64 -t 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-api:latest --push .


cd shlok-ai
sudo docker buildx build --platform linux/amd64,linux/arm64 -t 603077400146.dkr.ecr.ap-south-1.amazonaws.com/shlok-ui:latest --push .