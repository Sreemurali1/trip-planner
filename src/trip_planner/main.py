#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from trip_planner.crew import TripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'i want to plan a trip to kodaikanal from hosur for 4 days starting from 2025-02-03',
        'current_year': str(datetime.now().year)
    }
    
    try:
        TripPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

