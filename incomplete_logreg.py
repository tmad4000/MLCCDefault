import numpy as np
from util import *

def sigmoid(z):
  return np.exp(log_sigmoid(z)) #better
  #return 1 / (1 + np.exp(-z))

def log_sigmoid(z):
  # n.b. -np.logaddexp(0,-z) calculates -log(1+exp(-z)) 
  # in log space without exponentiation to avoid overflow.
  # Try help(numpy.logaddexp) in the interpreter for
  # more information.
  return -np.logaddexp(0,-z)

def log_sigmoid_complement(z):
  return -np.logaddexp(0,z)

# This function should calculate the negative conditional 
# log probability of the data x given weights w and 
# observed response variables y.
#https://www.cs.ox.ac.uk/teaching/materials13-14/machinelearning/lecture_logistic_regression_4up.pdf  page 10/23
# MLE Gradient, lecture 5
#y is t
def objective(x, y, w):
  z = np.dot(x, w)
  return -(y*log_sigmoid(z)+(1-y)*log_sigmoid_complement(z));

# This is the log Gaussian prior 
def log_prior(w, alpha):
  return np.dot(w, w) / (2*alpha)

# This function should calculate the gradient of the negative 
# conditional log probability of the data x given weights w
# and observed response variables y.
#slide 11/23
# MLE Gradient continued, lecture 5
#y is t
def grad(x, y, w):
  
  z = np.dot(x, w)
  
  return np.dot(sigmoid(z)-y,x)
  # return ...
  #appy tanh on entire dataset

# This is the derivative of the Gaussian prior
#lecture 6 Logistic Regression Summary side 11/25 The gradient:
def prior_grad(w, alpha):
  #gamma^2 = alpha
  return w/alpha
  # return ...
