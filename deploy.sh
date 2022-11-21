#!/bin/sh

source /home/ec2-user/.bashrc

cd /home/ec2-user/<xxxxxx>

echo 'docker compose up'
docker-compose up -d --build

echo 'clean docker build cache.'
docker builder prune -f