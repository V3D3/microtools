#!/usr/bin/env bash
PYTORCH_ENABLE_MPS_FALLBACK=1 torchrun --nproc_per_node 1 chat-server-flask.py &
streamlit run chat-frontend-streamlit.py