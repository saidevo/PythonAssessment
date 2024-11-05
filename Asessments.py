{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8ed54f4f-5c10-4fa7-a0df-1d7b44f36d36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0\n"
     ]
    }
   ],
   "source": [
    "people=60\n",
    "bus_seats=15\n",
    "print(60/15)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "33171b7d-f386-42b6-bef2-e854564767c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Temperature in Celsius: 36.39°C\n"
     ]
    }
   ],
   "source": [
    "farenheit=float(97.5)\n",
    "celsius= (farenheit-32)*5/9\n",
    "print(f\"Temperature in Celsius: {celsius:.2f}°C\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c38fdb1a-aad9-4bae-b381-0944a8aafb8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Temperature in Fahrenheit: 131.30°F\n"
     ]
    }
   ],
   "source": [
    "celsius=float(97.5)\n",
    "fahrenheit= (farenheit+9/5)+32\n",
    "print(f\"Temperature in Fahrenheit: {fahrenheit:.2f}°F\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2b54e3ca-e774-43f8-811c-0b5fd4158ae3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2025\n",
      "343000\n"
     ]
    }
   ],
   "source": [
    "a=int(20)\n",
    "b=int(25)\n",
    "c=int(30)\n",
    "d=int(40)\n",
    "print(int(20+25)**2)\n",
    "print(int(30+40)**3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "4c726322-1682-4ef1-b988-839ef2f5de87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value 10\n",
      "enter a value 10\n",
      "enter a value 10\n",
      "enter a value 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variance: 0.0\n",
      "0.0\n",
      "49\n"
     ]
    }
   ],
   "source": [
    "a= float(input(\"enter a value\"))\n",
    "b= float(input(\"enter a value\"))\n",
    "c=float(input(\"enter a value\"))         \n",
    "d= float(input(\"enter a value\"))\n",
    "number= [a, b, c, d]\n",
    "mean = sum(number)/len(number)\n",
    "v=(a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2+ (d - mean) ** 2\n",
    "\n",
    "variance = v / len(number) \n",
    "\n",
    "print(\"Variance:\", variance)\n",
    "\n",
    "std_deviation = variance ** 0.5\n",
    "print(std_deviation)\n",
    "m=1.23\n",
    "b=0.045\n",
    "x=sum(number)\n",
    "y=m*x+b\n",
    "print((int(y)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "2ad705ec-3aa5-4b09-bb96-578d63e2a05e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is km to cm 500000\n",
      "this is km to meters 1.23\n",
      "this is km to mm 5000000\n",
      "this is km to c 500000\n",
      "this is km to feet 16404.2\n",
      "this is km to yards 5468.049999999999\n"
     ]
    }
   ],
   "source": [
    "km = 5\n",
    "cm = km * 100000\n",
    "print(\"this is km to cm\", cm)\n",
    "meters = km * 1000\n",
    "print(\"this is km to meters\", m)\n",
    "mm = km * 1000000\n",
    "print(\"this is km to mm\", mm)\n",
    "cents = km * 100000\n",
    "print(\"this is km to c\", cents)\n",
    "feet = km * 3280.84\n",
    "print(\"this is km to feet\", feet)\n",
    "yards = km * 1093.61\n",
    "print(\"this is km to yards\", yards)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "d166a287-05a1-4914-8d53-958baf29704f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MB 10240\n",
      "KB 10485760\n",
      "TB 0.009765625\n",
      "PB 9.5367431640625e-06\n"
     ]
    }
   ],
   "source": [
    "gb=10\n",
    "# 1 gb = 1024 mb\n",
    "MB= gb*1024\n",
    "print(\"MB\", MB)\n",
    "KB=gb* 1024*1024\n",
    "print(\"KB\", KB)\n",
    "TB=gb/1024\n",
    "print(\"TB\", TB)\n",
    "PB=gb/(1024*1024)\n",
    "print(\"PB\", PB)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "50542cb6-cb43-4155-a3b0-d551a4c0868e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your name sainath\n",
      "enter your age 27\n",
      "enter your height 5.6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name:sainath of the person, Age:27 of the person, Height:5.6 of the person\n"
     ]
    }
   ],
   "source": [
    "# The details of the person: Name:name of the person, Age:age of the person, Height:height of the person\n",
    "name=input(\"enter your name\")\n",
    "age=input(\"enter your age\")\n",
    "height=input(\"enter your height\")\n",
    "res = f\"Name:{name} of the person, Age:{age} of the person, Height:{height} of the person\"\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "65e4f36e-948f-4910-acb0-33b9dbc5cf8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "31.249999999999993\n"
     ]
    }
   ],
   "source": [
    "weight=80\n",
    "height=1.6 # give in meters\n",
    "\n",
    "bmi = (weight / (height ** 2))\n",
    "\n",
    "print(bmi)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "af9ebffc-aff9-4dce-a9e8-faa9e9b7115b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name:Jayaram, Age:1, Height:3, Weight:10\n"
     ]
    }
   ],
   "source": [
    "name=\"Jayaram\"\n",
    "age=1.6\n",
    "height=3.5356234\n",
    "weight=10.343856783\n",
    "\n",
    "# Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344\n",
    "\n",
    "res = \"Name:%s, Age:%d, Height:%d, Weight:%d\"%(name, age, height, weight)\n",
    "print(res)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "86293d7b-4dbc-4277-b0e0-353449a6ec1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2³\n"
     ]
    }
   ],
   "source": [
    "base=2\n",
    "exponent=3\n",
    "# Use: 2\\u00b3\n",
    "res=f\"{base}\\u00b3\"\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "d088497b-351f-41f1-81fe-562dbac1d793",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcdefghijklm  fyuu ABCDEFGHIJKLM  FYUU\n"
     ]
    }
   ],
   "source": [
    "# Take three upper case letters from the user convert in to small case.\n",
    "sainath=\"ABCDEFGHIJKLM  fyuu\"\n",
    "convert=sainath.lower()\n",
    "f = sainath.upper()\n",
    "print(convert, f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "c13ddd89-ac79-4971-bbbb-270f5672c66a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "105 21.0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "0d094486-d4ac-4a43-a540-2694c79b13c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total cost :  105\n",
      "Average :  21.0\n",
      "Maximum_value:  35\n",
      "Minimum_value: 10\n"
     ]
    }
   ],
   "source": [
    "# Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.\n",
    "\n",
    "Apple=20\n",
    "Oranges=10\n",
    "Pineapple=15\n",
    "Kindaapple=25\n",
    "middleapple=35\n",
    "\n",
    "a = [Apple, Oranges, Pineapple, Kindaapple, middleapple]\n",
    "\n",
    "total = sum(a)\n",
    "print(\"Total cost : \", total)\n",
    "avg = total / len(a)\n",
    "print(\"Average : \", avg)\n",
    "\n",
    "max_of = max(a)\n",
    "print(\"Maximum_value: \", max_of)\n",
    "\n",
    "min_of = min(a)\n",
    "print(\"Minimum_value:\", min_of)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e458ebe1-3f24-4c05-b9c4-80e1dc10c344",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 13. Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8a181986-d8cf-4580-82ef-31644178c885",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 is an odd number.\n"
     ]
    }
   ],
   "source": [
    "# Taking input from the user\n",
    "number = int(input(\"Enter a number: \"))\n",
    "\n",
    "# Checking if the number is even or odd\n",
    "if number % 2 == 0:\n",
    "    print(f\"{number} is an even number.\")\n",
    "else:\n",
    "    print(f\"{number} is an odd number.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "aa25f3c4-73c8-4db8-b8db-7551a3d38044",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11.0 is a positive number.\n"
     ]
    }
   ],
   "source": [
    "# take number from the user decide whether it is positive number or negative number\n",
    "number = float(input(\"Enter a number: \"))\n",
    "if number > 0:\n",
    "    print(f\"{number} is a positive number.\")\n",
    "else:\n",
    "    print(\"The number is negative.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "54c656e8-5b24-4f7e-b9f2-4eca74b19ac0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The length of the string is 1.\n"
     ]
    }
   ],
   "source": [
    "# take a string from the user print the length. if the user not given anything then show an error message\n",
    "user_input = input(\"Enter a string: \")\n",
    "\n",
    "# Checking if the user provided input\n",
    "if user_input:\n",
    "    print(f\"The length of the string is {len(user_input)}.\")\n",
    "else:\n",
    "    print(\"Error: No input provided. Please enter a valid string.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5a658b49-9704-4c1b-b835-4f221da2335a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 121\n",
      "enter a number 252\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. add \n",
      "2. sub \n",
      "3. mul \n",
      "4.div \n",
      "5.quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number from above options : 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "quit\n"
     ]
    }
   ],
   "source": [
    "# # 17.code to perform mathematical operations. take two numbers from the user and show the below menu\n",
    "# 1. add,\n",
    "# \t2. sub,\t\n",
    "# \t3. mul,\n",
    "#  \t4.div, \n",
    "# \t5.quit\n",
    "# \tEnter an option:\n",
    "# \t\tbased on the option need to perform an operations\n",
    "\n",
    "value_1= input(\"enter a number\")\n",
    "value_2= input(\"enter a number\")\n",
    "value_1= int(value_1)\n",
    "value_2= int(value_2)\n",
    "print(\"1. add \\n2. sub \\n3. mul \\n4.div \\n5.quit\")\n",
    "select_one = input(\"select a number from above options :\")\n",
    "select_one = int (select_one)\n",
    "\n",
    "\n",
    "if select_one == 1:\n",
    "    print(f\"addition of {value_1} + {value_2} : \", value_1 + value_2)\n",
    "elif select_one == 2:\n",
    "    print(f\"substraction of {value_1} - {value_2} : \", value_1 - value_2)\n",
    "elif select_one == 3:\n",
    "    print(f\"multiplication of {value_1} * {value_2} : \", value_1 * value_2)\n",
    "elif select_one == 4:\n",
    "    print(f\"addition of {value_1} / {value_2} : \", value_1 / value_2)\n",
    "elif select_one == 5:\n",
    "    print(f\"quit\")\n",
    "else :\n",
    "    print(\"select a option from above values\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "925cb404-8508-431e-a072-8283cebe402a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. kid \n",
      "2. mens \n",
      "3. womens\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number from above options : 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "thengofromhere\n"
     ]
    }
   ],
   "source": [
    "# 18 show the menu:\n",
    "#    \t\t 1. kids\n",
    "#     \t\t2. Men's\n",
    "#    \t\t # 3. Women's\n",
    "#     \t\tShow the corresponding message based on the selection.\n",
    "# \t\tOption:1: you are a kid\n",
    "#                                            2: you are a gentlemen\n",
    "#                                             3: you are a good women\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "print(\"1. kid \\n2. mens \\n3. womens\")\n",
    "select_one = input(\"select a number from above options :\")\n",
    "select_one = int (select_one)\n",
    "\n",
    "\n",
    "if select_one == 1:\n",
    "    print(\"you are a kid\")\n",
    "elif select_one == 2:\n",
    "    print(\"you are a gentlemen\")\n",
    "elif select_one == 3:\n",
    "    print(\"you are a good women\")\n",
    "else :\n",
    "    print(\"thengofromhere\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d5f2f513-f5e2-4783-a419-61fd3a799d39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " then print ss \n"
     ]
    }
   ],
   "source": [
    "#  19. write a program to check given substring is there in actual string or not?\n",
    "# example: act=\"python is a pure object-oriented programing language\"\n",
    "# check whether “pure” is there in act or not.\n",
    "\n",
    "act=\"python is a pure object-oriented programing language\"\n",
    "sub_string= \"pure\"\n",
    "if sub_string in act:\n",
    "    print(\" then print ss \")\n",
    "else :\n",
    "    print(\"then dont print\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "5b634dab-265e-41c3-8fae-a6c4d7df4b0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a first number 10\n",
      "enter a second number 20\n",
      "enter a third number 30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30.0\n"
     ]
    }
   ],
   "source": [
    "# 20. Take three numbers from the user and decide which is big\n",
    "value_1= input(\"enter a first number\")\n",
    "value_2= input(\"enter a second number\")\n",
    "value_3= input(\"enter a third number\")\n",
    "\n",
    "value_1=float(value_1)\n",
    "value_2=float(value_2)\n",
    "value_3=float(value_3)\n",
    "\n",
    "if value_1 >= value_2 and value_1 >= value_3 :\n",
    "    print (value_1)\n",
    "elif value_2 >=  value_1 and value_2 >= value_3:\n",
    "    print(value_2)\n",
    "else:\n",
    "    print(value_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "787dd9ff-3d2a-4da5-979b-6c47137037a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 55\n",
      "enter male/female female\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are elgible for marriage\n"
     ]
    }
   ],
   "source": [
    "#  21. Take age and gender from the user and decide whether he is eligible for \tmarriage in India or not.\n",
    "# # Age criteria: men age>24, women>21\n",
    "\n",
    "age= input(\"enter a number\")\n",
    "gender= input(\"enter male/female\")\n",
    "\n",
    "age=float(age)\n",
    "\n",
    "if (gender == \"female\" and age >= 21) or (gender == \"male\" and age >= 24):\n",
    "    print(\"you are elgible for marriage\")\n",
    "else :\n",
    "    print(\"dont marry\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "6e9673a7-102d-4202-b053-9af92fa1eecf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 6\n",
      "enter men/women men\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are elgible for theater\n"
     ]
    }
   ],
   "source": [
    "# Take an age  and gender from the user: and mention that what he/she can \tdo in india.\n",
    "# \t\"\"\"\n",
    "# \t\tconditions\n",
    "# 1. Theatre: 5 for men 7 for women\n",
    "#     \t2. Voting system: 18 for men and women\n",
    "#     \t3. Marriage in india: 23 for men and for women >21\n",
    "#     \t4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for \twomen\n",
    "#    \t \t5. For driving licence: (min:18, max:60) for men and women\n",
    "# \tEligibility:\n",
    "#    \t\t1. theatre\n",
    "# \t\t\t2.  Voting system\n",
    "# \t\t\t3.  Marriage in india\n",
    "# \t\t\t4.  For govt obs\n",
    "# \t\t\t# 5. For driving licence:\n",
    "# \tEnter an option:\n",
    "# \t\tGender:\n",
    "# \t\t\t1. men\n",
    "# \t\t\t2. women\n",
    "# \tEnter an option:\n",
    "# \t\tEnter an age of person:\n",
    "\n",
    "\n",
    "\n",
    "age= input(\"enter a number\")\n",
    "gender= input(\"enter men/women\")\n",
    "\n",
    "age=float(age)\n",
    "\n",
    "if (gender == \"men\" and age >= 5) or (gender == \"women\" and age >= 7):\n",
    "    print(\"you are elgible for theater\")\n",
    "else :\n",
    "    print(\"dont enter\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a61b1211-2371-4991-846e-3053f2cf75c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 25\n",
      "enter men/women women\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are elgible for voting\n"
     ]
    }
   ],
   "source": [
    "age= input(\"enter a number\")\n",
    "gender= input(\"enter men/women\")\n",
    "\n",
    "age=float(age)\n",
    "\n",
    "if (gender == \"men\" and age >= 18) or (gender == \"women\" and age >= 18):\n",
    "    print(\"you are elgible for voting\")\n",
    "else :\n",
    "    print(\"dont vote\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "85edb604-983e-4419-b5d7-5b0a01516c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 55\n",
      "enter men/women women\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are elgible for marriage\n"
     ]
    }
   ],
   "source": [
    "age= input(\"enter a number\")\n",
    "gender= input(\"enter men/women\")\n",
    "\n",
    "age=float(age)\n",
    "\n",
    "if (gender == \"women\" and age >= 21) or (gender == \"men\" and age >= 23):\n",
    "    print(\"you are elgible for marriage\")\n",
    "else :\n",
    "    print(\"dont marry\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b595593c-7ad9-4e47-8326-1e5092f598cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your age:  36\n",
      "enter your gender (male/female):  female\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "your not eligible for govt jobs\n"
     ]
    }
   ],
   "source": [
    "age = input(\"enter your age: \")\n",
    "gender = input(\"enter your gender (male/female): \")\n",
    "\n",
    "age=float(age)\n",
    "\n",
    "if (gender == \"female\" and (age >= 18 and age <=34)) or (gender == \"male\" and (age >= 18 and age <= 32 )):\n",
    "    print(\"you are elgible for govt jobs\")\n",
    "else:\n",
    "    print(\"your not eligible for govt jobs\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "8da371d5-734d-446f-811e-047fbe46340e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " operating systems:\n",
      "\u0001.windows\n",
      "\u0002.android\n",
      "\u0003.mac\n",
      "Enter an floors:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goto second floor and buy android mobiles\n"
     ]
    }
   ],
   "source": [
    "# 23. operating systems:\n",
    "# \t1.windows\n",
    "# \t2.android\n",
    "# \t3.mac\n",
    "# Enter an option:\n",
    "\n",
    "# If the user enters 1 then show \"Goto first floor and buy windows laptop or mobile\"\n",
    "# If the user enters 2 then show \"Goto second floor and buy adroid mobiles\"\n",
    "# If the user enters 3 then show \"Goto third floor and buy mac laptop or iphones\"\n",
    "# If the user enters other than 1 or 2 or 3 then show \"There is only three floors, please select 1 or 2 or 3\"\n",
    "\n",
    "floors = input(\" operating systems:\\n\\1.windows\\n\\2.android\\n\\3.mac\\nEnter an floors: \")\n",
    "\n",
    "if floors == \"1\":\n",
    "  print(\"Goto first floor and buy windows laptop or mobile\")\n",
    "elif floors == \"2\":\n",
    "  print(\"Goto second floor and buy android mobiles\")\n",
    "elif floors == \"3\":\n",
    "  print(\"Goto third floor and buy mac laptop or iphones\")\n",
    "else:\n",
    "  print(\"There is only three floors, please select 1, 2 or 3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "e143c0e5-03de-4c51-8e8e-11d4b40491fa",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after function definition on line 3 (569572314.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[98], line 6\u001b[1;36m\u001b[0m\n\u001b[1;33m    if age <= 1:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after function definition on line 3\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.\n",
    "\n",
    "age_category(age):\n",
    "\n",
    "\n",
    "if age <= 1:\n",
    "    print(\"baby\")\n",
    "elif 1 < age <= 3:\n",
    "    print(\"toddler\")\n",
    "elif 3 < age <= 12:\n",
    "    print(\"child\")\n",
    "elif 12 < age <= 19:\n",
    "    print(\"teenager\")\n",
    "elif 19 < age <= 65:\n",
    "    print(\"adult\")\n",
    "else:\n",
    "    print( \"old codger\" )\n",
    "\n",
    "age = int(input(\"Enter your age: \"))\n",
    "category = age_category(age)\n",
    "print(\"your age of {category}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "81e9a799-b0da-4bf1-9989-3a7fe38dd6d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number (a):  55\n",
      "Enter the second number (b):  45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55 is not divisible by 45\n"
     ]
    }
   ],
   "source": [
    "# 25.Take two number a,b from the user and check whether a is divisible by b or not\n",
    "\n",
    "a = int(input(\"Enter the first number (a): \"))\n",
    "b = int(input(\"Enter the second number (b): \"))\n",
    "\n",
    "if a % b == 0:\n",
    "  print(f\"{a} is divisible by {b}\")\n",
    "else:\n",
    "  print(f\"{a} is not divisible by {b}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "35f66be6-c832-466c-8b23-eabbee451749",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  sai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Small letter\n"
     ]
    }
   ],
   "source": [
    "# 26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or capital letter or number or special symbol\n",
    "\n",
    "\n",
    "letter = input(\"Enter a letter: \")\n",
    "\n",
    "if letter.islower():\n",
    "  print(\"Small letter\")\n",
    "elif letter.isupper():\n",
    "  print(\"Capital letter\")\n",
    "elif letter.isdigit():\n",
    "  print(\"Number\")\n",
    "else:\n",
    "  print(\"Special symbol\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "68a0b534-ac70-4e2f-b6a8-50f28257fe21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.Men\n",
      "2.Women\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter gender 4\n",
      "enter an age: \n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m gender \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter gender\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m age \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter an age:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 4\u001b[0m age \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mfloat\u001b[39m(age)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m gender\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m      6\u001b[0m      \u001b[38;5;28;01mif\u001b[39;00m age\u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5\u001b[39m:\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: ''"
     ]
    }
   ],
   "source": [
    "print(\"1.Men\\n2.Women\")\n",
    "gender = input(\"Enter gender\")\n",
    "age = input(\"enter an age:\")\n",
    "age = float(age)\n",
    "if gender==\"1\":\n",
    "     if age>=5:\n",
    "         print(\"he can got to movie\")\n",
    "     if age>=18:\n",
    "         print(\"He can apply for voting\")\n",
    "     if age>=23:\n",
    "        print(\"He can get married\")\n",
    "     if age>=18 and age<=34:\n",
    "        print(\"He can apply for govt gobs\")\n",
    "     if age>=18 and age<=60:\n",
    "        print(\"He can apply for driving licence\")\n",
    "else:\n",
    "    if age>=7:\n",
    "         print(\"She can got to movie\")\n",
    "    if age>=18:\n",
    "         print(\"SHe can apply for voting\")\n",
    "    if age>=23:\n",
    "        print(\"SHe can get married\")\n",
    "    if age>=18 and age<=34:\n",
    "        print(\"SHe can apply for govt gobs\")\n",
    "    if age>=18 and age<=60:\n",
    "        print(\"SHe can apply for driving licence\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b45ad243-c7f3-4adc-91b5-e548e648da9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bd1d1dfb-91ec-499a-b371-b2ee1ccf8526",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "number\n",
      "hello\n",
      "number\n",
      "hello\n",
      "number\n",
      "hello\n",
      "number\n",
      "Hello\n"
     ]
    }
   ],
   "source": [
    "numbers=[10,20,30,40]\n",
    "for num in numbers:\n",
    "    print(\"hello\")\n",
    "    print(\"number\")\n",
    "print(\"Hello\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1501abde-d9cb-4401-b436-6ba95097d34c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "10\n",
      "hello\n",
      "20\n",
      "hello\n",
      "30\n",
      "hello\n",
      "40\n",
      "Hello\n"
     ]
    }
   ],
   "source": [
    "numbers=(10,20,30,40)\n",
    "for num in numbers:\n",
    "    print(\"hello\")\n",
    "    print(num)\n",
    "print(\"Hello\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9293d717-52c7-4ea2-8209-8e5f4b01f1fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "10\n",
      "hello\n",
      "20\n",
      "hello\n",
      "30\n",
      "hello\n",
      "40\n",
      "Hello\n"
     ]
    }
   ],
   "source": [
    "numbers=[10,20,30,40]\n",
    "for num in numbers:\n",
    "    print(\"hello\")\n",
    "    print(num)\n",
    "print(\"Hello\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "429fc72f-1ad9-470b-b78f-281ed4a43a5f",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'false' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[32], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m num \u001b[38;5;129;01min\u001b[39;00m false:\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28mprint\u001b[39m(num)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'false' is not defined"
     ]
    }
   ],
   "source": [
    "for num in False:\n",
    "    print(num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "45472f17-cea0-4c27-a500-e7b8d6b120bd",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'bool' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[36], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m num \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m:\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28mprint\u001b[39m(num)\n",
      "\u001b[1;31mTypeError\u001b[0m: 'bool' object is not iterable"
     ]
    }
   ],
   "source": [
    "for num in False:\n",
    "    print(num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "183c7950-40bb-4ae1-a6e2-3c9ccfd11c6d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[38], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m num \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;241m100\u001b[39m:\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28mprint\u001b[39m(num)\n",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not iterable"
     ]
    }
   ],
   "source": [
    "for num in 100:\n",
    "    print(num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "377a72ce-8c21-4c57-961d-c81a85353664",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'float' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[40], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m num \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;241m221.11\u001b[39m:\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28mprint\u001b[39m(num)\n",
      "\u001b[1;31mTypeError\u001b[0m: 'float' object is not iterable"
     ]
    }
   ],
   "source": [
    "for num in 221.11:\n",
    "    print(num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "38fa5e5f-9e2f-46cc-8770-de5b65b3cc29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "for i in []:\n",
    "    print(i)\n",
    "    print(\"hi\")\n",
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "4e11f0bd-0edd-4f05-94d0-200070d81ac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+ve\n"
     ]
    }
   ],
   "source": [
    "num = 10\n",
    "if num>0:\n",
    "    print(\"+ve\")\n",
    "else:\n",
    "    print(\"-ve\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8a294bdd-1a50-47c4-8ff1-5b91e542228a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 +Ve\n",
      "3 +Ve\n",
      "2 +Ve\n",
      "5 +Ve\n",
      "-5 -ve\n",
      "6 +Ve\n",
      "-9 -ve\n",
      "its done\n"
     ]
    }
   ],
   "source": [
    "numbers=[10,3,2,5,-5,6,-9]\n",
    "for num in numbers:\n",
    "    if num>=0:\n",
    "        print (num, \"+Ve\")\n",
    "    else:\n",
    "        print (num, \"-ve\")\n",
    "print(\"its done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8eea40e8-222a-4144-9ea7-9f63a545e2b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 +Ve\n",
      "3 +Ve\n",
      "-2 -Ve\n",
      "5 +Ve\n",
      "-5 -Ve\n",
      "6 +Ve\n",
      "-9 -Ve\n",
      "its done\n"
     ]
    }
   ],
   "source": [
    "numbers=[10,3,-2,5,-5,6,-9]\n",
    "for num in numbers:\n",
    "    if num>=0:\n",
    "        print (num, \"+Ve\")\n",
    "    else:\n",
    "        print (num, \"-Ve\")\n",
    "print(\"its done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d486b0d8-e046-4648-bae5-91a1f5c8cfa2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "number=[10,-20,-30,45,67,-56]\n",
    "positive_number =0\n",
    "negative_number =0\n",
    "for num in numbers:\n",
    "    if num>=0:\n",
    "      positive_number=positive_number+1\n",
    "    else: \n",
    "      negative_number=negative_number+1\n",
    "print(positive_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7d86169d-d0fd-45d4-9b11-8ca62d621c78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 +Ve\n",
      "3 +Ve\n",
      "-2 -Ve\n",
      "5 +Ve\n",
      "-5 -Ve\n",
      "6 +Ve\n",
      "-9 -Ve\n"
     ]
    }
   ],
   "source": [
    "number=[10,-20,-30,45,67,-56]\n",
    "for num in numbers:\n",
    "    if num>=0:\n",
    "        print (num, \"+Ve\")\n",
    "    else:\n",
    "        print (num, \"-Ve\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bdf345ca-dbc1-4d89-8e23-5b29554b8777",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[21], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m p_n\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m\n\u001b[0;32m      3\u001b[0m n_n\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;241m1\u001b[39m:\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m i\u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m      6\u001b[0m         p_n \u001b[38;5;241m=\u001b[39mp_n \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not iterable"
     ]
    }
   ],
   "source": [
    "number=[10,-20,-30,45,67,-56]\n",
    "p_n=0\n",
    "n_n=0\n",
    "for i in 1:\n",
    "    if i>=0:\n",
    "        p_n =p_n +1\n",
    "    else:\n",
    "        n_n= n_n +1\n",
    "print(p_n)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1505ccaa-6e23-452c-baf5-7438ed8d2640",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 8, 11]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(5,12,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "06034391-0b2e-4a8a-96c2-e771b88d3b2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(12,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e6125b6c-d0eb-431b-b8af-bc19accafbf0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(12,3,15))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3bc8b178-5af7-4ba1-af9e-c8c1733a1866",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[2:-10:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "dc1f49ff-bc6e-4543-b7a9-5dffca5826d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cb\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[2:-11:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "502c3d23-b49a-48cb-83c1-2ce0fe3e39a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cegik\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[2:11:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "09bdd126-d84e-4d63-a3aa-925f2bd86c79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[2:-11:-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "34c25715-c9d0-48fa-b6f9-163d893710d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[2:-9:-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d6f5fbed-d21f-4fba-969c-a65d2a79d792",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fd\n"
     ]
    }
   ],
   "source": [
    "s=\"abcdefghijk\"\n",
    "print(s[5:-9:-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "d0bfcc52-4ebd-418d-ba57-5c746b01a57c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "330\n",
      "-310\n",
      "3200\n",
      "0.018518518518518517\n"
     ]
    }
   ],
   "source": [
    "def add (a,b):\n",
    "    print(a+b)\n",
    "def sub(a,b):\n",
    "    print(a-b)\n",
    "def mul(a,b):\n",
    "    print(a*b)\n",
    "def div(a,b):\n",
    "    print(a/b)\n",
    "\n",
    "add(10,320)\n",
    "sub(10,320)\n",
    "mul(10,320)\n",
    "div(10,540)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "1f7b1f42-d674-421b-ae61-241d60c98062",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a-1, b-0,c-0,d-0\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def add(a,b=0,c=0,d=0):\n",
    "    print(f\"a-{a}, b-{b},c-{c},d-{d}\")\n",
    "    print(a+b+c+d)\n",
    "add(a=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "c9eb49fa-42d9-4db8-bd2e-22bbd11d3277",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a-10, k=()\n",
      "a-1, k=(2, 3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "def add(a,*k):\n",
    "    print(f\"a-{a}, k={k}\")\n",
    "add(10)\n",
    "add(1,2,3,4,5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "ce56e7ce-535a-490e-966d-22559e71a2c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a=10, k-{'b': 20, 'c': 30, 'd': 40}, type{'b': 20, 'c': 30, 'd': 40}\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "add() takes 1 positional argument but 6 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[89], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00ma\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, k-\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mk\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, type\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mk\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m add(a\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m, b\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m20\u001b[39m, c\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m30\u001b[39m, d\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m40\u001b[39m)\n\u001b[1;32m----> 4\u001b[0m add(\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m3\u001b[39m,\u001b[38;5;241m4\u001b[39m,\u001b[38;5;241m5\u001b[39m,\u001b[38;5;241m6\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: add() takes 1 positional argument but 6 were given"
     ]
    }
   ],
   "source": [
    "def add(a,**k):\n",
    "    print(f\"a={a}, k-{k}, type{k}\")\n",
    "add(a=10, b=20, c=30, d=40)\n",
    "add(1,2,3,4,5,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "8170a6d8-85a0-4ea5-8ae4-4a65b059bc6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "k=[1,2,3,4]\n",
    "def fun(x):\n",
    "    x[0]=20\n",
    "fun(k)\n",
    "print(k)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "b8de34c9-29e7-4028-b77f-6a4a4ebd8fd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "k=0\n",
    "def fun(x):\n",
    "    x=20\n",
    "fun(k)\n",
    "print(k)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "3a9bd2a7-247a-4dc5-96a9-c995cb7a839e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<function add at 0x00000278D217F9C0>\n",
      "2717944117696\n",
      "<class 'function'>\n"
     ]
    }
   ],
   "source": [
    "def add(x,y):\n",
    "    print(x+y)\n",
    "print(add)\n",
    "print(id(add))\n",
    "print(type(add))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "380099b3-e436-42ea-ab74-05fa949fa16e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a=100, b=200\n",
      "300\n",
      "Done\n"
     ]
    }
   ],
   "source": [
    "x =100\n",
    "y= 200\n",
    "a = 10\n",
    "def add (a,b):\n",
    "    print(f\"a={a}, b={b}\")\n",
    "    z=a+b\n",
    "    x=10\n",
    "    print(z)\n",
    "add(x,y)\n",
    "print(\"Done\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "04f68049-d8ef-4360-90e2-e69a45d9c403",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#26. take a string from the user and check contains only digits or not? \n",
    "s = input()\n",
    "print(s.isdigit())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dd1957a5-557d-4314-b782-dda4abba440f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter string:  45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#27. take a string from the user and check contains only  alphabets or not? \n",
    "print(input(\"Enter string: \").isalpha())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e7161edc-fbe7-4727-bba6-c80449d6b9a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 007\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#28. take a string from the user and check contains only  special chars or not? \n",
    "s = input()\n",
    "print(s.isalnum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d5fce7bd-8efc-4de4-94bd-f0bbae861290",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter string:  \"sainath\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#29.take a string from the user and check contains only  capital letters or not? \n",
    "print(input(\"Enter string: \").isupper())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "60486d07-c3b8-41d2-986d-c9e9330c4a3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter string:  SAinath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#30.take a string from the user and check contains only  small letters or not? \n",
    "print(input(\"Enter string: \").islower())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "121a57b0-f666-438e-8245-d3f4dca53df0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "-20\n"
     ]
    }
   ],
   "source": [
    "def add (x,y):\n",
    "    return x+y\n",
    "def sub (x,y):\n",
    "    return x-y\n",
    "def multiplication (x,y):\n",
    "    return x*y\n",
    "x=10\n",
    "y=20\n",
    "result1= add (x,y)\n",
    "result2= sub (20,40)\n",
    "result3= multiplication(x,y)\n",
    "result4= result1-result2\n",
    "\n",
    "result5= result1*result4\n",
    "print(result1)\n",
    "print(result2)\n",
    "# print(result3)\n",
    "# print(result4)\n",
    "# print(result5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a13e3207-fd70-4c50-8e26-239d8631ad97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets :  df\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contains only alphabets\n"
     ]
    }
   ],
   "source": [
    "# 27. take a string from the user and check contains only  alphabets or not?\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets : \")\n",
    "count = 0\n",
    "for i in user_input:\n",
    "    if not((i >= \"a\" and i <= \"z\") or (i >= \"A\" and i <= \"Z\")) :\n",
    "        print(\"contains others\")\n",
    "        break\n",
    "    else:\n",
    "        count += 1\n",
    "if count == len(user_input):\n",
    "    print(\"contains only alphabets\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cbd6595e-b0db-48f4-b0da-7c9fa11346cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with Specail chars :  @\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contains only Specail chars\n"
     ]
    }
   ],
   "source": [
    "# 28. take a string from the user and check contains only  special chars or not?\n",
    "\n",
    "user_input = input(\"Enter a word with Specail chars : \")\n",
    "count = 0\n",
    "for i in user_input:\n",
    "    if not( (i >= \"a\" and i <= \"z\") or (i >= \"A\" and i <= \"Z\") or (i >= \"0\" and i <= \"9\") ) :\n",
    "        print(\"contains only Specail chars\")\n",
    "        break\n",
    "    else:\n",
    "        count += 1\n",
    "if count == len(user_input):\n",
    "    print(\"contains others \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7e32fc64-0dd0-47be-9e04-82c15fd955c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets :  AAAA\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contains only Capital Letters\n"
     ]
    }
   ],
   "source": [
    "# 29.take a string from the user and check contains only  capital letters or not?\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets : \")\n",
    "count = 0\n",
    "for i in user_input:\n",
    "    if not((i >= \"A\" and i <= \"Z\")) :\n",
    "        print(\"contains others\")\n",
    "        \n",
    "        break\n",
    "    else:\n",
    "        count += 1\n",
    "if count == len(user_input):\n",
    "    print(\"contains only Capital Letters\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9a849d29-f33d-46c1-9f31-e7bbdd4fc4c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets :  SAInath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contains others\n"
     ]
    }
   ],
   "source": [
    "# 30.take a string from the user and check contains only  small letters or not?\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets : \")\n",
    "count = 0\n",
    "for i in user_input:\n",
    "    if not((i >= \"a\" and i <= \"z\")) :\n",
    "        print(\"contains others\")\n",
    "        break\n",
    "    else:\n",
    "        count += 1\n",
    "if count == len(user_input):\n",
    "    print(\"contains only small letters\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5d9524d6-454c-4452-94c7-ae68509d7d34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple,orange,apple,grape,orange,apple,apple,orange\n",
      "apple,orange,apple,grape,orange,APPLE,APPLE,orange\n"
     ]
    }
   ],
   "source": [
    "# 31. WAP to replace last n occurrence of give string.\n",
    "# For example:”apple,orange,apple,grape,orange,apple,apple,orange”\n",
    "# source: “apple”\n",
    "# last occurrences: 2\n",
    "# replace with: APPLE\n",
    "# output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”\n",
    "\n",
    "a = \"apple,orange,apple,grape,orange,apple,apple,orange\"\n",
    "print(a)\n",
    "list_a = a.split(',')\n",
    "list_a = list_a[::-1]\n",
    "source = \"apple\"\n",
    "n = 2\n",
    "count = 0\n",
    "for i in range(0, len(list_a)):\n",
    "    if list_a[i] == source :\n",
    "        list_a[i] = \"APPLE\"\n",
    "        count += 1\n",
    "        if count == n:\n",
    "            break\n",
    "print(\",\".join(list_a[::-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3d00a5a9-95d9-4b60-9333-0fb2705a44e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains numbers and float values :  88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contains numbers \n"
     ]
    }
   ],
   "source": [
    "# 32. WAP to check given string contains numbers or not. it should consider float numbers also.\n",
    "user_input = input(\"Enter a string it contains numbers and float values : \" )\n",
    "for i in user_input:\n",
    "    if (i >= \"0\" and i <= \"9\"):\n",
    "        print(\"contains numbers \")\n",
    "        break\n",
    "else:\n",
    "    print(\"not contains numbers \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0c375534-8eca-4a20-9c45-9a1d90f7218e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets :  sainathisagoodboy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sainathisagoodboy\n"
     ]
    }
   ],
   "source": [
    "# 33. Convert the total string in to lower case. Without using lower() function.\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets : \")\n",
    "user_input = list(user_input)\n",
    "for i in range(0, len(user_input)):\n",
    "    if ((user_input[i] >= \"A\" and user_input[i] <= \"Z\")) :\n",
    "        user_input[i] = chr(ord(user_input[i]) + 32)\n",
    "\n",
    "print(\"\".join(user_input))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fe5b272d-0416-4878-8aea-f2c3b1a30196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SAINATH\n"
     ]
    }
   ],
   "source": [
    "# 34. Convert the total string in to upper case. Without using upper() function.\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets : \")\n",
    "user_input = list(user_input)\n",
    "for i in range(0, len((user_input))):\n",
    "    if ((user_input[i] >= \"a\" and user_input[i] <= \"z\")) :\n",
    "        user_input[i] = chr(ord(user_input[i]) - 32)\n",
    "\n",
    "print(\"\".join(user_input))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "55559f80-1212-476e-97d0-72f99b078887",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Menu: \n",
      "1. windows \n",
      "2. Linux \n",
      "3. Mac \n",
      "4. quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select a number from above options :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  *** You selected Mac  ***  \n",
      "Menu: \n",
      "1. windows \n",
      "2. Linux \n",
      "3. Mac \n",
      "4. quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select a number from above options :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  *** You selected Mac  ***  \n",
      "Menu: \n",
      "1. windows \n",
      "2. Linux \n",
      "3. Mac \n",
      "4. quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select a number from above options :  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===>  Select from given options please  <===\n",
      "Menu: \n",
      "1. windows \n",
      "2. Linux \n",
      "3. Mac \n",
      "4. quit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select a number from above options :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  *** Thank You!  ***  \n"
     ]
    }
   ],
   "source": [
    "'''35. Show the below menu to the user until and until user select quit and display corresponding os message\n",
    "Menu:\n",
    "1. windows\n",
    "2. Linux\n",
    "3. Mac\n",
    "4. quit\n",
    "a = \"Menu: \\n1. windows \\n2. Linux \\n3. Mac \\n4. quit\"\n",
    "print(a)'''\n",
    "\n",
    "condition = True\n",
    "while condition:\n",
    "    a = \"Menu: \\n1. windows \\n2. Linux \\n3. Mac \\n4. quit\"\n",
    "    print(a)\n",
    "    user_input = input(\"Select a number from above options : \")\n",
    "    if \"1\" == user_input:\n",
    "        print(\"  ***  You selected Windows  ***  \")\n",
    "        condition = True\n",
    "    elif \"2\" == user_input:\n",
    "        print(\" ***  You selected Linux  ***  \")\n",
    "        condition = True\n",
    "    elif \"3\" == user_input:\n",
    "        print(\"  *** You selected Mac  ***  \")\n",
    "        condition = True\n",
    "    elif \"4\" == user_input:\n",
    "        print(\"  *** Thank You!  ***  \")\n",
    "        condition = False\n",
    "    else:\n",
    "        print(\"===>  Select from given options please  <===\")\n",
    "        condition = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c2bd0838-0a8c-4ec4-8d89-4d3a0de46cb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains numbers :  alkdfj\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not contains numbers \n"
     ]
    }
   ],
   "source": [
    "# 36. take a string from the user and check contains at least one digit or not?\n",
    "user_input = input(\"Enter a string it contains numbers : \" )\n",
    "for i in user_input:\n",
    "    if (i >= \"0\" and i <= \"9\"):\n",
    "        print(\"contains numbers \")\n",
    "        break\n",
    "else:\n",
    "    print(\"not contains numbers \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f1ac733f-9e89-40cd-bfcb-70b49236264b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains alphabets :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Contains Alphabets \n"
     ]
    }
   ],
   "source": [
    "# 37. take a string from the user and check contains at least one alphabets or not?\n",
    "\n",
    "user_input = input(\"Enter a string it contains alphabets : \" )\n",
    "for i in user_input:\n",
    "    if (i >= \"A\" and i <= \"Z\") or (i >= \"a\" and i <= \"z\"):\n",
    "        print(\"Contains Alphabets \")\n",
    "        break\n",
    "else:\n",
    "    print(\"Not contains Alphabets \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8e978301-f982-48d8-9d95-defe0d3ee366",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains Chars :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not contains chars \n"
     ]
    }
   ],
   "source": [
    "# 38. take a string from the user and check contains at least one chars or not?\n",
    "user_input = input(\"Enter a string it contains Chars : \" )\n",
    "for i in user_input:\n",
    "    if not ((i >= \"A\" and i <= \"Z\") or (i >= \"a\" and i <= \"z\") or (i >= \"0\" and i <= \"9\")):\n",
    "        print(\"Contains Chars\")\n",
    "        break\n",
    "else:\n",
    "    print(\"Not contains chars \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "df7de67f-3531-4fee-9c97-5f5a0477f1c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains alphabets :  SAINATH\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Contains capital letters \n"
     ]
    }
   ],
   "source": [
    "# 39. take a string from the user and check contains at least one capital letter or not?\n",
    "\n",
    "user_input = input(\"Enter a string it contains alphabets : \" )\n",
    "for i in user_input:\n",
    "    if (i >= \"A\" and i <= \"Z\"):\n",
    "        print(\"Contains capital letters \")\n",
    "        break\n",
    "else:\n",
    "    print(\"Not contains capital letters \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "dd9d8665-09b8-4b91-86d2-57f6a29559e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string it contains alphabets :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Contains small letters \n"
     ]
    }
   ],
   "source": [
    "# 40. take a string from the user and check contains at least one small letter or not?\n",
    "\n",
    "user_input = input(\"Enter a string it contains alphabets : \" )\n",
    "for i in user_input:\n",
    "    if (i >= \"a\" and i <= \"z\"):\n",
    "        print(\"Contains small letters \")\n",
    "        break\n",
    "else:\n",
    "    print(\"Not contains small letters \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "044e4e96-8b63-4e36-aa78-2dc0e7e662e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163,165,167,169,171,173,175,177,179,181,183,185,187,189,191,193,195,197,199,"
     ]
    }
   ],
   "source": [
    "# 41. Print the first 100 odd numbers\n",
    "\n",
    "for i in range(1, 201):\n",
    "    if i % 2 != 0:\n",
    "        print(i, end=\",\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e9add3af-3f34-4d4c-a606-6cf188e6675d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number :  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 4 5 10 20 25 50 100 "
     ]
    }
   ],
   "source": [
    "# 42. Determine the factors of a number entered  by the user\n",
    "\n",
    "user_input = input(\"enter a number : \")\n",
    "user_input = int(user_input)\n",
    "\n",
    "for i in range(1, user_input+1):\n",
    "    if user_input % i == 0:\n",
    "        print(i, end= \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "2db34020-0458-4673-b842-06e14269d927",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'random' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[43], line 5\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower).\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m# This should continue until and until user gives a correct number or want to quit in the middle.\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;66;03m# Get a hidden number by using random.randint(1,100)\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m number \u001b[38;5;241m=\u001b[39m random\u001b[38;5;241m.\u001b[39mrandint(\u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m100\u001b[39m)\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m# print(number)\u001b[39;00m\n\u001b[0;32m      7\u001b[0m condition \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'random' is not defined"
     ]
    }
   ],
   "source": [
    "# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower).\n",
    "# This should continue until and until user gives a correct number or want to quit in the middle.\n",
    "# Get a hidden number by using random.randint(1,100)\n",
    "\n",
    "number = random.randint(1, 100)\n",
    "# print(number)\n",
    "condition = True\n",
    "while condition:\n",
    "    user_input = input(\"enter a number for guess : \")\n",
    "    user_input = int(user_input)\n",
    "    if number == user_input:\n",
    "        print(\"YES\")\n",
    "        condition = False\n",
    "    elif number > user_input:\n",
    "        print(\"Lower\")\n",
    "        condition = True\n",
    "    else:\n",
    "        print(\"Higher\")\n",
    "        condition = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0ae0d9c7-b565-46dd-ba8a-94196147e472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a  number : 7\n",
      "enter a number :  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      " a is divisible by b \n"
     ]
    }
   ],
   "source": [
    "# 44. Take two numbers from the user a,b check whether a is divisible by b or not?\n",
    "\n",
    "a = input(\"enter a  number :\" )\n",
    "a = int(a)\n",
    "b = input(\"enter a number : \")\n",
    "b = int(a)\n",
    "print(a % b)\n",
    "if a % b == 0:\n",
    "    print(\" a is divisible by b \")\n",
    "else:\n",
    "    print(\" a is not divisible by b \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "d999d48b-c1b1-4b05-b2fe-8934cb5fdfe1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum of multiples of 3 is  166833\n",
      "sum of multiples of 5 is  99500\n"
     ]
    }
   ],
   "source": [
    "# 45. Find the sum of all the multiples of 3 or 5 below 1000\n",
    "\n",
    "sum_of_3 = 0\n",
    "sum_of_5 = 0\n",
    "for i in range(1, 1000):\n",
    "    if i % 3 == 0:\n",
    "        sum_of_3 += i\n",
    "    if i % 5 == 0:\n",
    "        sum_of_5 += i\n",
    "\n",
    "print(\"sum of multiples of 3 is \", sum_of_3)\n",
    "print(\"sum of multiples of 5 is \", sum_of_5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b9efddcd-d8f5-47ac-9833-47a4e84b8d7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number : 55\n",
      "Enter a number : 68\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Big number is  68\n"
     ]
    }
   ],
   "source": [
    "# 46. Write a program to find out big of two numbers\n",
    "user_input = input(\"Enter a number :\")\n",
    "user_input_2 = input(\"Enter a number :\")\n",
    "user_input = float(user_input)\n",
    "user_input_2 = float(user_input_2)\n",
    "\n",
    "if user_input > user_input_2 :\n",
    "    print(\"Big number is \", int(user_input))\n",
    "else:\n",
    "    print(\"Big number is \", int(user_input_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "cab951ff-5b11-4104-9c36-d51b6ff261c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a Number : 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "# 47. Write a program to find out biggest number in the given numbers.\n",
    "user_input = input(\"Enter a Number :\")\n",
    "user_input = list(user_input)\n",
    "big = int(user_input[0])\n",
    "for i in user_input:\n",
    "    if int(i) >= big:\n",
    "        big = int(i)\n",
    "print(big)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "16961630-2d69-4a18-be2d-eab421af4bce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a String  sainath\n",
      "Enter a sub string sai\n"
     ]
    }
   ],
   "source": [
    "# 48. find out the index of third occurrence of given substring\n",
    "user_input = input(\"Enter a String \")\n",
    "user_input_2 = input(\"Enter a sub string\")\n",
    "count = 0\n",
    "length = 0\n",
    "list_words = user_input.split(\" \")\n",
    "for i in range(0, len(list_words)):\n",
    "    if list_words[i] == user_input_2:\n",
    "        count += 1\n",
    "        if count == 3:\n",
    "            break\n",
    "        length += len(list_words[i])\n",
    "    else:\n",
    "        length += len(list_words[i])\n",
    "user_input = \" \".join(list_words)\n",
    "if count == 3:\n",
    "    print(length+count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "c995b50f-0035-45c8-b433-869383b67798",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a String  sainath\n",
      "Enter a sub string ll\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "# 49. find out the index nth occurrence of given substring\n",
    "\n",
    "user_input = input(\"Enter a String \")\n",
    "user_input_2 = input(\"Enter a sub string\")\n",
    "count = 0\n",
    "length = 0\n",
    "list_words = user_input.split(\" \")\n",
    "for i in range(0, len(list_words)):\n",
    "    if list_words[i] == user_input_2:\n",
    "        count += 1\n",
    "        length += len(list_words[i])\n",
    "    else:\n",
    "        length += len(list_words[i])\n",
    "user_input = \" \".join(list_words)\n",
    "\n",
    "print(length+count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "ee054aa5-442b-45c6-a1db-c57a4e2b2912",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number for no of inputs :  2\n",
      " enter a number  45\n",
      " enter a number  45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mimimunm of a given numbers  45\n",
      "Maximum of a given numbers  45\n",
      "sum of given numbers  90\n",
      "Average of given numbers 45.0\n"
     ]
    }
   ],
   "source": [
    "# 50. Take some single digit numbers from the user and findout min, maximum, sum, average\n",
    "\n",
    "n = input(\"enter a number for no of inputs : \")\n",
    "n = int(n)\n",
    "list_a = []\n",
    "for i in range(n):\n",
    "    user_input = input(\" enter a number \")\n",
    "    list_a.append(int(user_input))\n",
    "min_of = list_a[0]\n",
    "max_of = list_a[0]\n",
    "sum_of = 0\n",
    "for i in list_a:\n",
    "    sum_of += i\n",
    "    if min_of >= i:\n",
    "        min_of = i\n",
    "    if max_of  <= i:\n",
    "        max_of = i\n",
    "print(\"mimimunm of a given numbers \", min_of)\n",
    "print(\"Maximum of a given numbers \", max_of)\n",
    "print(\"sum of given numbers \", sum_of)\n",
    "print(\"Average of given numbers\", (sum_of / n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "e71a86f1-7876-455f-9dcb-232e520dd413",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number  55\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "000055\n"
     ]
    }
   ],
   "source": [
    "# 51. print the number in proper mathematical way.\n",
    "# \tConsider that we have 6 digit numbers.\n",
    "# Number format  WAP> 10 -> 000010\n",
    "# \t\t100 ->  000100\n",
    "# \t\t1000 ->  001000\n",
    "# \t\t 2345678  ->  2345678\n",
    "# \tIf the number has morethan 6 digits then print as it is.\n",
    "\n",
    "user_input = input(\"enter a number \")\n",
    "length = len(user_input)\n",
    "if length < 7:\n",
    "    print(\"0\" * (6- length) + user_input) #  or  #  print(user_input.zfill(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "993fa7d7-4eb4-420b-b0ed-44bcfae93f18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter emp name  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp1 sainath\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter emp name  devops\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp2 devops\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter emp name  sai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp3 sai\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter emp name  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "emp4 sainath\n"
     ]
    }
   ],
   "source": [
    "# 52. names =\"emp1,emp2,emp3,emp4\" iterate through the employee names.\n",
    "\n",
    "names =\"emp1,emp2,emp3,emp4\"\n",
    "for i in names.split(\",\"):\n",
    "    print(i, input(\"enter emp name \" ))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "85fdf46f-3fdd-4ee8-8c33-5b56ce2cfe9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a sentence  sainath is a good boy\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sainath', 'is', 'a', 'good', 'boy']\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a sub string sainath\n",
      "enter a occurances of numbers  5\n",
      "enter a string to change 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sainath\n",
      "is\n",
      "a\n",
      "good\n",
      "boy\n",
      "5 is a good boy\n"
     ]
    }
   ],
   "source": [
    "# 53. Take actual string, source string, destination string.\n",
    "# replce first nth occurrences of source string with destination string of actual string.\n",
    "\n",
    "user_input = input(\"Enter a sentence \")\n",
    "list_a = user_input.split()\n",
    "print(list_a)\n",
    "source = input(\"enter a sub string\")\n",
    "n = input(\"enter a occurances of numbers \")\n",
    "n = int(n)\n",
    "destination = input(\"enter a string to change\")\n",
    "count = 0\n",
    "for i in range(0, len(list_a)):\n",
    "    print(list_a[i])\n",
    "    if list_a[i] == source :\n",
    "        list_a[i] = destination\n",
    "        count += 1\n",
    "        if count == n:\n",
    "            break\n",
    "print(\" \".join(list_a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f42116db-dd6d-4514-991f-5911e75fbd2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number : 55\n",
      "enter a number : 46\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. addition \n",
      "2. multiples \n",
      "3.division \n",
      "4.sqrt \n",
      "5. pow a**b \n",
      "6.subtraction\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select from above options :  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pow a**b  of : 1.1394196811467816e+80\n"
     ]
    }
   ],
   "source": [
    "# 54. Take a two numbers from the user and do below menu driven operations\n",
    "# 1. addition\n",
    "# 2. multiples\n",
    "# 3.division\n",
    "# 4.sqrt\n",
    "# 5. pow    a**b\n",
    "# 6.subtraction\n",
    "# After selection do the corresponding operation.\n",
    "# Note: user may give int, or float numbers. You should check whether it is proper digits or not. \n",
    "# I.e the user given string should be in the position to convert to float. \n",
    "# Other wise show the “inproper string given” Error.\n",
    "\n",
    "user_input = input(\"enter a number :\")\n",
    "user_input = float(user_input)\n",
    "user_input_1 = input(\"enter a number :\")\n",
    "user_input_1 = float(user_input_1)\n",
    "\n",
    "print(\"1. addition \\n2. multiples \\n3.division \\n4.sqrt \\n5. pow a**b \\n6.subtraction\")\n",
    "select = input(\"select from above options : \")\n",
    "if select == \"1\":\n",
    "    print(\"addition of :\", user_input + user_input_1)\n",
    "elif select == \"2\":\n",
    "    print(\"multiples  of :\", user_input * user_input_1)\n",
    "elif select == \"3\":\n",
    "    print(\"division   of :\", user_input / user_input_1)\n",
    "elif select == \"4\":\n",
    "    print(\"sqrt of :\", user_input **2,  user_input_1**2 )\n",
    "elif select == \"5\":\n",
    "    print(\"pow a**b  of :\", user_input ** user_input_1 )\n",
    "elif select == \"6\":\n",
    "    print(\"subtraction  of :\", user_input - user_input_1)\n",
    "else:\n",
    "    print(\"selected inproper option\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "8baa76f7-0947-40ec-ae4d-2776dbae2cba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number for no of inputs :  5\n",
      " enter a number  6\n",
      " enter a number  9\n",
      " enter a number  8\n",
      " enter a number  7\n",
      " enter a number  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mimimunm of a given numbers  6\n",
      "Maximum of a given numbers  9\n",
      "sum of given numbers  37\n",
      "Average of given numbers 7.4\n"
     ]
    }
   ],
   "source": [
    "# 55. Take numbers from the user and find out min, maximum, sum, average\n",
    "\n",
    "n = input(\"enter a number for no of inputs : \")\n",
    "n = int(n)\n",
    "list_a = []\n",
    "for i in range(n):\n",
    "    user_input = input(\" enter a number \")\n",
    "    list_a.append(int(user_input))\n",
    "min_of = list_a[0]\n",
    "max_of = list_a[0]\n",
    "sum_of = 0\n",
    "for i in list_a:\n",
    "    sum_of += i\n",
    "    if min_of >= i:\n",
    "        min_of = i\n",
    "    if max_of  <= i:\n",
    "        max_of = i\n",
    "print(\"mimimunm of a given numbers \", min_of)\n",
    "print(\"Maximum of a given numbers \", max_of)\n",
    "print(\"sum of given numbers \", sum_of)\n",
    "print(\"Average of given numbers\", (sum_of / n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "7e5bd3b7-6554-43fc-8ebd-aee48b8ccdef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even numbers: 11\n",
      "Odd numbers: 11\n",
      "Positive numbers: 22\n",
      "Negative numbers: 0\n",
      "Prime numbers: 7\n",
      "Perfect numbers: 0\n",
      "Armstrong numbers: 8\n",
      "Palindrome numbers: 11\n"
     ]
    }
   ],
   "source": [
    "# 56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] \n",
    "# find out how many even numbers are there and how many odd numbers are there and \n",
    "# how many positive numbers are there and how many negative numbers are there and \n",
    "# how many prime numbers are there and how many perfect numbers are there and \n",
    "# how many Armstrong numbers are there and how many palindrome numbers are there.\n",
    "ve_no = 0\n",
    "ne_no = 0\n",
    "even_no = 0\n",
    "odd_no = 0\n",
    "prime_no = 0\n",
    "perfect_no = 0\n",
    "armstrong_no = 0\n",
    "palindrome_no = 0\n",
    "\n",
    "l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]\n",
    "for i in l:\n",
    "    if i >=0:\n",
    "        ve_no += 1\n",
    "    else:\n",
    "        ne_no += 1\n",
    "    if i % 2 == 0:\n",
    "        even_no += 1\n",
    "    else:\n",
    "        odd_no += 1\n",
    "    if i <= 1:\n",
    "        prime_no += 0\n",
    "    else:\n",
    "        count = 0\n",
    "        for j in range(2, i+1):\n",
    "            if i % j == 0:\n",
    "                count += 1\n",
    "        if count == 1:\n",
    "            prime_no += 1\n",
    "    if i <= 1:\n",
    "        perfect_no += 0\n",
    "    else:\n",
    "        sum = 1\n",
    "        for j in range(2, i+1):\n",
    "            if i % j == 0:\n",
    "                sum += j\n",
    "                if i // j != j:\n",
    "                    sum += i // j\n",
    "        if sum == i:\n",
    "            perfect_no += 1\n",
    "    num_str = str(i)\n",
    "    num_digits = len(num_str)\n",
    "    sum_of_powers = 0\n",
    "    \n",
    "    for j in num_str:\n",
    "        sum_of_powers += (int(j) ** num_digits)\n",
    "\n",
    "    if sum_of_powers == i:\n",
    "        armstrong_no += 1\n",
    "    if str(i) == str(i)[::-1]:\n",
    "        palindrome_no += 1\n",
    "\n",
    "print(\"Even numbers:\", even_no)\n",
    "print(\"Odd numbers:\", odd_no)\n",
    "print(\"Positive numbers:\", ve_no)\n",
    "print(\"Negative numbers:\", ne_no)\n",
    "print(\"Prime numbers:\", prime_no)\n",
    "print(\"Perfect numbers:\", perfect_no)\n",
    "print(\"Armstrong numbers:\", armstrong_no)\n",
    "print(\"Palindrome numbers:\", palindrome_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "f674cf27-1614-4e93-ac9d-ccba38016859",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digits: 0\n",
      "Special symbols: 7\n",
      "Small letters: 7\n",
      "Capital letters: 0\n"
     ]
    }
   ],
   "source": [
    "# 57. Take a string from the user and find out how many digits are there, \n",
    "# how many special symbols are there, how many small letters are there, how many caps are there.\n",
    "\n",
    "user_input = input(\"Enter a string : \")\n",
    "digit_count = 0\n",
    "symbol_count = 0\n",
    "small_letter = 0\n",
    "captial_count = 0\n",
    "for i in user_input:\n",
    "    if (i >= \"a\" and i <= \"z\"):\n",
    "        small_letter += 1\n",
    "    if (i >= \"A\" and i <= \"Z\"):\n",
    "        captial_count += 1\n",
    "    if (i >= \"0\" and i <= \"9\"):\n",
    "        digit_count += 1\n",
    "    else:\n",
    "        symbol_count += 1\n",
    "print(\"Digits:\", digit_count)\n",
    "print(\"Special symbols:\", symbol_count)\n",
    "print(\"Small letters:\", small_letter)\n",
    "print(\"Capital letters:\", captial_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "482fa148-c9f7-4064-b49d-b96412d3705d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string : sainath\n",
      "Enter a char : sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of occurances are :  0\n"
     ]
    }
   ],
   "source": [
    "# 58. Take a char from the user and find out how many number of occurrences are there in given string\n",
    "\n",
    "user_input = input(\"Enter a string :\")\n",
    "user_input_1 = input(\"Enter a char :\")\n",
    "count = 0\n",
    "for i in user_input:\n",
    "    if i == user_input_1:\n",
    "        count += 1\n",
    "\n",
    "print(\"no of occurances are : \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "c4cb9b0f-a778-4eae-8270-6ea96b0227af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number : 44\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of  occurances are  0\n"
     ]
    }
   ],
   "source": [
    "# 59. Take a element from the user and find out how many times the  element occurred in given list\n",
    "\n",
    "list_a = [1,2,3,4,5,2,5,2,6,1,2,5,2,1,5,4,3,8,9,2]\n",
    "user_input = input(\"Enter a number :\")\n",
    "user_input = int(user_input)\n",
    "count = 0\n",
    "for i in list_a:\n",
    "    if i == user_input:\n",
    "        count += 1\n",
    "print(\"no of  occurances are \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "92c57aa4-ae3c-49f7-99e3-b4c6a96847bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number : 55\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no of  occurances are  0\n"
     ]
    }
   ],
   "source": [
    "# 60. Take an element from the user and find out how many number of occurrences are there in given tuple\n",
    "\n",
    "list_a = (1,2,3,4,5,2,5,2,6,1,2,5,2,1,5,4,3,8,9,2)\n",
    "user_input = input(\"Enter a number :\")\n",
    "user_input = int(user_input)\n",
    "count = 0\n",
    "for i in list_a:\n",
    "    if i == user_input:\n",
    "        count += 1\n",
    "print(\"no of  occurances are \", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "32e2a921-6597-4b15-98e1-8e9a5a9c68be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abc123,#$45def6%$^789$%^\n",
      "$%^987%$^6fed54,#$321cba\n",
      "$%^987%$^6fed54,#$321cba required output\n"
     ]
    }
   ],
   "source": [
    "# 61. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.\n",
    "#     Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba\n",
    "#     Input:abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^\n",
    "# \tInout: \"123,#$456%$^789$%^\", Output: 321,#$654%$^987$%^   Only numbers has to reverse.\n",
    "\n",
    "\n",
    "s = \"abc123,#$45def6%$^789$%^\"\n",
    "print(s)\n",
    "string_reverse = s[::-1]\n",
    "\n",
    "res = \"\"\n",
    "sub = \"\"\n",
    "for i in string_reverse:\n",
    "    if i.isalnum():\n",
    "        res += sub + i\n",
    "        sub = \"\"\n",
    "    else:\n",
    "        sub = i + sub\n",
    "    \n",
    "\n",
    "print(res)\n",
    "\n",
    "print(\"$%^987%$^6fed54,#$321cba\", \"required output\" ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "73b81d2d-2036-4ef6-a793-fa61972720db",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 62. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.\n",
    "#     Input:abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^\n",
    "\n",
    "s      = \"abc123,#$45def6%$^789$%^\"\n",
    "output = \"9876fe,#$d54321%$^cba$%^\"\n",
    "\n",
    "# Input:, output: 9876fe,#$d54321%$^cba$%^"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "496d74d5-6d94-45e6-8db2-95397a7337aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter The Name of the Person :  asinath\n",
      "Enter an Age  of the Person :  27\n",
      "Enter height  of the Person :  5.6\n",
      "Enter weight  of the Person :  80\n",
      "Enter aadhar no.of the Person :  1023\n",
      "Enter Mobile no.of the Person :  9100588742\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name of the Person asinath\n",
      "Age of the Person 27\n",
      "Weight of the Person :  80\n"
     ]
    }
   ],
   "source": [
    "# 65. define a function to take person details name and age are mandatory parameters \n",
    "# and height weight are optional parameters. If the user willing to pass any other details(like adhar, cell, pan, passport etc..) \n",
    "#     regarding him then your function should access those details.\n",
    "def person_details(name, age, height = None, weight = None, **kwargs):\n",
    "    print(f\"Name of the Person {name}\")\n",
    "    print(f\"Age of the Person {age}\")\n",
    "    if height:\n",
    "        print(f\"Height of the Person :  {height}\")\n",
    "    if weight:\n",
    "        print(f\"Weight of the Person :  {weight}\")\n",
    "    if kwargs:\n",
    "        for key, value in kwargs:\n",
    "            print(f\"{key} : {value}\")\n",
    "\n",
    "name = input(\"Enter The Name of the Person : \")\n",
    "age = input(\"Enter an Age  of the Person : \")\n",
    "height =  input(\"Enter height  of the Person : \")\n",
    "weight =  input(\"Enter weight  of the Person : \")\n",
    "aadhar =  input(\"Enter aadhar no.of the Person : \")\n",
    "mobile_no =  input(\"Enter Mobile no.of the Person : \")\n",
    "\n",
    "person_details(name, age, weight= weight)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ba4208d-28a1-47cd-b101-d729d840592a",
   "metadata": {},
   "source": [
    "l=[1,2,3,4]\n",
    "k=l.append(5)\n",
    "print(\"l=\", l)\n",
    "print(\"k=\", k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "abfb1059-874c-48ac-9afe-a4d18c0d2a6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "l=[1,2,3,4]\n",
    "k= l.append(5)\n",
    "print(k)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2a184ee-63c5-4092-9e97-1f6df8c9634e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcd\n",
      "Abcd\n"
     ]
    }
   ],
   "source": [
    "s =\"abcd\"\n",
    "s1=s.replace(\"a\", \"A\")\n",
    "print(s)\n",
    "print(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f1419380-3bc2-4a26-a9a4-4dcdc4e80e97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, [1, 2], [3, 4], [5, 6]]\n"
     ]
    }
   ],
   "source": [
    "l=[1,2,3,4]\n",
    "l.extend([[1,2],[3,4],[5,6]])\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c96fa913-4c2f-4eaf-a9c8-aeec878c432e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 40, 10, 20, 30]\n"
     ]
    }
   ],
   "source": [
    "l=[1,2,3,4]\n",
    "l.extend({10,20,30,40})\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "51d63a17-2e79-4ab6-84de-9e9d778d03bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 'd', 'E']\n"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "l.insert(30, \"E\")\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "af0a0bbd-cb40-4835-b751-b3defa304ca7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['E', 'a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "l.insert(-30, \"E\")\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5d7af74d-ab32-413e-a036-d9f774df679d",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "pop index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[16], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m l\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124md\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m----> 2\u001b[0m l\u001b[38;5;241m.\u001b[39mpop(\u001b[38;5;241m30\u001b[39m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mk=\u001b[39m\u001b[38;5;124m\"\u001b[39m,k)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ml=\u001b[39m\u001b[38;5;124m\"\u001b[39m,l)\n",
      "\u001b[1;31mIndexError\u001b[0m: pop index out of range"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "l.pop(30)\n",
    "print(\"k=\",k)\n",
    "print(\"l=\",l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "07a4b645-cbeb-4c5a-bb2c-63b78ab3d9ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k= c\n",
      "l= ['a', 'b', 'd']\n"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "k=l.pop(-2)\n",
    "print(\"k=\",k)\n",
    "print(\"l=\",l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "384c07ce-945c-4112-abe6-32a2db05f41a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k= None\n",
      "l= ['a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "k=l.sort()\n",
    "print(\"k=\",k)\n",
    "print(\"l=\",l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9ae9d8b4-1e94-4c65-9ee8-3a10f66173e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k= None\n",
      "l= ['a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "l=[\"a\",\"b\",\"c\",\"d\"]\n",
    "k=l.sort()\n",
    "print(\"k=\",k)\n",
    "print(\"l=\",l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d32e1610-1957-406a-829b-b37f46135cdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ABC', 'abc', 'def', 'ghi']\n"
     ]
    }
   ],
   "source": [
    "l=[\"abc\",\"ABC\",\"def\",\"ghi\"]\n",
    "l.sort()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "46fce58e-b0c8-4aa7-a0e3-3e1adf5c111a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ABC', 'GHI', 'abc', 'def', 'ghi']\n"
     ]
    }
   ],
   "source": [
    "l=[\"abc\",\"ABC\",\"def\",\"ghi\",\"GHI\"]\n",
    "l.sort()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "024efb75-29be-4e09-909b-4ca9fb7a6b8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even\n"
     ]
    }
   ],
   "source": [
    "# 65a. rewrite above assignments by functions. Can use string functions to solve the string related assignments\n",
    "# 65 b. write a function to check given value is even or not\n",
    "number=10\n",
    "if number %2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d9c658ff-0ce7-4e9c-a90d-c254d824b5c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17 is a prime number.\n"
     ]
    }
   ],
   "source": [
    "# 65 c. write a function to check given value is prime or not\n",
    "\n",
    "number = 17\n",
    "if (number):\n",
    "  print(f\"{number} is a prime number.\")\n",
    "else:\n",
    "  print(f\"{number} is not a prime number.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bf8bc1e2-d16e-4540-9113-8fd48dcf5fa9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "its divisble\n"
     ]
    }
   ],
   "source": [
    "number1=10\n",
    "number=15\n",
    "if (number1, number):\n",
    "    print(f\"its divisble\")\n",
    "else:\n",
    "    print(f\"its not divisible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "df273a53-ba17-4802-b8e2-efed6118e6a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value: s\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "its not a digit\n"
     ]
    }
   ],
   "source": [
    "# 67. take a string from the user and check contains only digits or not?\n",
    "user_input = input(\"enter a value:\")\n",
    "\n",
    "if user_input.isdigit():\n",
    "    print(f\"its a digit\")\n",
    "else:\n",
    "    print(f\"its not a digit\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "3b3aca05-f31f-4b06-804d-ca8e5f72c7cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value: 12sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The given value is not alphabet\n"
     ]
    }
   ],
   "source": [
    "# 68. take a string from the user and check contains only alphabets or not?\n",
    "user_input = input(\"enter a value:\")\n",
    "if user_input.isalpha():\n",
    "    print(f\"The given value is alphabet\")\n",
    "else:\n",
    "    print(f\"The given value is not alphabet\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "a5be9fd8-8a88-466a-ae10-7ee6fa0abcb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value: 654654\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this are not characters\n"
     ]
    }
   ],
   "source": [
    "# 69. take a string from the user and check contains only special chars or not?\n",
    "user_input = input(\"enter a value:\")\n",
    "if user_input.isalpha():\n",
    "    print(\"this contains characters\")\n",
    "else:\n",
    "    print(\"this are not characters\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "1ea951c8-9483-4787-b800-e53dc4f257c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value: SAINATH\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This contains capital letters\n"
     ]
    }
   ],
   "source": [
    "# 70. take a string from the user and check contains only capital letters or not?\n",
    "user_input = input(\"enter a value:\")\n",
    "if user_input.isupper():\n",
    "    print(f\"This contains capital letters\")\n",
    "else:\n",
    "    print(\"This does not contain capital letters\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "33348129-0eb2-480f-971a-cc1651f53585",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a value: sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This contains lower letters\n"
     ]
    }
   ],
   "source": [
    "# 71. take a string from the user and check contains only small letters or not?\n",
    "user_input = input(\"enter a value:\")\n",
    "if user_input.islower():\n",
    "    print(f\"This contains lower letters\")\n",
    "else:\n",
    "    print(\"This are capital letters\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "8264ccf8-e447-4065-8f66-cb1638f9a911",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 72. WAP to replace last n occurrence.\n",
    "user_input = \"abcdabcdabcdabcd\"\n",
    "#no_of occurrence= 2\n",
    "source_string = \"a\"\n",
    "destination_string= \"A\"\n",
    "sample_output= \"abcdabcdAbcdAbcd\"\n",
    "\n",
    "string = ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "80802949-282c-4d53-9c5a-15ecaae3b244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dcbAdcbAdcbAdcbAdcbAdcbAdcbAdcbA\n"
     ]
    }
   ],
   "source": [
    "for i in user_input[::-1]:\n",
    "    if source_string == i:\n",
    "        i= destination_string\n",
    "        string= string+i\n",
    "    else :\n",
    "       string= string+i\n",
    "print(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "e4972699-5d53-462c-a41f-e94e6191ee17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcdabcdAbcdAbcd\n"
     ]
    }
   ],
   "source": [
    "user_input = \"abcdabcdabcdabcd\"\n",
    "# reverse_string= user_input[::-1]\n",
    "# reverse_string\n",
    "count=0\n",
    "string= \"\"\n",
    "no_of_occurrence= 2\n",
    "source_string = \"a\"\n",
    "destination_string= \"A\"\n",
    "for char in user_input[::-1]:\n",
    "    if char == source_string:\n",
    "        if count < no_of_occurrence:\n",
    "            count += 1\n",
    "            string= string+ destination_string\n",
    "        else:\n",
    "            string += char\n",
    "    else:\n",
    "        string= string+char\n",
    "# sample_output= \"abcdabcdAbcdAbcd\"\n",
    "print(string[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8467a46e-5e57-40f3-98b9-ed5b428f308e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 73. WAP to check given string contains numbers or not. it should consider float numbers also"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "66616992-4d4b-4253-a108-5ecfad9981e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a word with alphabets:  SAINATH\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SAINATH\n",
      "sainath\n"
     ]
    }
   ],
   "source": [
    "# 74. Convert the total string in to lower case. # Convert the total string in to upper case.\n",
    "def convert_to_uppercase(input_string):\n",
    "\n",
    "    return input_string.upper()\n",
    "\n",
    "def convert_to_lowercase(input_string):\n",
    "   \n",
    "    return input_string.lower()\n",
    "\n",
    "user_input = input(\"Enter a word with alphabets: \")\n",
    "\n",
    "uppercase_string = convert_to_uppercase(user_input)\n",
    "print(uppercase_string)\n",
    "\n",
    "lowercase_string = convert_to_lowercase(user_input)\n",
    "print(lowercase_string)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "f82ce772-3993-4505-9590-55152478d39a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string :  my name is sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My Name Is Sainath\n"
     ]
    }
   ],
   "source": [
    "75# Convert every word start letter into caps. Some how title not working if it contains numbers and special symbols in the word\n",
    "def capitalize_words(text):\n",
    "  words = text.split()\n",
    "  capitalized_words = []\n",
    "  for word in words:\n",
    "    if word:\n",
    "      capitalized_words.append(word.capitalize())\n",
    "    else:\n",
    "      capitalized_words.append(word)\n",
    "  return \" \".join(capitalized_words)\n",
    "\n",
    "text = input(\"Enter a string : \")     # \"hello world 123! special_symbol\"\n",
    "capitalized_text = capitalize_words(text)\n",
    "print(capitalized_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "2c8857e5-eea7-4151-ada0-3109b04790ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def capitalize_words(text):\n",
    "    words = text.split()\n",
    "    capitalize_words = []\n",
    "    for word in words:\n",
    "        if word:\n",
    "            capitalize_words.append().word.capitalize()\n",
    "        else:\n",
    "            capitalized_word.append(word)\n",
    "        return \" \".join(capitalized_words)\n",
    "    text= input(\"Enter a string : \")\n",
    "    capitalized_text = capitalize_words(text)\n",
    "    print(capitalized_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "fc4e910f-1baa-48e8-ac06-575a53f757d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string :  sainath\n",
      "Enter a word :  is from devops\n",
      "Enter a word :  in aja\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "empty separator",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[209], line 19\u001b[0m\n\u001b[0;32m     17\u001b[0m source \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a word : \u001b[39m\u001b[38;5;124m\"\u001b[39m) \n\u001b[0;32m     18\u001b[0m destination \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a word : \u001b[39m\u001b[38;5;124m\"\u001b[39m) \n\u001b[1;32m---> 19\u001b[0m new_text \u001b[38;5;241m=\u001b[39m replace_last_two_occurrences(text, source, destination)\n",
      "Cell \u001b[1;32mIn[209], line 4\u001b[0m, in \u001b[0;36mreplace_last_two_occurrences\u001b[1;34m(text, source_string, destination_string, delimiter)\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mreplace_last_two_occurrences\u001b[39m(text, source_string, destination_string, delimiter\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m):\n\u001b[1;32m----> 4\u001b[0m     words\u001b[38;5;241m=\u001b[39m text\u001b[38;5;241m.\u001b[39msplit(delimiter)\n\u001b[0;32m      5\u001b[0m     count\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m\n\u001b[0;32m      6\u001b[0m     new_words\u001b[38;5;241m=\u001b[39m[]\n",
      "\u001b[1;31mValueError\u001b[0m: empty separator"
     ]
    }
   ],
   "source": [
    "#   76.replace last two occurrences of given source string with destination string\n",
    "# #  preserve the delimiter after split.\n",
    "def replace_last_two_occurrences(text, source_string, destination_string, delimiter=''):\n",
    "    words= text.split(delimiter)\n",
    "    count= 0\n",
    "    new_words=[]\n",
    "    for i in range(len(words) -1,-1,-1):\n",
    "        if words[i] == source and count < 2:\n",
    "            new_words.insert(0, destination)\n",
    "            count= +1\n",
    "        else:\n",
    "            new_words.insert(0, words[i])\n",
    "        return delimiter.join(new_words)\n",
    "\n",
    "\n",
    "text = input(\"Enter a string : \") \n",
    "source = input(\"Enter a word : \") \n",
    "destination = input(\"Enter a word : \") \n",
    "new_text = replace_last_two_occurrences(text, source, destination)\n",
    "# print(new_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "24205f91-5c3e-4bed-afe1-ae1e368469cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string :  sainath\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The substring 'sainath' is not present in the string.\n"
     ]
    }
   ],
   "source": [
    "# 77. write a program to check given substring is there in actual string or not? (search should be case insensitive)\n",
    "# example: act=\"python is a pure object oriented programing language\"\n",
    "\n",
    "\n",
    "def contains_substring_case_insensitive(actual_string, substring):\n",
    "    if substring.casefold() in actual_string.casefold():\n",
    "        print(f\"The substring '{substring_to_check}' is present in the string.\")\n",
    "    else:\n",
    "        print(f\"The substring '{substring_to_check}' is not present in the string.\")\n",
    "\n",
    "act = \"python is a pure object oriented programing language\"\n",
    "substring_to_check = input(\"Enter a string : \")\n",
    "contains_substring_case_insensitive(act, substring_to_check)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "2ff3971d-6640-43c2-8a90-96b267f781be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The substring 'pure' is present in the string.\n"
     ]
    }
   ],
   "source": [
    "# 78.check whether “pure” is there in act or not.\n",
    "# Note: Use in operator\n",
    "\n",
    "def contains_substring_case_insensitive(actual_string, substring):\n",
    "    if substring.casefold() in actual_string.casefold():\n",
    "        print(f\"The substring '{substring_to_check}' is present in the string.\")\n",
    "    else:\n",
    "        print(f\"The substring '{substring_to_check}' is not present in the string.\")\n",
    "\n",
    "act = \"python is a pure object oriented programing language\"\n",
    "substring_to_check = \"pure\"\n",
    "contains_substring_case_insensitive(act, substring_to_check)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "191423ba-f83b-46c0-b508-ad1cb61829c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "DATA STRUCTURES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "29dd643d-dbbe-42c3-9f76-6d44709463c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10]\n"
     ]
    }
   ],
   "source": [
    "# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list\n",
    "\n",
    "\n",
    "def dimensional_list(lst):\n",
    "  flat_lst = []\n",
    "  for item in lst:\n",
    "    if type(item) == list :\n",
    "      flat_lst.extend(flatten_list(item))\n",
    "    else:\n",
    "        flat_lst.append(item)\n",
    "    return flat_lst\n",
    "\n",
    "l= [10, 20, 30, [40, 50, 60], 70, [80, 90, 20]]\n",
    "flat_l = dimensional_list(l)\n",
    "print(flat_l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "1d66c7b0-2655-479f-b71b-23dccc3089f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'G': 1, 'o': 2, 'g': 1, 'l': 1, 'e': 1}\n"
     ]
    }
   ],
   "source": [
    "# 80. input: \"Google\" print count of each character\n",
    "\n",
    "def char_count(input_string):\n",
    "  char_counts = {}\n",
    "  for char in input_string:\n",
    "    if char in char_counts:\n",
    "      char_counts[char] += 1\n",
    "    else:\n",
    "      char_counts[char] = 1\n",
    "  return char_counts\n",
    "\n",
    "input_string = \"Google\"\n",
    "char_counts = char_count(input_string)\n",
    "print(char_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d5e3798-8ff3-49ee-b15c-2ac901d7cc6f",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
