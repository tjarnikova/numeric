def conduction_quiz(answer):
    '''Gives the responses to the conduction quiz: is lambda positive?'''

    # dictionary of responses for conduction quiz
    response = {'True': 'Right!', 'False': 'Sorry.  The idea here is as follows:  Assume that the object is warmer than its surroundings, i.e. T-Ta > 0. We know that the temperature of the object should decrease with time, which translates into dT/dt < 0 in terms of the derivative.  Now, in order that both sides of the differential equation have the same sign, this requires that $\lambda$ > 0.', 'Hint 1': 'Think physically!', 'Hint 2': 'Suppose that the object is warmer than its surroundings (i.e. T-Ta > 0).  Think about what this means for the signs of the terms in the differential equation ....'}
    try:
        return response[answer]
    except KeyError:
        return "Acceptable answers are 'True', 'False', 'Hint 1' or 'Hint 2'"

