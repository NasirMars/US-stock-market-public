import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tech_company = {
'software_company_list' : ['MSFT', 'ORCL', 'ADBE', 'PANW', 'PLTR', 'SNPS', 'CRWD', 'FTNT', 'GPN', 'GDDY', 'CPAY', 'VRSN', 'GEN', 'AKAM', 'FFIV'],
'consumer_electronics_company_list' : ['AAPL'],
'semiconductors_company_list' : ['NVDA', 'AVGO', 'AMD', 'QCOM', 'TXN', 'MU', 'ADI', 'INTC', 'NXPI', 'MPWR', 'MCHP', 'ON', 'SWKS', 'QRVO'],
'software_application_company_list' : ['CRM', 'NOW', 'INTU', 'UBER', 'ADP', 'CDNS', 'ROP', 'ADSK', 'PAYX', 'FICO', 'ANSS', 'TYL', 'PTC', 'PAYC', 'DAY'],
'information_technology_services_company_list' : ['ACN', 'IBM', 'FI', 'FIS', 'IT', 'CTSH', 'CDW', 'BR', 'LDOS', 'JKHY', 'EPAM'],
'semiconductor_equipment_and_materials_company_list' : ['AMAT', 'KLAC', 'LRCX', 'TER'],
'computer_hardware_company_list' : ['ANET', 'DELL', 'HPQ', 'SMCI', 'NTAP', 'WDC', 'STX'],
'communication_equipment_company_list' : ['CSCO', 'MSI', 'HPE', 'ZBRA', 'JNPR'],
'electronic_computer_company_list' : ['APH', 'TEL', 'GLW', 'JBL'],
'scientific_and_technical_instruments_company_list' : ['GRMN', 'KEYS', 'FTV', 'TDY', 'TRMB'],
'solar_company_list' : ['FSLR', 'ENPH']
}
communication_services = {
    'internet_content_and_information_company_list' : ['GOOG', 'META'],
    'telecom_services_company_list' : ['TMUS', 'VZ', 'CMCSA', 'T', 'CHTR'],
    'entertainment_company_list' : ['NFLX','DIS', 'LYV', 'WBD', 'FOXA', 'NWS', 'PARA'],
    'electronic_gaming_and_multimedia_company_list' : ['EA', 'TTWO'],
    'advertising_agencies_company_list' : ['OMC', "IPG"]
    }

company_type = ''
tech_company_list = []
for company_list in tech_company.values():
    tech_company_list.extend(company_list)

communication_services_list = []
for company_list in communication_services.values():
    communication_services_list.extend(company_list)

def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    sp500_df = table[0]
    return sp500_df['Symbol'].tolist(), sp500_df[['Symbol', 'Security', 'GICS Sector']]

tickers, sp500_info = get_sp500_tickers()    # Download stock data for a subset of S&P 500
tickers_subset = tickers[:100]  # Adjust this number to analyze more companies

# company_type = 'semiconductors_company_list'
# company_type = 'internet_content_and_information_company_list'
# company_list = tech_company[company_type]
# company_list = communication_services[company_type]

# company_list = tech_company_list
# company_list = communication_services_list
company_list = tickers_subset

# Download historical stock data
def download_stock_data(tickers, start_date, end_date):
    return yf.download(tickers, start=start_date, end=end_date)

# Analyze stock performance
def analyze_stock_performance(stock_data):
    stock_returns = stock_data['Adj Close'].pct_change()
    cumulative_returns = (1 + stock_returns).cumprod() - 1
    return stock_returns, cumulative_returns

# Visualize data
def plot_stock_data(ticker, stock_data):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data.index, stock_data[('Adj Close', ticker)], label=f'{ticker} Adjusted Close')
        plt.title(f'{ticker} Stock Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Adjusted Close Price')
        plt.legend()
        plt.show()
    except KeyError as e:
        print(f"Data for {ticker} not available. Skipping...")

# Heatmap for correlation
def plot_correlation_heatmap(stock_data):
    # Unstacking the multi-level columns to get individual stock price data for correlation
    adj_close_data = stock_data['Adj Close']
    correlation_matrix = adj_close_data.corr()
    plt.figure(figsize=(50, 50))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Stock Price Correlation Heatmap')
    plt.show()

# Main function
def main():
    stock_data = download_stock_data(company_list, start_date='2022-01-01', end_date='2024-10-01')

    # Analyze performance
    stock_returns, cumulative_returns = analyze_stock_performance(stock_data)

    # Visualize individual stock performance
    for ticker in company_list:
        if ('Adj Close', ticker) in stock_data.columns:  # Check if ticker data is present in the MultiIndex DataFrame
            plot_stock_data(ticker, stock_data)
        else:
            print(f"No data available for {ticker}")

    # Plot correlation heatmap
    plot_correlation_heatmap(stock_data)

if __name__ == "__main__":
    main()
