from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    try:
        data = request.get_json()
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        cf = fetch_conversion_factor(source_currency, target_currency)

        if cf is None:
            response = {'fulfillmentText': f"Unable to fetch conversion factor for {source_currency} to {target_currency}"}
        else:
            final_amount = amount * cf
            final_amount = round(final_amount, 2)
            response = {
                'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
            }

    except Exception as e:
        response = {'fulfillmentText': f"Error: {str(e)}"}

    return jsonify(response)

def fetch_conversion_factor(source, target):
    try:
        url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=9aa0c54f5ad4c460c36d".format(source, target)
        response = requests.get(url)
        response = response.json()

        return response['{}_{}'.format(source, target)]

    except Exception as e:
        print(f"Error fetching conversion factor: {str(e)}")
        return None

if __name__ == "__main__":
    app.run(debug=True)