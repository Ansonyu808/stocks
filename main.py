import json
from alpha_vantage.timeseries import TimeSeries

class StockInterface:
    api_key = ""
    ticker = ""
    dataframe = None

    def __init__(self, api_key_json_file: str, ticker: str):
        self.api_key = self.load_api_key(api_key_json_file)
        self.ticker = ticker
        self.dataframe = self.load_ts_data_from_ticker(self.api_key, self.ticker)

    def load_api_key(self, api_key_json_file: str):
        with open(api_key_json_file) as f:
            api_key = json.load(f).get("key")
        return api_key

    def load_ts_data_from_ticker(self, api_key: str, ticker: str):
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=ticker, outputsize="full")
        return data

    def df_to_excel(self, ticker: str, df: dataframe):
        output_name = ticker + ".xlsx"
        df.to_excel(output_name)

amzn = StockInterface("./api-key.json", "amzn")

amzn.df_to_excel(amzn.ticker, amzn.dataframe)
print(amzn.dataframe)