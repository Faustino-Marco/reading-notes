# Ten Thousand Game 1

## Read

### [How to use Random Module](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)
- import random
- print random.randint(0, 5)
  - outputs 1,2,3,4,5
- random.random()*100
  - output between 0-100
- random.choice( ['red', 'black', 'green'] )
  - random.choice(my_list)
- x = [[i] for i in range(10)]
  - shuffle(x)
    - print(x) outputs array 0-10 in shuffled order
- random.randrange(start, stop, [step])
```
import random
import itertools

outcomes = { 'heads':0,
             'tails':0,
             }
sides = outcomes.keys()

for i in range(10000):
    outcomes[ random.choice(sides) ] += 1

print 'Heads:', outcomes['heads']
print 'Tails:', outcomes['tails']
```

### [What is Risk Analysis](https://www.edureka.co/blog/risk-analysis-in-software-testing/)
- Risk: probability of an unwanted incident
- software testing: id risks in apps or software you built, prioritizing them to test
  - then assign level of risk
- Risk Analysis
  - at beginning
    - highlights potential problem areas
    - test plan created in consideration of risks
- Potential risks
  - use of new hardware
  - use of new tech
  - use of new automation tool
  - sequence of code
  - availability of test resources for the application
- Unavoidable risks
  - time allocated for testing
  - defect leakage due to complexity/size of app
  - urgency from clients to deliver product
  - incomplete requirements
- Address risks
  - risk assessment review meeting
  - use max resources to work on high-risk areas
  - create risk- assessment database for future use
  - ID and notice risk magnitude indicators: high, med, low
    - high
      - risk is high, non-tolerable company may face loss
    - med
      - tolerable but not desirable, company may suffer financially but limited risk
    - low
      - tolerable, little or no external exposure or no financial loss
- Risk assessment
  - 3 perspectives
    - by effect
      - impact of condition, event, action
    - by cause
      - scan problem and find most probable reason behind it
    - by likelihood
      - this is to say there is a probability a requirement won't be satisfied
  - search the risk
  - analyze the impact of each risk
  - ID measures for the risk

### [Test Coverage](https://martinfowler.com/bliki/TestCoverage.html)
- not a measure of quality
- used to find untested code
- high coverage is too easy to attain with low quality testing
- good tests don't just examine things that rarely go wrong
- slow tests can be moved to a larger stage in your deployment pipeline
  - or even pull them out of the pipeline and run them periodically

## Videos

### [Big O Notation](https://www.youtube.com/watch?v=v4cd1O4zkGw)
- Algorithmic Efficiency
  - O(1) - pigeon
  - O(N) - internet (based on size)
- 4 rules
  - add different steps
  - drop constants
  - different inputs => different variables
  - Drop non-dominate terms
- this is only talking about O(N) time, right?

## Bookmark and Review / Further Reading

### [Python Random](https://docs.python.org/3/library/random.html)

### [What is Dependency Injection](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/)

## Things I'd like to Know more About

- I'm fascinated by risk analysis I hope we'll go into it in further depth in class. If we don't I'll research it more on my own. I'm familiar with financial investment risk analysis, but less familiar with business enterprise Risk Analysis and software dev RA.
- Based on the article about test coverage, I don't yet feel confident that I understand how to examine test coverage itself. 
- I think I have a good idea of how big O works but I want more practice differentiating between time and space under the umbrella of big O