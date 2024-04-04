from argparse import ArgumentParser
import re
import sys

class Tracker():
    """ Representation of a fitness tracker for a week"""
    # made by Eric Tan
    def __init__(self, path = None):
        """ Initializes a Tracker using a path to a textfile containing
            Strings of a specific pattern. These are used to add the information
            into week as dictionaries.
            
            Args:
                path (optional str): the path to the file with exercise info
            Side effects:
                creates a Tracker
            Raises:
                Value Error: will raise if any line violates the format
        """
        week = [[] for num in range(7)]

        if (path is not None):
            # All exercises come in the format
            # muscle_group,workout_type,time(mins),reps,day
                regex = r'''(?x)^
                    (?P<muscle_group>[-\w\s]+)
                    ,
                    (?P<workout_type>[-\w\s]+)
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
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Tu"):
                                week[1] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "We"):
                                week[2] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Th"):
                                week[3] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Fr"):
                                week[4] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Sa"):
                                week[5] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Su"):
                                week[6] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                
    # Made by Eric Tan
    def __str__(self):
        """ String representation of a Tracker
        
            Returns: The exercises from each day as a string. 
        """
        pass
        
    def delete_activity():
        """
        A method to delete an activity that has not been completed
        
        Atrributes:
            del_workout(str) = workout that needs to be removed.
        """
        
        
    def export_data():
        with open(filepath, "w", encoding = "utf-8"):
