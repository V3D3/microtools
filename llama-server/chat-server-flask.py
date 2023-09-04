from flask import Flask
from flask import request

app = Flask (__name__)

# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional

from llama import Llama

import json

ckpt_dir = 'llama-2-7b-chat/'
tokenizer_path = 'tokenizer.model'
max_seq_len = 8192
max_batch_size = 4
temperature = 0.4 # tune creativity (high)
top_p = 0.3 # tune repetitiveness, and creativity (high)
max_gen_len : Optional[int] = None

GEN = None

@app.route ('/health')
def health ():
    if GEN is None:
        return "NOT OK"
    else:
        return "OK"

@app.route ('/generate')
def generate_model ():
    global GEN
    global ckpt_dir
    global tokenizer_path
    global max_seq_len
    global max_batch_size

    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    GEN = generator
    return "OK"

DIALOG_PRE = [
    {"role": "system", "content": "You are a serious AI assistant. Prioritize brevity and correctness."}
]

# @app.route ('/settemp')

@app.route ('/setsys', methods=['POST'])
def setsys ():
    global DIALOG_PRE
    sysmsg = request.data
    DIALOG_PRE[0]['content'] = str(sysmsg)
    return "OK"

@app.route ('/chat', methods=['POST'])
def chat ():
    global GEN
    global max_gen_len
    global temperature
    global top_p
    global DIALOG_PRE

    if (GEN is None):
        return "Error: generator is not initialized. Check /health"

    message = request.data
    dialogs = [[*DIALOG_PRE, {"role": "user", "content": str (message)}]]
    results = GEN.chat_completion (dialogs, max_gen_len=max_gen_len, temperature=temperature, top_p=top_p)[0]['generation']['content']
    return results


if __name__ == '__main__':
    app.run (host="127.0.0.1", port=6800)