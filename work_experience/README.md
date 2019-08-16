# OXMT Work Experience

## Introduction

|Machine Type|Main Part Replaced|Date for the start of work|
|-|-|-|
|TRUCK 001|Engine|18/06/2015|
|TRUCK 001|Wheel|22/01/2015|
|TRUCK 001|Engine|14/07/2017|
|TRUCK 002|Engine|16/07/2016|
|TRUCK 002|Air Conditioning|16/05/2017|
|TRUCK 003|Engine|01/08/2017|

The table above shows several large trucks that are operated in a haulage industry.  Each line (observation or row) in the data represents a work order – a work order describes work done to change parts in the trucks, along with the date the work began.

## Learning Outcome

For the small data sets in this document it is easy to see the answers by looking at it, but we want you to use code to derive the answers.  In the real world, data may be hundreds of thousands of rows long, and trying to review the raw data entirely visually is not practical.  The outcome here is to use code to summarise data to help you understand the data better, so you can trust the tools and enable yourself to systematically analyse data.  Although MS Excel is often used to analyse data, it does have limitations, especially with the sizes of data it is able to accommodate.  Python does not have these limitations.

We use statistics to summarise and describe data, in this week you will learn about and use basic statistical techniques to learn interesting things in the data.

The set of tools we may use are the Python scripting programming language, using code libraries called pandas, with a charting library called MatPlotLib.  The code editor we will use is called a Jupyter Notebook.  The Jupyter notebook will allow you to present your results as it is possible to include your own notes, the Python code, numeric results and copies of the charts you produce in one place.  By the end of this week, you will have a basic understanding of these tools, enabling you to learn more by yourself.  You will understand some of the work done by a data analyst and programmer.  We will show you how to use Git and GitHub, so you can save and publicise your work.

Your futures:  having skills to analyse data, will be applicable in a very wide range of careers, in both technical jobs like software development, data analysis and engineering, and business type jobs where financial, process and performance data analysis skills will set you apart.

