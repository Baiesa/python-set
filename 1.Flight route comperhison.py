'''
1. Python Sets Adventure

Objective:
The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, 
ranging from basic operations to advanced manipulations and best practices. You will correct given codes, 
use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
'''



our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_distination = our_routes.intersection(competitor_routes)
print("Common flights to our airlines",common_distination)

unique_to_our_airlines = our_routes.difference(common_distination)
print("Distination unique to our airlines",unique_to_our_airlines)

if not common_distination:
    print("Neither airlines shares any distination")
else:
    all_distinations = our_routes.union(competitor_routes)
    print("Distanion that neither airlines shares: ")