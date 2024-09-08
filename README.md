# Financial-analysis-and-visualisation
 Nifty 50 Futures Financial Analysis and Visualization  Description: The Nifty 50 Futures Financial Analysis and Visualization project involves working with historical financial data to analyze and visualize trends in the Nifty 50 futures market. 
 The project primarily focuses on using Python to preprocess and clean the data, conduct statistical analysis, and generate insightful visualizations that reflect trends in price, volume, and daily percentage changes over time.

The project is suitable for individuals interested in financial markets, data analysis, and visualization, especially those looking to enhance their Python skills for real-world financial analysis.

Objectives:
Data Cleaning and Preprocessing: The historical data is first cleaned and formatted correctly, handling missing values and ensuring numerical columns are in the right format.

Statistical Analysis: Basic descriptive statistics of the dataset are computed to get an overview of the market trends over time.
Data Visualization: Line charts and histograms are created to visualize the trends in price, volume, and daily percentage changes in the Nifty 50 futures market.

Interpretation: The visualizations enable better understanding and interpretation of market behavior during different periods, helping to identify patterns like volatility, volume surges, and price movements.
Tools & Technologies:

Python: Used for data preprocessing, analysis, and visualization.

Pandas: Essential for reading and manipulating the CSV data.

Matplotlib: Utilized for creating plots and visualizations.

Seaborn: For enhanced visualizations, specifically histograms and distribution plots.

CSV File: Historical financial data of Nifty 50 Futures is stored in CSV format.

Project Requirements:

Python 3.x: Ensure that Python is installed on your system.

Libraries:

Install necessary libraries using the command:

pip install pandas matplotlib seaborn
Dataset: The CSV file containing historical data (Nifty 50 Futures Historical Data.csv) should be stored in the C:\Users\91904\Downloads\financial-analysis-portfolio directory.

Instructions to Run the Project:
Prepare the Data: Ensure the CSV file Nifty 50 Futures Historical Data.csv is in the following directory:

makefile
Copy code
C:\Users\91904\Downloads\financial-analysis-portfolio\Nifty 50 Futures Historical Data.csv
Save the Script: Save the Python script as analysis.py in any directory of your choice.

Execute the Script: Open a terminal or command prompt and navigate to the directory where your analysis.py is saved. Run the script by executing the following command:

bash
Copy code
python analysis.py

View Outputs: The script generates the following plots:

price_trend.png: A line chart showing the trend of Nifty 50 futures prices over time.
volume_trend.png: A line chart showing the trend of trading volume over time.
change_distribution.png: A histogram representing the distribution of daily percentage changes in the futures market.
The plots will be saved in the directory C:\Users\91904\Downloads\financial-analysis-portfolio.
Expected Outputs:
Price Trend: A line chart showing the fluctuations in the Nifty 50 futures price over the given period.
Volume Trend: A line chart that displays how the trading volume of Nifty 50 futures varied over time.
Change % Distribution: A histogram displaying the distribution of daily percentage changes in the Nifty 50 futures, giving insights into the market's volatility and behavior.
Each of these visualizations will be saved as PNG files in the specified directory for further analysis or reporting.
