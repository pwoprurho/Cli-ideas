"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 24/01/25
Python code to get details of an element in the periodic table
Using the atomic number of the Element
"""
import periodictable
print("This code that gives the information of an eleent by it's atomic number")
atomic_number = int(input("Enter the atomic number: "))
element = peiodictable.elements[atomic_number]
print(f"Atomic number = {element.number}")
print(f"Symbol = {element.symbol}")
print(f"Atomic mass = {element.mass}")
print(f"Atomic Density = {element.density}")
