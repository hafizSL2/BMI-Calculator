{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font size=\"+3\">Module 48 - BMI App</font>\n",
    "\n",
    "## Context: Understanding the Problem Statement --------Problem Scoping\n",
    "\n",
    "#### BMI Calculator\n",
    "\n",
    "Body Mass Index (BMI) is generally used to broadly categorize a person as underweight, normal weight, overweight, or obese based on their height and weight.\n",
    "For calculating the BMI, we need to know the Weight (in Kg) and Height (in metre) ."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Import the Streamlit Library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Give title to the application and ask user for entering height and weight for calculating BMI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-09-19 22:36:05.727 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run d:\\my internships\\sustainable living labs\\openvino_env\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# give a title to our app\n",
    "st.title('Welcome to BMI Calculator')\n",
    " \n",
    "# TAKE WEIGHT INPUT in kgs\n",
    "weight = st.number_input(\"Enter your weight (in kgs)\")\n",
    " \n",
    "# TAKE HEIGHT INPUT\n",
    "# radio button to choose height format\n",
    "status = st.radio('Select your height format: ',\n",
    "                  ('cms', 'meters', 'feet'))\n",
    " \n",
    "# compare status value\n",
    "if(status == 'cms'):\n",
    "    # take height input in centimeters\n",
    "    height = st.number_input('Enter your height in Centimeters')\n",
    "     \n",
    "    try:\n",
    "        bmi = weight / ((height/100)**2)\n",
    "    except:\n",
    "        st.text(\"Enter some value of height\")\n",
    "         \n",
    "elif(status == 'meters'):\n",
    "    # take height input in meters\n",
    "    height = st.number_input('Enter your height in Meters')\n",
    "     \n",
    "    try:\n",
    "        bmi = weight / (height ** 2)\n",
    "    except:\n",
    "        st.text(\"Enter some value of height\")\n",
    "         \n",
    "else:\n",
    "    # take height input in feet\n",
    "    height = st.number_input('Enter your height in Feet')\n",
    "     \n",
    "    # 1 meter = 3.28\n",
    "    try:\n",
    "        bmi = weight / (((height/3.28))**2)\n",
    "    except:\n",
    "        st.text(\"Enter some value of height\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Classify the BMI index of the person based on the WHO chart"
   ]
  },
  {
   "attachments": {
    "who_chart.jpg": {
     "image/jpeg": "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"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![who_chart.jpg](attachment:who_chart.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# check if the button is pressed or not\n",
    "if(st.button('Calculate BMI')):\n",
    "     \n",
    "    # print the BMI INDEX\n",
    "    st.text(\"Your BMI Index is {}.\".format(bmi))\n",
    "     \n",
    "    # give the interpretation of BMI index\n",
    "    if(bmi < 16):\n",
    "        st.error(\"You are Extremely Underweight\")\n",
    "    elif(bmi >= 16 and bmi < 18.5):\n",
    "        st.warning(\"You are Underweight\")\n",
    "    elif(bmi >= 18.5 and bmi < 25):\n",
    "        st.success(\"Healthy\")       \n",
    "    elif(bmi >= 25 and bmi < 30):\n",
    "        st.warning(\"Overweight\")\n",
    "    elif(bmi >= 30):\n",
    "        st.error(\"Extremely Overweight\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": false,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
