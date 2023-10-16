{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "506bf67f",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 5\n",
    "y = 7\n",
    "\n",
    "j = x*y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4a240a78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n"
     ]
    }
   ],
   "source": [
    "print(j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e7019e8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "77b844f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = 'Nnenna'  #string\n",
    "\n",
    "age = 27"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e44b44b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27\n"
     ]
    }
   ],
   "source": [
    "print(age)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb001761",
   "metadata": {},
   "source": [
    "# Intro to Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "afd4806c",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = 'Timothy'\n",
    "name2 = 'timothy'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4bb7843b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name == name2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c5a76cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variables\n",
    "# Variable types\n",
    "# Operators\n",
    "# How to write comments\n",
    "\n",
    "# Python Expressions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8f0ea29",
   "metadata": {},
   "outputs": [],
   "source": [
    "Scenario1\n",
    "# Timothy if my friend. He is 30 years old and earns $2000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1cfd6750",
   "metadata": {},
   "outputs": [],
   "source": [
    "# TAssk: convert the scenario to code in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "15fce5f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = \"Timothy\"\n",
    "age = 30\n",
    "income = 2000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "25a92dab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Timothy'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "41d2eccd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Timothy\n"
     ]
    }
   ],
   "source": [
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "30448e5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "print(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "da7eeb0a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Income' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_111860\\1902992472.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mIncome\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'Income' is not defined"
     ]
    }
   ],
   "source": [
    "print(Income)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d6b757bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60000"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "30 * 2000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f815d6d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60000"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age * income"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1e25cc6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "name3  = 'Besi`'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d35b6fc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Besi`\n"
     ]
    }
   ],
   "source": [
    "print(name3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "523f6e31",
   "metadata": {},
   "outputs": [],
   "source": [
    "# james is a teacher in St. Joseph College. \n",
    "#He teaches math, phy and chem. He is 45 years old and currently been teaching for 20 yesrs\n",
    "\n",
    "Represent the information using variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "522aa8f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "teacherName = \"james\"\n",
    "college = \"St. Joseph\"\n",
    "subject1 = 'math'\n",
    "subject2 = 'phy'\n",
    "subject3 = 'chem'\n",
    "teacherAge = 45\n",
    "experience = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ad3291d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rules for Creating variables\n",
    "\n",
    "1. Keep the variable name short and meaningful. It should suggets the value it holds\n",
    "2. Observe a consistent naming convention\n",
    "- Camel case # the first word inthe name is all small case and the first letter of each succeding word is capitaliozed\n",
    "- Snake case # all words in the name are small letters seperated by an underscore\n",
    "\n",
    "3. Always assign values to a variable when craeted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25f6f129",
   "metadata": {},
   "outputs": [],
   "source": [
    "myname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f277326",
   "metadata": {},
   "outputs": [],
   "source": [
    "myName"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "979ef355",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8d87cad",
   "metadata": {},
   "outputs": [],
   "source": [
    "tName = \"james\"\n",
    "colge = \"St. Joseph\"\n",
    "subj1 = 'math'\n",
    "subj2 = 'phy'\n",
    "subj3 = 'chem'\n",
    "tAge = 45\n",
    "expr = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fdc99d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise:\n",
    "\n",
    "Agatha is the second child in a household of 6 kids. She is the first daughter and attends the All Girls High School in her d\n",
    "district. Every dy she comes to school with a lunchbox containing 10 toffies, 2 muffins, 3 oranges and 2 eggs.\n",
    "She owes her friend Simi the sum of $15 and has promisted to settle it with 5 toffies,  a muffin and an egg.\n",
    "\n",
    "represent these in code using only variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e782f63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "562e0d72",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Comments\n",
    "\n",
    "# Single line commenets   STARTS WITH A #\n",
    "\n",
    "# Multiple line comments   STARTS AND ENDS WITH \"\"\"  \"\"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5096d54",
   "metadata": {},
   "outputs": [],
   "source": [
    "# EXAMPLE OF SINGLE LINE COMMENT\n",
    "\n",
    "x  = 7\n",
    "y = 9\n",
    "# we next multiply the variables\n",
    "j = x*y # computing the product of x and y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e754823d",
   "metadata": {},
   "outputs": [],
   "source": [
    " # Example of mulple line comments\n",
    "\n",
    "studAge = 30\n",
    "\n",
    "grade = 'A-'\n",
    "\n",
    "\"\"\"\n",
    "Grades are computed usingt he following scale\n",
    "A : 80 to 100\n",
    "B:  70 to 80\n",
    "C: 60 to 70\n",
    "F: below 60\n",
    "\"\"\"\n",
    "\n",
    "studClass = 'SSS1'\n",
    "\n",
    "grdMonth = 'July 2024'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7bb7aaa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "text = \"\"\"\n",
    "Grades are computed usingt he following scale\n",
    "A : 80 to 100\n",
    "B:  70 to 80\n",
    "C: 60 to 70\n",
    "F: below 60\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "87af9ae0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Grades are computed usingt he following scale\n",
      "A : 80 to 100\n",
      "B:  70 to 80\n",
      "C: 60 to 70\n",
      "F: below 60\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16cf6df0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variable types\n",
    "\n",
    "int\n",
    "float\n",
    "string\n",
    "tuple\n",
    "set\n",
    "list\n",
    "dictionary\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2818d59a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Numerics\n",
    "\n",
    "age = 45"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d0f8e75d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check the variable type that age is\n",
    "\n",
    "type(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b0ed69c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "income = 9876.98"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4cd1c567",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(income)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9d2fa112",
   "metadata": {},
   "outputs": [],
   "source": [
    "myName = 'Korede'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "78f63d03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myName)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cb88812",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type Casting\n",
    "\n",
    "This allows us to convert one data type to another"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3c7b1deb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "income = 688.90\n",
    "type(income)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e14b04c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# casting income to an integer\n",
    "\n",
    "income2 = int(income)\n",
    "type(income2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4563aa0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "688"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "income2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "0b02b25c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# a number can be expressed as a string\n",
    "\n",
    "height = \"7.78\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "34836397",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(height)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "62669867",
   "metadata": {},
   "outputs": [],
   "source": [
    "height2 = float(height)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a6540ed6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.78"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "height2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "2269f222",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(height2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee109ace",
   "metadata": {},
   "source": [
    "# Intro Example"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1df51ee7",
   "metadata": {},
   "source": [
    "## into Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "929f744a",
   "metadata": {},
   "outputs": [],
   "source": [
    "xname = 'Immaculate'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2836864",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c794222",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e1d333f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "fc1167cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Immaculate'"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b30a219c",
   "metadata": {},
   "outputs": [],
   "source": [
    "xname = 'Francis'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2ca0b2db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Francis'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a02d8228",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}