# main.py, importing module from mood_responses.py
import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))