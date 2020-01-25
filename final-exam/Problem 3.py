"""
You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

Write a Monte Carlo simulation that meets the specifications below. Feel free to write a helper function if you wish.
"""

from random import randint

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    counter = 0
    for trial in range(numTrials):
        balls = ["Green ball", "Green ball", "Green ball", "Green ball", "Red ball", "Red ball", "Red ball", "Red ball"]
        drawed_balls = []
        for draw in range(3):
            randnum = randint(0, len(balls) - 1)
            mydraw = balls[randnum]
            drawed_balls.append(mydraw)
            del balls[randnum]
        if drawed_balls[0] == drawed_balls[1] and drawed_balls[1] == drawed_balls[2]:
            counter += 1
    return (counter / numTrials)
