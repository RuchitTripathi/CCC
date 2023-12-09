# Currency Converter Chatbot using Flask

This is a simple Flask application that serves as a webhook for a currency converter chatbot. The chatbot processes user queries about currency conversion and responds with the converted amount.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

2. Make a POST request to the endpoint `http://127.0.0.1:5000/` with a JSON payload containing the user's query. For example:

   ```json
   {
       "queryResult": {
           "parameters": {
               "unit-currency": {
                   "currency": "USD",
                   "amount": 100
               },
               "currency-name": "EUR"
           }
       }
   }
   ```

   This will return a JSON response with the converted amount.

## Deployment

This application is designed to be deployed on platforms like Heroku. A `Procfile` and `setup.sh` file are included to assist with the deployment process.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```