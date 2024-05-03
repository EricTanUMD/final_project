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
        
        # ask
        self.exercises = None
        # externally stored exercises in json file created by Jaylen Carrillo
        self.load_data('exercises.json')
         
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
                            
    # Created by Jaylen Carrillo
    # Use of json.load 
    def load_data(self, filepath):
        """
        will come back to this
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
               result += f"Muscle Group: {activity['muscle_group']} Workout: {activity['workout']} Time: {activity['time']} Reps: {activity['reps']}\n"
        return result
        # should return a massive string in the format of
        # Day:
        # a line for each activity's information

    def delete_activity(self, day_index, activity_index):
        # made by Ibrahim Barry, Magic Methods
        """
        A method to delete an activity that has not been completed

        Args:
            day_index (int) : Index of the day in the week (0 for Monday, 1 for Tuesday, 2 for Wednesday, etc.)
            activity_index (int) : Index of the activity to delete

        Raises:
            IndexError: If there is an index out of range, it will raise the index error.
        """

        try:
            del self.week[day_index][activity_index]
        except IndexError:
            raise IndexError("Day or activity is out of range.")

    def __delitem__(self, key):
        # Made by Ibrahim Barry
        """ Deletes an entire days worth of activities.

            Args:
                key (): Index of the day you wish to remove.
        """

        self.week[key].clear()

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
        day_index = key
        try:
            return self.week[day_index]
        except IndexError:
            raise IndexError("Day or activity is out of range")

    def export_data(self, filepath):
        # Peterson, With statements 
        """
    A method that exports the str method to a textfile.

    Args:
        filepath: A file for the str method to write too.
    """
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(self))

    def max_reps(self, day):
        # Peterson, Keys
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                    "Saturday", "Sunday"]

        other = sorted((self.week[day]), key=lambda s: s["reps"])

        return f"Max reps from {weekdays[day]} is {other[0]['reps']}"

        
    # Created by Jaylen Carrillo
    # Conditional expression
    def recommend_exercises(self, muscle_group):
        """ Recommends up to three random exercises for the specified muscle
        group by looking up the class's exercises dictionary.

        Args:
            muscle_group (str): The name of the muscle group for which to
            recommend exercises.

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
        message = f"No exercises found for muscle group: {muscle_group}"
        return random.sample(recommended, min(len(recommended), 3)) if recommended else message
    
    # Designed by Kanyi
    def workout_visualization(self):
        '''
            Visualizes the total workout duration for each day of the week.
            Prompts the user to input workout details for each day.
        '''
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        total_times = []
        print("\n")
        print("_______________________________________________")
        print("             # Visualization                   ")
        print("_______________________________________________")
        print("Enter workout details for each day of the week.")
        for day_index, day in enumerate(self.week):
            print(f"\nDay: {days[day_index]}")
            activity_count = int(input("Enter the number of activities for this day: "))
            total_time = 0
            for x in range(activity_count):
                print(f"\nActivity {x + 1}:")
                muscle_group = input("Muscle group: ")
                workout = input("Workout: ")
                time = int(input("Time (minutes): "))
                reps = input("Reps: ")
                total_time += time
                self.week[day_index].append({
                    "muscle_group": muscle_group,
                    "workout": workout,
                    "time": time,
                    "reps": reps
                })
            total_times.append(total_time)
        plt.bar(days, total_times, color='green')
        plt.xlabel('Day of the Week')
        plt.ylabel('Total Workout time (minutes)')
        plt.title('Total Workout time for Each Day of the Week')
        plt.tight_layout()
        plt.show()
        print(" ")
        print("Thanks for Providing the Data, Hope you Enjoy!")
        print("______________________________________________")
        
    
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
    print("\n")
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
    recommended_exercises = tracker.recommend_exercises(muscle_group)
    print(f"Recommended exercises for {muscle_group}: {recommended_exercises}")
    tracker.export_data("test.txt")
    print(tracker.max_reps(0))
    tracker.workout_visualization()  # Calling the workout_visualization method(Kanyi)
    display_summary(tracker)  # Calling display_summary method(Kanyi)
    tracker.__getitem__(int(input("Pick a day you would like to see your activity: ")))


if __name__ == "__main__":
    main()