### **Statistics and Its Types**

**Statistics** is the science of collecting, analyzing, interpreting, presenting, and organizing data. In machine learning, it's the bedrock for understanding data and evaluating model performance.

There are two main types of statistics:

* **Descriptive Statistics**: This involves summarizing and organizing data so it can be easily understood. It describes the basic features of the data in a study. Think of it as creating a "profile" of your dataset.
    * **Example**: Calculating the average height of students in a class.
* **Inferential Statistics**: This involves making inferences and predictions about a larger population based on a sample of data taken from it. It's used to test hypotheses and make predictions.
    * **Example**: Using the average height of students in a few classes to estimate the average height of all students in a university.

***

### **Population vs. Sample Data (N & n)**

* **Population (N)**: This refers to the **entire group** you want to study or draw conclusions about. The size of the population is denoted by **$N$**. In machine learning, the population is often the complete set of all possible data points.
    * **Example**: All the houses in a country.

* **Sample (n)**: This is a **subset** of the population that you actually collect data from. It's used to make inferences about the whole population. The size of the sample is denoted by **$n$**. In machine learning, your training dataset is a sample of the real world.
    * **Example**: A selection of 1,000 houses from different cities across the country.

The goal is to have a sample that is representative of the entire population.

***

### **Measures of Central Tendency**

These are single values that attempt to describe a central position within a set of data.

* **Mean**: The **average** of all data points. It's calculated by summing all values and dividing by the count of values. It's sensitive to outliers.
    * **Formula**: $\mu$ (population mean) or $\bar{x}$ (sample mean) = $\frac{\sum x_i}{n}$
* **Median**: The **middle** value in a sorted dataset. It's less affected by outliers, making it a more robust measure for skewed data.
* **Mode**: The **most frequent** value in a dataset. It's useful for categorical data.

***

### **Measure of Dispersion**

These measures describe the **spread or variability** of the data. They tell you how "spread out" your data points are.

* **Range**: The difference between the highest and lowest values. It's simple but highly sensitive to outliers.
* **Variance ($\sigma^2$ or $s^2$)**: The average of the squared differences from the Mean. A larger variance means the data is more spread out.
* **Standard Deviation ($\sigma$ or $s$)**: The square root of the variance. It's the most common measure of spread.

***

### **Standard Deviation**

**Standard Deviation** ($SD$) is a measure of how dispersed the data is in relation to the mean.

* **Low Standard Deviation**: The data points tend to be close to the mean. This is often desirable in machine learning predictions, as it indicates consistency.
* **High Standard Deviation**: The data points are spread out over a wider range of values. This can indicate high variability in the data.

In machine learning, you might use standard deviation to identify outliers or to standardize features (e.g., in a process called feature scaling).

***

### **Variables & Random Variables**

* **Variable**: A property or characteristic of a data point that can be measured or counted. In a dataset, variables are typically the columns.
    * **Example**: In a dataset of houses, the variables could be 'price', 'number of bedrooms', and 'square footage'.

* **Random Variable**: A variable whose value is a numerical outcome of a random phenomenon. It's a variable described by a probability distribution. In machine learning, we often treat our input features and target outputs as random variables.
    * **Example**: The outcome of a dice roll (can be 1, 2, 3, 4, 5, or 6) is a random variable. The price of a *randomly selected* house is also a random variable.

***

### **Histograms**

A **histogram** is a graphical representation of the distribution of numerical data. It's a bar plot where the x-axis represents the bins (intervals of the data), and the y-axis represents the frequency (the number of data points in each bin).

Histograms are excellent for quickly understanding:
* The shape of the data's distribution (e.g., Normal, Skewed).
* The central tendency and dispersion.
* The presence of outliers.

***

### **Percentile and Quartiles**

* **Percentile**: A measure indicating the value below which a given percentage of observations in a group of observations falls.
    * **Example**: If you score in the 90th percentile on a test, it means you scored better than 90% of the people who took the test.

* **Quartiles**: These are specific percentiles that divide the data into four equal parts.
    * **First Quartile (Q1)**: The 25th percentile. 25% of the data falls below this value.
    * **Second Quartile (Q2)**: The 50th percentile, which is also the **median**. 50% of the data falls below this value.
    * **Third Quartile (Q3)**: The 75th percentile. 75% of the data falls below this value.

The range between Q1 and Q3 is called the **Interquartile Range (IQR)**, which is a robust measure of spread.

***

### **5 Number Summary**

This is a descriptive statistics summary that provides a concise overview of a dataset's distribution. It consists of five values:

1.  **Minimum**: The smallest value in the dataset.
2.  **First Quartile (Q1)**: The 25th percentile.
3.  **Median (Q2)**: The middle value.
4.  **Third Quartile (Q3)**: The 75th percentile.
5.  **Maximum**: The largest value in the dataset.

This summary is used to create a **Box Plot** (or box-and-whisker plot), which is another powerful tool for visualizing data distribution and identifying outliers.

***

### **Correlation & Covariance**

These measures describe the relationship and dependency between two variables.

* **Covariance**: Measures the joint variability of two random variables.
    * **Positive Covariance**: Indicates that the two variables tend to move in the same direction (if one increases, the other tends to increase).
    * **Negative Covariance**: Indicates that the variables tend to move in opposite directions.
    * **Limitation**: The magnitude of covariance is not standardized, making it hard to compare across different pairs of variables.

* **Correlation**: A standardized version of covariance that measures the **strength and direction** of a *linear* relationship between two variables. The value ranges from -1 to +1.
    * **+1**: Perfect positive linear relationship.
    * **-1**: Perfect negative linear relationship.
    * **0**: No linear relationship.
    * **In Machine Learning**: Correlation is crucial for feature selection. Highly correlated features can be redundant, and understanding the correlation between features and the target variable is key to building effective models.