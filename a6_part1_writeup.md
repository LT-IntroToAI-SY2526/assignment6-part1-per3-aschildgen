# Assignment 6 Part 1 - Writeup

**Name:** _______________  
**Date:** _______________

---

## Part 1: Understanding Your Model

### Question 1: R² Score Interpretation
What does the R² score tell you about your model? What does it mean if R² is close to 1? What if it's close to 0?
The R² score tells us how much of the variation in the test scores can be explained by the number of hours studied. If R² is close to 1, the model explains almost all the variation → very accurate. If R² is close to 0, the model explains almost none of the variation → very weak model.

**YOUR ANSWER:**
The R² score tells us how much of the variation in the test scores can be explained by the number of hours studied. If R² is close to 1, the model explains almost all the variation → very accurate. If R² is close to 0, the model explains almost none of the variation → very weak model.


---

### Question 2: Mean Squared Error (MSE)
What does the MSE (Mean Squared Error) mean in plain English? Why do you think we square the errors instead of just taking the average of the errors?
MSE represents how far off the model’s predictions are from the real scores, on average. Squaring the errors makes large mistakes count more, and it also prevents negative errors from canceling out positive ones.

**YOUR ANSWER:**
MSE represents how far off the model’s predictions are from the real scores, on average. Squaring the errors makes large mistakes count more, and it also prevents negative errors from canceling out positive ones.
I would only trust the model to predict 10 hours if the training data includes values close to 10. Predicting outside the range may be inaccurate because it has never seen those kinds of examples.



---

### Question 3: Model Reliability
Would you trust this model to predict a score for a student who studied 10 hours? Why or why not? Consider:
- What's the maximum hours in your dataset?
- What happens when you make predictions outside the range of your training data?

**YOUR ANSWER:**
I would only trust the model to predict 10 hours if the training data includes values close to 10. Predicting outside the range may be inaccurate because it has never seen those kinds of examples. I think this is known as extrapolation, linear regression models can output very unreliable results when it comes to making predictions outside of their trained data range. 



---

## Part 2: Data Analysis

### Question 4: Relationship Description
Looking at your scatter plot, describe the relationship between hours studied and test scores. Is it:
- Strong or weak?
- Linear or non-linear?
- Positive or negative?

**YOUR ANSWER:**
The scatter plot shows a strong, linear, and positive relationship: as hours studied increase, test scores also increase consistently.



---

### Question 5: Real-World Limitations
What are some real-world factors that could affect test scores that this model doesn't account for? List at least 3 factors.

**YOUR ANSWER:**
1. Test anxiety or stress
2. Sleep and health
3. Quality of study materials or teaching
4. Student motivation or intensity of focus.


---

## Part 3: Code Reflection

### Question 6: Train/Test Split
Why do we split our data into training and testing sets? What would happen if we trained and tested on the same data?

**YOUR ANSWER:**
We split the data into training and testing sets to evaluate how well the model preforms on new, unseen data. If we trained the model on the same data we tested it on, the model would most likely preform perfectly on that data, however would fail to extrapolate its knowledge to unseen data. My reasearch says this is called overfitting, "where the model memorizes instead of learning the underlying pattern."




---

### Question 7: Most Challenging Part
What was the most challenging part of this assignment for you? How did you overcome it (or what help do you still need)?

**YOUR ANSWER:**
The most challenging part for me was understanding how to interpret the evaluation metrics, R^2 and MSE and what they mean in real terms. I mostly overcame this challenge by reasearching on google and reviewing examples I could find online. I also compared different model outputs to see how changes in the data affect the results. 




---

## Part 4: Extending Your Learning

### Question 8: Future Applications
Describe one real-world problem you could solve with linear regression. What would be your:
- **Feature (X):** 
- **Target (Y):** 
- **Why this relationship might be linear:**

**YOUR ANSWER:**
Feature (X): Square footage of a house
Target (Y): Sale price
This relation may be linear as generally as the size of a house increases, its price also increases, of course many other factors affect price other than just square footage, however it should stll be a roughly linear relation. 




---

## Grading Checklist (for your reference)

Before submitting, make sure you have:
- [ ] Completed all functions in `a6_part1.py`
- [ ] Generated and saved `scatter_plot.png`
- [ ] Generated and saved `predictions_plot.png`
- [ ] Answered all questions in this writeup with thoughtful responses
- [ ] Pushed all files to GitHub (code, plots, and this writeup)

---

## Optional: Extra Credit (+2 points)

If you want to challenge yourself, modify your code to:
1. Try different train/test split ratios (60/40, 70/30, 90/10)
2. Record the R² score for each split
3. Explain below which split ratio worked best and why you think that is

**YOUR ANSWER:**
