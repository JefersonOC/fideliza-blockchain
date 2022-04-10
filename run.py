from flask import Flask, jsonify, request
from datetime import datetime
import json
import logging

from loyalty import get_balance, gift_redeem, gift_transfer, poits_mint

app = Flask(__name__)

# Setup the logging system
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


@app.route('/health', methods=['GET'])
def health():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(
        datetime=dt_string,
        status="OK"
    ), 200


@app.route('/balance', methods=['GET'])
def balance():
    account = request.args.get('account', default="0x")

    data = get_balance(account=account)

    logging.info(json.dumps(data, indent=4))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(
        datetime=dt_string,
        status="OK",
        data=data
    ), 200


@app.route('/transfer', methods=['POST'])
def transfer():
    request_data = request.get_json()

    data = gift_transfer(account=str(request_data["account"]),
                         account_to=str(request_data["to"]),
                         amount=str(request_data["amount"]))

    logging.info(json.dumps(data, indent=4))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(
        datetime=dt_string,
        status="OK",
        data=data
    ), 200


@app.route('/redeem', methods=['POST'])
def redeem():
    request_data = request.get_json()

    data = gift_redeem(account=str(request_data["account"]),
                       amount=str(request_data["amount"]))

    logging.info(json.dumps(data, indent=4))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(
        datetime=dt_string,
        status="OK",
        data=data
    ), 200

@app.route('/mint', methods=['POST'])
def mint():
    request_data = request.get_json()

    data = poits_mint(account=str(request_data["account"]),
                       amount=str(request_data["amount"]))

    logging.info(json.dumps(data, indent=4))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify(
        datetime=dt_string,
        status="OK",
        data=data
    ), 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
