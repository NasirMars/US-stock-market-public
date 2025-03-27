# This code compares the current stock price with the historical high, helping you understand its price potential now.
!pip install yfinance matplotlib #While running in Google Colab
import yfinance as yf
import matplotlib.pyplot as plt

my_portfolio_company_list = ['PYPL', 'BK', 'WMT', 'GE', 'TSLA', 'BSX', 'KO']

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
financial_company ={
    'credit_services_company_list' : ['V', 'MA', 'AXP', 'PYPL', 'COF', 'DFS', 'SYF'],
    'banks_company_list' : ['JPM', 'BAC', 'WFC', 'C', 'BK'],
    'insurance_diversified_company_list' : ['BRK-B', 'AIG', 'ACGL'],
    'asset_management_company_list' : ['BX', 'BLK', 'KKR', 'AMP', 'RJF', 'STT', 'TROW', 'NTRS', 'PFG', 'BEN', 'IVZ'],
    'financial_data_company_list' : ['SPGI', 'ICE', 'MCO', 'CME', 'MSCI', 'NDAQ', 'CBOE', 'FDS'],
    'capital_market_company_list' : ['GS', 'MS', 'SCHW', 'MKTX'],
    'insurance_propert_company_list' : ['PGR', 'CB', 'TRV', 'ALL', 'HIG', 'CINF', 'WRB', 'L', 'AIZ'],
    'banks_regional_company_list' : ['USB', 'PNC', 'TFC', 'MTB', 'FITB', 'HBAN', 'RF', 'CFG', 'KEY'],
    'financial_insurance_brokers_company_list' : ['MMC', 'AON', 'AJG', 'BRO', 'WTW', 'ERIE'],
    'insurance_life_company_list' : ['AFL', 'MET', 'PRU', 'GL'],
    'insurance_reinsurance_company_list' : ['EG']
}

company_type = ''
tech_company_list = []
for company_list in tech_company.values():
    tech_company_list.extend(company_list)

communication_services_list = []
for company_list in communication_services.values():
    communication_services_list.extend(company_list)

financial_company_list = []
for company_list in financial_company.values():
    financial_company_list.extend(company_list)

# company_type = 'semiconductors_company_list'
# company_type = 'internet_content_and_information_company_list'
# company_list = tech_company[company_type]
# company_list = my_portfolio_company_list
# company_list = communication_services[company_type]

# company_list = tech_company_list
# company_list = communication_services_list
company_list = financial_company_list

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period="1d")
    current_price = stock_info['Close'].iloc[-1]
    stock_history = stock.history(period="max")
    highest_price = stock_history['High'].max()
    lowest_price = stock_history['Low'].min()
    return current_price, highest_price, lowest_price

def percentage(current_price, history_lowest_price, history_highest_price):
    potencial = (current_price - history_lowest_price) / (history_highest_price - history_lowest_price)
    potencial_rate = f'{potencial*100:.2f}%'
    return potencial_rate

if __name__ == "__main__":
  # print(tech_company_list)

  if len(company_type) > 0:
    print("Company type:"+ company_type) # print array name
    exit()
  for stock_symbol in company_list:
    current_price, highest_price, lowest_price = get_stock_data(stock_symbol)
    potencial_rate = percentage(current_price, lowest_price, highest_price)
    print(f"Stock: {stock_symbol}")
    print(f"Current Price: {current_price:.2f}")
    # print(f"Highest Price: {highest_price:.2f}")
    # print(f"Lowest Price: {lowest_price:.2f}")
    print(f"Potencial Rate: {potencial_rate}")
