# Python-Assignmemt1
This assignmet is about Python Data Types

**Python Basics: Data types**

1. Use the **constructor methods** to create different data types in python (integer,float,string,list,tuple,dictionary,set etc.). Also use **object literals** to create those data types.
2. Operators in python [https://www.w3schools.com/python/python\_operators.asp](https://www.w3schools.com/python/python_operators.asp)
  1. Create two operands and play around using different operators

1. Once you create an object of each data type, run **dir(object)**. Navigate the **magic methods/dunder methods** and other methods and attributes of each object. Try to implement those methods and attributes as many as possible.

Eg: a=int(5)

dir(a)

print(a.\_\_add\_\_(5))

Implementing above dunder method is same as print(a+5)

Verify the data types using methods **type** and **isinstance.**

1. Learn different ways to format the string.

Tutorials on [https://realpython.com/python-formatted-output/](https://realpython.com/python-formatted-output/)

Try:

![](RackMultipart20230308-1-pr6h9z_html_f874078543895464.png)

1. Familiarize yourself with indexing in python.Iterables can be accessed using index values in python. Eg: list, tuple,dict, set
  1. Create a list of items.

Eg:countries= ["Finland","Sweden","Denmark","Netherlands","Germany","Norway","Iceland"]

  1. Find the index of "Sweden".
  2. Get all the items except the first
  3. Get all the items except the last
  4. Find the last item using negative indexing
  5. Find the last three item using negative indexing
  6. Grab all the items with odd indices
  7. Find the first and last item for the list
  8. Get ["Netherlands","Germany","Norway"] using negative indexing
  9. Reverse the list
  10. What is the output of countries[::-2]
  11. What is the output of countries[1:100:2]?
  12. What is the output of countries[len(countries)-1:0:2]?
  13. Get the output ['Germany', 'Netherlands', 'Denmark']
  14. Use enumerate method to get index and values in the list

1. Exercise on dictionaries
  1. Given the two lists of same length, create a dictionary using a list as keys and another list as values without using loop

Eg: ["a","b","c","d"],[1,2,3,4] lists should be made {'a': 1, 'b': 2, 'c': 3, 'd': 4}

**Hint: zip method**

  1. Create two dictionaries, merge them into one.

**Hint: update method/dictionary unpacking**

  1. Given the list of students, assign them the course.

Students=["Duy", "Laxmi","Antonio","Maria"]

Course["Python","Database","ML"]

Should result to the new dictionary students\_profile=

{'Duy': ['Python', 'Database', 'ML'], 'Laxmi': ['Python', 'Database', 'ML'],

'Antonio': ['Python', 'Database', 'ML'],'Maria': ['Python', 'Database', 'ML']}

  1. Modify Antonio's course to ["JavaScript","Database","NodeJS"]
  2. Add "ReactJs" to Anonio's course
  3. Replace Antonio's "ReactJs" to "Vuejs"
  4. Remove an item from dictionary

**Hint: use del statement or pop/ popitem method. Observe the differences**
