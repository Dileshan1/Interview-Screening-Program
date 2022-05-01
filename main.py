import Selection_criteria
import pandas as pd

data=pd.read_csv("interview_screen.CSV")

if __name__ == '__main__':
    Selection_criteria.interviewee_screening(data)
