#!/bin/sh

source /home/ec2-user/.bashrc

cd /home/ec2-user/be_line_cocial_crm

echo 'docker compose up'
docker-compose up -d --build

echo 'clean docker build cache.'
docker builder prune -f