One way of seeing the use of data analysis is the website [Kaggle](http://www.kaggle.com) which hosts competitions with monetary rewards for being the best. For example there is a current competition running with a $25,000 reward to analyse particle data from CERN. There is a massive variety in the problems hosted on this website.  See if you can find the Titanic problem on Kaggle that you might want to try after this week, this has been very popular as a beginners’ project, with lots of help, suggestions and other people’s solutions.

Having a portfolio of code on GitHub where you can show examples of your own work will impress prospective employers.  You can save pure code on GitHub, but don't forget that a readme file is usually expected describing the contents of the repository, which is written with a ‘mark-down’ language - similar to HTML but far less verbose. Jupyter notebook also uses mark-down  for embedded explanatory notes and is an excellent choice if you want to show-case your code to non-technical business orientated people.  It also enables you to demonstrate your presentation skills.

# Task 1 - Environment Setup

**Task: Download, install and set up your environments, including Git and GitHub.**  All of the tools used are open source and free of costs or other charges.

There is plenty of help on the web to assist you in achieving these tasks.  If you do use some of these resources jot down the URLs and include them as references for your project presentation.

- Download and install [Anaconda](https://anaconda.org/anaconda/python)
- Create an account on [GitHub](https://github.com/)
- Download and install [Git](https://git-scm.com/downloads)
- Create your own repository on GitHub and link this to a local repository on your PC. Essentially you create a folder titled 'OXMTWorkExperience' and inside this folder you will store all related files. This folder will then be marked as a repository and only files inside it will be uploaded to GitHub. We can also assist you in doing this. Best practice will be to commit every time you complete a question though it is easy to forget so don't worry.
- Run Jupyter Notebook (run from the Anaconda navigator application), and create your first 'hello world' program, run it to check your Python environment is working.
- You could also write the code using the [Pycharm](https://www.jetbrains.com/pycharm/) IDE if you prefer an IDE based approach though you must make sure to record all your results in parallel so you can present at the end (Jupyter Notebooks will handle this for you)
- Download [Atom](https://atom.io/) which can be used for writing and previewing mark down (for the readme)

# Task 2 - Learn Python

Watch and follow along with videos 1 - 11 (inclusive of 11) of the following [playlist](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7).  

# Task 3 - Basic Data Analysis

All the following questions should be answered via code, even though some are simple to answer by looking at the table manually.

You should read in the CSV file "data/basic_work_orders.csv" in Python. Here is some code to get you started:

```
import pandas

data_frame = pandas.read_csv("data/basic_work_orders.csv")

print(data_frame)
```

Some simple data manipulation which can be used to answer some of the following questions:

```
# Filter rows by criteria
print(data_frame[data_frame['Machine Type'] == "TRUCK 001"]) # All Work Orders on TRUCK 001
print(data_frame[data_frame['Main Part Replaced'] == "Engine"]) # All Work Orders replacing Engines

print(data_frame[(data_frame['Main Part Replaced'] == "Engine")
                 &
                 (data_frame['Machine Type'] == "TRUCK 001")]) # All Work Orders replacing an engine where the machine type is TRUCK 001

print(data_frame[(data_frame['Main Part Replaced'] == "Engine")
                 |
                 (data_frame['Machine Type'] == "TRUCK 001")]) # All Work Orders replacing an engine or where the machine type is TRUCK 001
```

Further information on indexing and selecting data with Pandas can be found [here](http://pandas.pydata.org/pandas-docs/version/0.15.2/indexing.html)

```
# Get all values of a column
print(data_frame['Main Part Replaced'].values)

# Get all values of a column (only list each value once)
print(set(data_frame['Main Part Replaced'].values))

# Get the values of the 3rd row. Note: rows start from index 0, hence index 2 corresponds to the third row
print(data_frame.loc[2].values)

# Get the Machine Type of the 4th row
print(data_frame.loc[3]['Machine Type'])
```

### Questions

*Questions with a * ** are generally harder and more open-ended than the others, if you don't feel like doing them don't worry. May be a good option for you both to work together*

**1.** Which Machine type has the most work orders, and how many are there?

**2.** Which Machine type has the least work orders, and how many are there?

**3.*** Rank each vehicle by the number of work orders (more is higher ranked)

Print some output similar to:
```
MACHINE_TYPE1 (400 work orders)
MACHINE_TYPE3 (320 work orders)
MACHINE_TYPE2 (90 work orders)
```

**4.** Across all vehicles, what was the part replaced the most?

**5.*** Do you notice any patterns between the part most replaced and the dates they were broken? You don't have to answer this one by code, this requires some manual inspection. You could then verify your answer via the use of code.

A real life case could involve 1 million work orders. That's too many to inspect manually, you could study a subset and reach a hypothesis then use code to test your hypothesis against the entire set of data.

**6.** Write a brief readme file using markdown for the GitHub repo.

# Task 4 - Data Analysis and Graphing

### Background

The next dataset is the file "engine_work_orders_with_labour_hrs.csv". It shows how long an individual maintenance person took to replace an engine on TRUCK 001.  We want to compare the performance of workers in changing engines.

Before we commence the tasks to summarise the data, it is necessary to understand what types of data we are dealing with and what charts and summary statistics are applicable. Watch [this video](https://www.youtube.com/watch?v=hZxnzfnt5v8) and jot notes about the most important learning points.

### Questions

**1.**  For each of the columns in the dataset above, write down what basic data types they are according to the video?  State what variables would be suitable to use 'average' measures for.

**2.**  For replacing engines, which employee, on average works the fastest?  

**3.** Is there an issue with using the average labour hours to measure performance? If so, why? And what could be a better metric to use?

**4.** Write code which calculates for each maintainer:

- The average performance
- The median performance
- The average performance with outliers removed
- The median performance with outliers removed

Which metric is more sensitive to outliers?

**5.*** How would you determine an outlier computationally (without manually inspecting the data)?

**6.** Create a bar chart displaying each employee in the x-axis vs. your chosen performance metric at replacing engines on the y-axis

**7.*** Create a bar chart displaying each employee in the x-axis vs. all four performance metrics on the y-axis (4 bars per employee)

**8.** Using your performance metric, write a function which can predict the amount of hours it will take for a person to fix an engine, so if I asked you "How long will it take John Carmack to replace this engine?" you can give me an estimate of expected time, with some idea of how this time may vary.

**9.**  What type of chart is handy for showing variance?  Use this type of chart in MatPlotLib to show the answer to the previous task. [See this URL for a hint](https://www.google.co.uk/search?q=box+plot)

# Task 5 – Data Cleaning

**Please let me know when you reach here as I might have to write up another task!!**

Most of the time any data you receive in real life is in a horrible format with embedded errors. In general a data analyst will spend 70 to 80% of their time cleaning and restructuring data before analysis. This process of cleaning and preparing data is often called ‘munging’. Python along with pandas provide very powerful methods to munge data. The data used is in the file "unclean_work_orders_with_labour_hrs.csv"

### Questions

**1.** Can you write a function to clean the data – fix spelling mistakes and remove rows which have a significant amount of missing data (it may be worth keeping rows which have at least some relevant data). You will need to do this step before you do any further analysis. Use python to clean up the data until it is ready for conducting analysis and charting.  Justify why you think the data is ready.

Hint: Look at the set of all possible values for each column to see all possible errors, omissions and spelling mistakes

**2.** Where the Labour Hours data is missing but the rest of the data is present, could you substitute a value?  What would you choose and why?

**3.** Create bar charts and box plots as in the previous task for each part in the data.

**4.** Create a function which takes both the part being replaced and the person assigned to it, to predict the number of hours it will take to replace it.

**5.** One of the benefits of using Python is the community of coders who use it.  This community is especially friendly and welcomes people of all ages and ability.  Find out if there are any organisations in Oxford associated with the Python language, along with meetups that you could attend.

**6.** Present your notebooks to Alex and Charles, explain how you achieved your answers, and any interesting things you learned.  You should aim for 15 minutes presentation followed by 5 minutes of questions.
