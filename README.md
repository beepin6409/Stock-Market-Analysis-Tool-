# Stock Market Analysis Tool

![image](https://github.com/beepin6409/Stock-Market-Analysis-Tool-/assets/78684754/7f65b37e-5319-40fe-b244-14de6b394692)


<p align="center">
  <em>Analyze stock market data and make informed investment decisions with ease.</em>
</p>

## 🚀 Features

- **Stock Data Analysis:** Input a stock symbol, start date, end date, and moving average window to analyze historical stock data.

- **Moving Average:** Calculate moving averages for the selected stock to visualize trends and trading signals.

- **Optimal Buy and Sell Dates:** Use a dynamic programming approach to find the best buying and selling dates with a minimum one-year holding period, considering factors like Compound Annual Growth Rate (CAGR).

- **Top 50 Stock Symbols:** Access a list of the top 50 stock symbols and their corresponding company names for convenience.

- **Disclaimer:** Receive a reminder that the tool is for educational purposes only and doesn't provide financial advice. Encourages users to conduct their research and consult financial professionals.

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/stock-market-analysis-tool.git


2. Install the required dependencies:

```bash
pip install yfinance pandas streamlit matplotlib
```

3. Run the application:

```bash
streamlit run stock_analysis_tool.py
```

## 📈 Usage

1. Launch the tool by running the Streamlit application.

2. Input the stock symbol (e.g., AAPL), start date, end date, and a moving average window (0 for no moving average).

3. Click the "Analyze" button to initiate the analysis.

4. The tool will display the results, including the optimal buying and selling dates with their respective prices, and the calculated CAGR.

5. You can also view the stock price chart with the selected moving average.
