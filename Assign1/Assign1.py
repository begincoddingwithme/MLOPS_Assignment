import time
import pandas as pd
import matplotlib.pyplot as plt

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(f"Execution time for {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

class SalesDataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    @timing_decorator
    def summarize_data(self):
        summary = self.data.describe()
        print(summary)
        return summary

    @timing_decorator
    def plot_sales_over_time(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        sales_over_time = self.data.groupby('Date')['Total'].sum()
        plt.figure(figsize=(10, 6))
        sales_over_time.plot()
        plt.title('Total Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    file_path = 'supermarket_sales.csv'  
    processor = SalesDataProcessor(file_path)
    processor.summarize_data()
    processor.plot_sales_over_time()
