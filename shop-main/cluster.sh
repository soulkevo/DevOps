#!/bin/sh
# cluster.sh — оновлена версія
minikube start -p shop-main --nodes 3 --driver=docker --cpus 2 --memory 2048
minikube addons enable csi-hostpath-driver -p shop-main
minikube addons enable volumesnapshots -p shop-main
minikube addons enable ingress -p shop-main
