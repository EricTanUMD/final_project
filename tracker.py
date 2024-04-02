from argparse import ArgumentParser
import re
import sys

class Tracker():
    """ Representation of a fitness tracker for a week"""
    def __init__(self, path = None):
        """ Initializes a Tracker using a path to a textfile containing
            Strings of a specific pattern. These are used to add the information
            into week as dictionaries.
            
            Args:
                path (optional str): the path to the 
        """
        week = [[] for num in range(7)]

        if (path is not None):
                regex = r'''(?x)^
                    (?P<workout_type>[-\w\s])
                    ,
                    (?P<time>\d+)
                    ,
                    (?P<reps>\d+)
                    ,
                    (?P<day>\w{2})
                    '''
                # Parse through the file and insert workout information into the
                # designated day
                with open(path, "r") as file:
                    for line in file():
                        match = re.match(regex, line)
                        if (match == None):
                            raise ValueError("Wrong format for exercise")
                        else: # check which day each exercise is in
                            if (match.group("day") == "Mo"):
                                week[0] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Tu"):
                                week[1] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "We"):
                                week[2] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Th"):
                                week[3] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Fr"):
                                week[4] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Sa"):
                                week[5] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Su"):
                                week[6] = {
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                
    
    def __str__(self):
        pass