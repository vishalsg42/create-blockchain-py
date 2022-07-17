#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 19:36:55 2022

@author: Vishal Gupta
"""

from crypt import methods
from email import message
from urllib import response
from flask import Flask, jsonify


from blockchain import Blockchain
# Part 2 - Mining our blockchain
app = Flask(__name__)

blockchain = Blockchain()


@app.route("/", methods=["GET"])
def uptime():
    status = {
        "message": "server is running fine",
        "success": True,
        "event": "APPLICATION_HEALTH"
    }
    return status


@app.route("/mine_block", methods=["GET"])
def mine_Block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    res = {
        "message": "blockchain is successfully mined",
        "success": True,
        "event": "MINE_BLOCK",
        "data": block
    }
    return jsonify(res)


@app.route("/get_chain", methods=["GET"])
def get_chain():
    response = {
        "message": "fetched all chain",
        "success": True,
        "event": "FETCH_ALL_CHAIN",
        "data": {
            "chain": blockchain.chain,
            "length": len(blockchain.chain)
        }
    }
    return response


@app.route("/is_valid", methods=["GET"])
def is_valid():
    is_chain_valid = blockchain.is_chain_valid(blockchain.chain)
    response = {
        "message": "Successfully verified the chain",
        "success": True,
        "event": "VERIFY_CHAIN",
        "data": {
            "is_chain_valid": is_chain_valid,
        }
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
