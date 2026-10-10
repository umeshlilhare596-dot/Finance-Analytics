# Project Research Note: Finance Analytics Dashboard

## Abstract
This project demonstrates how transaction records can be summarized into practical financial indicators. A Streamlit web application allows a user to filter transactions by date and category, compare income and expenses over time, and inspect expense distribution.

## Objectives
1. Calculate total income and total expenses.
2. Calculate net savings as income minus expenses.
3. Compare monthly income and expenses.
4. Visualize expense distribution by category.
5. Allow filtered transaction data to be downloaded.

## Methodology
The application reads a CSV file with Date, Description, Type, Category, and Amount columns. Pandas performs filtering and aggregation. Plotly generates interactive charts, and Streamlit presents the dashboard in a browser.

## Limitations
The bundled data is synthetic sample data. Results are only as accurate as the supplied transaction records. The dashboard does not connect to banks and does not provide investment advice.

## Conclusion
The project shows how basic data analytics and visualization can help users understand spending patterns and savings. Future improvements could include budget targets, recurring-payment detection, and secure import of user-owned transaction files.
