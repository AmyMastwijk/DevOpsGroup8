#!/bin/bash
# Update packages
sudo yum update -y

# Install Docker
sudo amazon-linux-extras install docker -y

# Start Docker service
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Add ec2-user to the docker group
sudo usermod -a -G docker ec2-user

# Run the Docker container
docker run -d -p 80:8080 --name supply-image --restart unless-stopped amymastwijk/supply-image
