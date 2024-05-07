from argparse import ArgumentParser
import re
import sys
import random
import matplotlib.pyplot as plt
import json


class Tracker():
    """ Representation of a fitness tracker for a week

        Attributes:
                week (list(lists(dict)): a list with a list containing exercise
                information for the week.
    """

    # Made by Eric Tan, Regular Expression and Generator expression
    def __init__(self, path=None):
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
    
        # externally stored exercises in json file created by Jaylen Carrillo
        self.load_exercise_data('exercises.json')

        if (path is not None):
            # All exercises come in the format
            # muscle_group,workout_type,time(mins),reps,day
            # Parse through the file and insert workout information into the
            # designated day
            days = {"Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4,
                    "Sa": 5, "Su": 6}
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
            with open(path, "r") as file:
                for line in file:
                    match = re.match(regex, line)
                    if (match is None):
                        raise ValueError("Wrong format for exercise")
                    else:  # check which day each exercise is in
                        day_index = days.get(match.group("day"))
                        if day_index is not None:
                            self.week[day_index].append({
                                "muscle_group": match.group("muscle_group"),
                                "workout": match.group("workout_type"),
                                "time": match.group("time"),
                                "reps": match.group("reps")
                            })
                            
    # Created by Jaylen Carrillo (use of json.load)
    def load_exercise_data(self, filepath):
        """ Loads exercise data from a exercise.json file into the 'exercises' 
            attribute of the class.
        
            Args:
                filepath (str): The path to a JSON file containing exercise data.
            
            Side effects:
                Reads from a file specified by 'filepath'.
        """
        with open(filepath) as json_file:
            self.exercises = json.load(json_file)
    
    # Made by Eric Tan
    def __str__(self):
        """ String representation of a Tracker

            Returns: A string listing the number of exercises for each day
        """
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                    "Saturday", "Sunday"]
        result = ""
        # access each day and its activities. Day is the index, activities is
        # the list of activities. Returns a string representation afterwards
        for day, activities in enumerate(self.week):
            weekday = weekdays[day]
            result += f"{weekday}:\n"
            for activity in activities:
                result += f"Muscle Group: {activity["muscle_group"]} Workout: {activity["workout"]} Time: {activity["time"]} Reps: {activity["reps"]}\n"
        return result 
        # should return a massive string in the format of
        # Day:
        # a line for each activity's information


    def __delitem__(self, day_index):
        # made by Ibrahim Barry, Magic Methods
        """
        A method to delete a day's worth of activities incompleted.

        Args:
            day_index (int) : Index of the day in the week (0 for Monday, 1 for Tuesday, 2 for Wednesday, etc.)
           

        Raises:
            IndexError: If there is an index out of range, it will raise the index error.
        """
        print()
        days = {"Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4,
                    "Sa": 5, "Su": 6}
        day_index = days[day_index]
        
        try:
            self.week[day_index].clear()
            print(self.week)
        except IndexError:
            raise IndexError("Day or activity is out of range.")

    def __getitem__(self, key):
        # Made by Ibrahim Barry
        """ Allows user to find activities from a day using the same syntax as the __delitem__ function

            Args:
                key (int): Number containing the day and the activity the user would like to access.

            Returns:
                dict: Activity information.

            Raises:
                IndexError: If day is out of range, function raises an index error.
        """
        

        days = {"Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4,
                    "Sa": 5, "Su": 6}
        if key > 6 or key < 0:
            raise IndexError("Day or activity is out of range")
        else:
            day_string = {day for day in days if days[day] == key}
            print(day_string, " : ")
            print(self.week[key])


    def export_data(self, filepath):
        # Peterson, With statements 
        """
    A method that exports the str method to a textfile.

    Args:
        filepath: A file for the str method to write too.
        
    Returns: 
        Txt of the string representation
    
    
    """
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(self))

    def max_reps(self, day):
        """
    A method that gives the maximum amount of reps from a specific day.

        Args:
            day: specific day of week M-S
            
        Returns: String with maximum amount of reps
        """
        # Peterson, Keys
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                    "Saturday", "Sunday"]

        other = sorted((self.week[day]), key=lambda s: s["reps"])
        return f"Max reps from {weekdays[day]} is {other[0]['reps']}"

        
    # Created by Jaylen Carrillo (use of a conditional expression and optional parameter)
    def recommend_exercises(self, muscle_group, num_exercises=3):
        """ Recommends up to three random exercises for the specified muscle
        group by looking up the class's exercises dictionary.

        Args:
            muscle_group (str): The name of the muscle group for which to
            recommend exercises.
            
            num_exercises (int, optional): The number of exercises to recommend. Default/minimum is 3.

        Returns:
            list of str: A list containing up to three recommended exercises as
            strings if the muscle group is found.

            str: A message indicating no exercises were found for the muscle
            group.
        """
        muscle_group = muscle_group.lower()
        # finds the list of exercises for the given muscle group
        recommended = self.exercises.get(muscle_group)
        # if not found, it will return this message
        message = f"No exercises found for '{muscle_group}'. Please input a valid muscle group (legs, chest, core, abs, arms, back, shoulders, glutes)."
        return random.sample(recommended, min(len(recommended), num_exercises)) if recommended else message
    
    # Designed by Kanyi
    def workout_visualization(self):
        '''
            Visualizes the total workout duration for each day of the week.
            Uses sample data for the visualization.
        '''
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        total_times = []
        print("\n")
        print ("____________________________________________")
        print("|             # Visualization                 |")
        print("|_____________________________________________|")
        User_Imput_sample_data = [
        [{"muscle_group": "Legs", "workout": "Squats", "time": 30, "reps": "10"},
         {"muscle_group": "Arms", "workout": "Push-ups", "time": 20, "reps": "15"}],  # Monday
        [{"muscle_group": "Chest", "workout": "Bench Press", "time": 45, "reps": "12"},
         {"muscle_group": "Back", "workout": "Pull-ups", "time": 25, "reps": "8"}],   # Tuesday
        [{"muscle_group": "Shoulders", "workout": "Shoulder Press", "time": 35, "reps": "10"}], # Wednesday
        [{"muscle_group": "Core", "workout": "Planks", "time": 15, "reps": "30"}],    # Thursday
        [{"muscle_group": "Legs", "workout": "Lunges", "time": 25, "reps": "12"}],    # Friday
        [{"muscle_group": "Arms", "workout": "Bicep Curls", "time": 20, "reps": "15"}],  # Saturday
        [{"muscle_group": "Back", "workout": "Deadlifts", "time": 40, "reps": "10"}]     # Sunday
        ]
        for day_index, day_data in enumerate(User_Imput_sample_data):
            total_time = sum(activity["time"] for activity in day_data)
            total_times.append(total_time)
        plt.bar(days, total_times, color='blue')
        plt.xlabel('Day of the Week')
        plt.ylabel('Total Workout time (minutes)')
        plt.title('Total Workout time for Each Day of the Week')
        plt.tight_layout()
        plt.show()
        print("\n")

    # Designed by Kanyi
    # f-strings
    def workout_summary(self):
        '''
        Create a workout summary information with f-strings containing expressions.
        Returns: 
            String: A summary of the tracker's information.
        '''
        total_days_count = len(self.week)
        total_activities = sum(len(day) for day in self.week)
        avg_activities_per_day = total_activities / total_days_count if total_days_count > 0 else 0
        return f"Total days: {total_days_count}, Total activities: {total_activities}, Average activities per day: {avg_activities_per_day:.2f}"
        
