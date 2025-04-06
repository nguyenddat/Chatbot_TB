#!/bin/bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate llm-env
uvicorn main:app --host 0.0.0.0 --port 5050 --reload