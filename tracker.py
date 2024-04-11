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
                path (optional str): the path to the file with exercise info
            Side effects:
                creates a Tracker
            Raises:
                Value Error: will raise if any line violates the format
        """
        # create a list of lists. Each index represents a day of the week.
        self.week = [[] for _ in range(7)]

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
                                self.week[0] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Tu"):
                                self.week[1] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "We"):
                                self.week[2] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Th"):
                                self.week[3] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Fr"):
                                self.week[4] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Sa"):
                                self.week[5] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                            elif (match.group("day") == "Su"):
                                self.week[6] = {
                                    "muscle_group": match.group("muscle_group"),
                                    "workout": match.group("workout_type"),
                                    "time": match.group("time"),
                                    "reps": match.group("reps")
                                }
                
    # Made by Eric Tan
    def __str__(self):
        """ String representation of a Tracker
        
            Returns: A string listing the number of exercises and one which day 
        """
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
                    "Saturday", "Sunday"]
        result = ""
        # access each day and its activities. Day is the index, activities is 
        # the list of activities. Returns 
        for day, activities in enumerate(self.week):
            weekday = weekdays[day]
            result += f"{weekday}:\n"
            for activity in activities:
                result += f"    Muscle Group:{activity["muscle_group"]} Workout:{activity["workout"]} Time: {activity["time"]} Reps: {activity["reps"]}\n"
        return result 
        # should return a massive string int the format of
        # Day:
        # a line for each activity's information     
        
    def delete_activity():
        """
        A method to delete an activity that has not been completed
        
        Atrributes:
            del_workout(str) = workout that needs to be removed.
        """
        
    def export_data(self, filepath):
        with open(filepath, "w", encoding = "utf-8"):
            pass
        
def display_summary(tracker):
    '''
        Display a summary of the workout activities within a week from the 
        provided Tracker instance. 

        Args:
            tracker (Tracker): An instance of the Tracker class containing 
            workout information.

        Returns:
            None

        Side effects:
            Printing out the workout summary for the week using the __str__ method
            of the Tracker class.

    '''
    print (f" Stay committed! Your weekly workout summary:\n{tracker}")  