# Designed by Kanyi
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
    print(f" Stay committed! Your weekly workout summary:\n{tracker}")

def main():
    """ Prompts the user to input a muscle group and prints a list of up to
    three recommended exercises for that muscle group. This function uses
    recommend_exercises method to retrieve the exercise recommendations.
    """
    filename = input("Input file name: ")
    tracker = Tracker(filename)
    print("Enter the muscle group you want to focus on today: ")
    muscle_group = input().strip()
    # need help coming up with a way where i can ask user to try again if they put an invalid muscle group without hard coding
    while True:
        num_exercises = int(input("How many exercises would you like for today's workout? Please choose a number between 3 and 8: "))
        if 3 <= num_exercises <= 8:
            break
        else:
            print("Invalid input. Please enter a number between 3 and 8.")
            
    recommended_exercises = tracker.recommend_exercises(muscle_group, num_exercises)
    print(f"Recommended exercises for {muscle_group}: {recommended_exercises}")
    tracker.export_data(input("Output file name: "))
    print(f"Maximum reps for Monday {tracker.max_reps(0)}")
    tracker.workout_visualization()  # Calling the workout_visualization method(Kanyi)
    display_summary(tracker)  # Calling display_summary (Kanyi)
    print(tracker.workout_summary()) # Calling the workout summary method(Kanyi)
    tracker.__getitem__(int(input("Pick a day you would like to see your activity: "))) 
    day_index = int(input("Choose a day to remove your activities from (0-6): "))
    if 0 <= day_index <= 6:
        del tracker.week[day_index]
        print(f"Activities for day {day_index + 1} have been removed.")
    else:
        print("Invalid day entered. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
