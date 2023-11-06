import yfinance as yf
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def find_optimal_buy_sell_dates(stock_data):
    n = len(stock_data)
    best_buy_date = None
    best_sell_date = None
    max_cagr = 0.0
    buy_date = stock_data.index[0]
    buy_price = stock_data['Adj Close'].iloc[0]

    for i in range(1, n):
        sell_date = stock_data.index[i]
        sell_price = stock_data['Adj Close'].iloc[i]
        
        years = (sell_date - buy_date).days / 365.0

        if years >= 1:
            # Calculate CAGR (annual growth rate)
            cagr = (sell_price / buy_price) ** (1 / years) - 1

            if cagr > max_cagr:
                max_cagr = cagr
                best_buy_date = buy_date
                best_sell_date = sell_date
                best_buy_price = buy_price
                best_sell_price = sell_price

        if sell_price < buy_price:
            buy_date = sell_date
            buy_price = sell_price

    return best_buy_date, best_sell_date, best_buy_price, best_sell_price, max_cagr

def main():
    st.title("Stock Market Analysis Tool ")

    
    # Get user input
    symbol = st.text_input("Enter the stock symbol (e.g., AAPL):")
    start_date = st.text_input("Enter the start date (YYYY-MM-DD):")
    end_date = st.text_input("Enter the end date (YYYY-MM-DD):")
    moving_average = st.text_input("Enter the number of days for moving average (0 for none):")
    
    if st.button("Analyze"):
        try:
            # Convert moving_average to an integer
            moving_average = int(moving_average)

            # Fetch stock data
            stock_data = yf.download(symbol, start=start_date, end=end_date)

            # Calculate moving average
            if moving_average > 0:
                stock_data['Moving_Average'] = stock_data['Adj Close'].rolling(window=moving_average).mean()

            # Calculate average price
            average_price = stock_data['Adj Close'].mean()

            # Calculate lowest price
            lowest_price = stock_data['Adj Close'].min()

            # Calculate highest price
            highest_price = stock_data['Adj Close'].max()

            # Calculate percentage change
            initial_price = stock_data.iloc[0]['Adj Close']
            final_price = stock_data.iloc[-1]['Adj Close']
            percentage_change = ((final_price - initial_price) / initial_price) * 100

            # Calculate hypothetical investment value
            initial_investment = 100  # $100 initial investment
            investment_value = (initial_investment / initial_price) * final_price

            # Display the analysis results
            st.write(f"Average Price: ${average_price:.2f}")
            st.write(f"Lowest Price: ${lowest_price:.2f}")
            st.write(f"Highest Price: ${highest_price:.2f}")
            st.write(f"Percentage Change: {percentage_change:.2f}%")
            st.write(f"Hypothetical Investment Value: ${investment_value:.2f} if you have invested 100 dollar on {start_date}")

            

            # Plot stock's closing prices and moving average
            st.write("Stock Price Chart:")
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(stock_data.index, stock_data['Adj Close'], label=f'{symbol} Adjusted Close Price')
            if moving_average > 0:
                ax.plot(stock_data.index, stock_data['Moving_Average'], label=f'{moving_average}-Day Moving Average')
            ax.set_title(f'{symbol} Stock Price')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.legend()
            ax.grid()
            st.pyplot(fig)

            best_buy_date, best_sell_date, best_buy_price, best_sell_price, max_cagr = find_optimal_buy_sell_dates(stock_data)

            if max_cagr > 0:
                st.write(f"Optimal Buying Date: {best_buy_date}")
                st.write(f"Price at Buying Date: ${best_buy_price:.2f}")
                st.write(f"Optimal Selling Date: {best_sell_date}")
                st.write(f"Price at Selling Date: ${best_sell_price:.2f}")
                st.write(f"CAGR: {max_cagr * 100:.2f}%")
            else:
                st.write("No optimal buying and selling dates found with a 1-year difference.")

        except ValueError:
            st.error("Please enter valid input for the moving average.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        

       

    common_stock_symbols = {
            'AAPL': 'Apple Inc.',
            'MSFT': 'Microsoft Corporation',
            'AMZN': 'Amazon.com Inc.',
            'GOOGL': 'Alphabet Inc. (Class A)',
            'FB': 'Meta Platforms, Inc. (formerly Facebook)',
            'TSLA': 'Tesla, Inc.',
            'JPM': 'JPMorgan Chase & Co.',
            'JNJ': 'Johnson & Johnson',
            'V': 'Visa Inc.',
            'PG': 'Procter & Gamble Company',
            'NVDA': 'NVIDIA Corporation',
            'MA': 'Mastercard Incorporated',
            'HD': 'The Home Depot, Inc.',
            'UNH': 'UnitedHealth Group Incorporated',
            'PYPL': 'PayPal Holdings, Inc.',
            'BAC': 'Bank of America Corporation',
            'VZ': 'Verizon Communications Inc.',
            'T': 'AT&T Inc.',
            'WMT': 'Walmart Inc.',
            'INTC': 'Intel Corporation',
            'DIS': 'The Walt Disney Company',
            'CRM': 'Salesforce.com, Inc.',
            'CMCSA': 'Comcast Corporation',
            'XOM': 'Exxon Mobil Corporation',
            'CVX': 'Chevron Corporation',
            'KO': 'The Coca-Cola Company',
            'ORCL': 'Oracle Corporation',
            'CSCO': 'Cisco Systems, Inc.',
            'PFE': 'Pfizer Inc.',
            'MRK': 'Merck & Co., Inc.',
            'NFLX': 'Netflix, Inc.',
            'IBM': 'International Business Machines Corporation',
            'ABBV': 'AbbVie Inc.',
            'QCOM': 'Qualcomm Incorporated',
            'GILD': 'Gilead Sciences, Inc.',
            'CAT': 'Caterpillar Inc.',
            'NKE': 'NIKE, Inc.',
            'BA': 'The Boeing Company',
            'MCD': "McDonald's Corporation",
            'HON': 'Honeywell International Inc.',
            'SBUX': 'Starbucks Corporation',
            'COP': 'ConocoPhillips',
            'COST': 'Costco Wholesale Corporation',
            'PM': 'Philip Morris International Inc.',
            'LLY': 'Eli Lilly and Company',
            'TMO': 'Thermo Fisher Scientific Inc.',
            'ADP': 'Automatic Data Processing, Inc.',
            'SPG': 'Simon Property Group, Inc.',
            'LMT': 'Lockheed Martin Corporation',
            'GM': 'General Motors Company'
        }
    st.subheader("Here are the symbols of top 50 stocks of the Stock Market ")
    for symbol,company in common_stock_symbols.items():
        st.write(symbol + ' : ' + company,end=' ')


    st.markdown(
        """
        <style>
        .marquee {
            white-space: nowrap;
            animation: marquee 10s linear infinite;
        }

        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        </style>
        <div class="marquee">
            <p>
            Disclaimer: The information provided by this tool is for educational purposes only. It is not financial advice, and you should not make investment decisions based solely on this tool. 
            Always do your own research and consult with a qualified financial professional before making investment decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )





if __name__ == '__main__':
    main()
