#!/bin/bash
PROJ_DIR=./
docker build ./ -t dudo_env
docker run -d --name dudo_run -v $PROJ_DIR/micro_dudo.py:/home/dev/project/micro_dudo.py dudo_env python3 micro_dudo.py