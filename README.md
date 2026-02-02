\# Smart Payment Routing Optimizer



\## 📌 Project Overview

As a Product Analyst, maximizing payment success rates is critical for revenue growth. This project demonstrates a data-driven approach to \*\*Payment Routing\*\*. It analyzes historical transaction data to identify the optimal Payment Gateway (HDFC, ICICI, or Razorpay) for specific Card Networks (Visa, Mastercard, Amex).



\## 🚀 Key Features

\* \*\*Data Generation:\*\* A Python script (`generate\_data.py`) that simulates 5,000 transactions with injected performance biases (e.g., HDFC performing better for Visa).

\* \*\*Routing Logic:\*\* An analytical engine (`optimizer.py`) that calculates success rates per segment.

\* \*\*Automated Recommendations:\*\* Generates a routing table to guide engineering on which gateway to prioritize to minimize "churn" at checkout.



\## 🛠️ Tech Stack

\* \*\*Language:\*\* Python 3.x

\* \*\*Library:\*\* Pandas (Data Manipulation)

\* \*\*Environment:\*\* Virtual Environments (venv)



\## 📊 How to Run

1\. \*\*Generate Data:\*\*

&nbsp;  `python generate\_data.py`

2\. \*\*Run Optimizer:\*\*

&nbsp;  `python optimizer.py`



\## 📈 Sample Insight

Based on the generated data, the optimizer identifies:

\* \*\*Visa transactions\*\* should be routed to \*\*HDFC\*\* (90% success).

\* \*\*Mastercard transactions\*\* should be routed to \*\*ICICI\*\* (85% success).

