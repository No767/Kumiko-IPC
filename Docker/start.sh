#!/usr/bin/env bash

if [[ -v IPC_SECRET_KEY ]]; then
    echo "IPC_SECRET_KEY=${IPC_SECRET_KEY}" >> /Kumiko_IPC/dramatiq_ipc/.env
else
    echo "Missing IPC_SECRET_KEY environment variable!"
    exit 1;
fi

if [[ -v RABBITMQ_USER ]]; then
    echo "RABBITMQ_USER=${RABBITMQ_USER}" >> /Kumiko_IPC/dramatiq_ipc/.env
else
    echo "Missing RABBITMQ_USER environment variable!"
    exit 1;
fi

if [[ -v RABBITMQ_PASSWORD ]]; then
    echo "RABBITMQ_PASSWORD=${RABBITMQ_PASSWORD}" >> /Kumiko_IPC/dramatiq_ipc/.env
else
    echo "Missing RABBITMQ_PASSWORD environment variable!"
    exit 1;
fi

if [[ -v RABBITMQ_HOST ]]; then
    echo "RABBITMQ_HOST=${RABBITMQ_HOST}" >> /Kumiko_IPC/dramatiq_ipc/.env
else
    echo "Missing RABBITMQ_HOST environment variable!"
    exit 1;
fi

if [[ -v RABBITMQ_PORT ]]; then
    echo "RABBITMQ_PORT=${RABBITMQ_PORT}" >> /Kumiko_IPC/dramatiq_ipc/.env
else
    echo "Missing RABBITMQ_PORT environment variable!"
    exit 1;
fi


delay=1
while true; do
  dramatiq-gevent Kumiko-IPC.dramatiq_ipc.worker -p 2
  if [ $? -eq 3 ]; then
    echo "Connection error encountered on startup. Retrying in $delay second(s)..."
    sleep $delay
    delay=$((delay * 2))
  else
    exit $?
  fi
done

dramatiq-gevent Kumiko-IPC.dramatiq_ipc.worker -p 2