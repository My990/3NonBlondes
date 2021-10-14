# 3NonBlondes
week 8 project
# Requirements: MCMC Simulation of a Supermarket
​
At the DOODL Supermarket chain we would like to understand our customers better in order to optimize the layout, staffing and service of our supermarkets. We would like you and your team to model the way customers move through a representative shop. Our main business goals are:
​
* understand customer behavior
* explain customer behavior to our non-data staff
* optimize staffing so that the queues do not get unnecessary long
​
We are using the following model supermarket with six areas: entrance, fruit, spices, dairy, drinks and checkout.
​
![](market.png)
​
We are interested in optimizing the number of open checkouts.
For that, we would like to simulate customer behavior over a typical business day.
The model should help explaining the business data to staff.
​
The data team wants to calculate descriptive statistics from the output.
These should be as close to the real data as possible.
They also would like to modify probabilities to play through scenarios like:
​
    "what happens if customers stay in the fruit section longer?" 
​
----
​
## 1. User Requirements
​
- the supermarket has four aisles: fruit, dairy, spices, drinks and a checkout
- users can observe multiple simulated customers to visit locations in the supermarket.
- the simulation can be run many times to see how dense the different sections of the supermarket are over time, how many people go to the checkout etc.
- the output of the simulation should be a CSV file, similar to the input
​
#### Example output:
​
    07:00:00,Jack Sparrow,entrance
    07:01:00,Jack Sparrow,fruit
    07:02:00,Elizabeth I,entrance
    07:03:00,Jack Sparrow,spices
    07:03:00,Elizabeth I,dairy
    07:07:00,Elizabeth I,spices
    07:11:00,Jack Sparrow,checkout
​
----
​
## 2. System Requirements
​
### 2.1 The Model:
​
- the model we use is a Monte Carlo Markov Chain (MCMC)
- assume the **Markov Property**: the probability of the next state depends only on the previous state
- in a first attempt, determine state changes with fixed probabilities *p(fruit)*, *p(drinks)* etc (random weighted choice)
- extend the program to use conditional probabilities (depends on where they come from). This can be described as a *transition probability matrix*
- once a customer reaches the checkout, they leave forever (they are considered churned)
- test the model with dummy probabilities that you set manually
- the probabilities are calculated from 5 data files (`monday.csv` to `friday.csv`). This can be done in a separate EDA notebook
​
----
​
### 2.2 The simulator program:
​
- simulate a single customer first
- the simulator prints each location a customer visits (*"customer #1 is now buying fruit"*)
- extend the simulation to simulate 3, then to 100 customers
- extend the simulation to simulate 1-minute timesteps over a day from 7:00 to 22:00. Test on a 10-minute interval first.
- extend the simulation to add new customers randomly: every minute, roll a die. On a 5, add one new customer. On a 6, add two.
- replace the adding of customers by sampling from a Poisson distribution
- replace the adding of customers by 1+ normal distributions that catch peak times of the day (Gaussian Mixture Model)
​
#### 2.2.1 Pseudocode for the simulation
​
    1. increase the time of the supermarket by one minute
    2. for every customer determine their next state
    3. output all state changes
    4. remove churned customers from the supermarket
    5. generate new customers at their initial location
    6. repeat from step 1
​
----
​
### 2.3 The output:
​
- produce a CSV output
- include a timestamp column in the output
- give every customer a randomly generated name
- plot the number of customers reaching the checkout over the day
- simulate 1000 days and plot the distribution of customers reaching the checkout per hour as a boxplot
​
----
​
## 3. Non-Functional Requirements:
​
- the implementation should be done in Python
- the project is kept in a public GitHub repository
- the project has a `README.md` file with a few notes how to install and run the program
- the project has a `requirements.txt` file
- the code should be checked with `pylint` to comply with the PEP8 style guide
- the code should be structured into multiple functions
- optionally, the code may use classes
- optionally add an `argparse` interface
