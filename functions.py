# Functions for WPM, Accuracy, Speed, TimeTrack etc

import time         
import random   
from sentences import easy_sentences, medium_sentences, hard_sentences

class Main:

    #method to check accuracy
    @staticmethod
    def accuracyCheck(total_typed_char,correct_char):
        if total_typed_char==0:           #no data to check
            return 0
        else:
            accuracy=correct_char/total_typed_char*100      #accuracy check formula
            return accuracy

    #moethod to calculate words per minute
    @staticmethod
    def WPM_calculate(total_char,total_time):
        words=total_char/5               #standard word length 5
        minutes=total_time/60            #convert to minutes
        if minutes>0:
            WPM=words/minutes                #words per minute
            return WPM
        else:
            return 0
    
    #method to track time (total given vs time taken)
    @staticmethod
    def timeTrack(start_time,end_time):
        if start_time==0 or end_time==0:
            return 0
        else:
            time_taken=end_time-start_time
            return time_taken

    #method to load random sentence according to the level of difficulty
    @staticmethod
    def LoadRandomSentence(difficulty):
        if difficulty=="easy":
            return random.choice(easy_sentences)
        elif difficulty=="medium":
            return random.choice(medium_sentences)
        elif difficulty=="hard":
            return random.choice(hard_sentences)

    #method to reset UI (to the start) 
    @staticmethod
    def reset():
        return{ "input_text":"",
               "start_time":0,
               "end_time":0,
               "correct_char":0,
               "total_typed_char":0,             
        }