# mood_responses.py, functions to import current moods
def mood_response(mood):
    if mood.lower() == "happy":
        print("I am feeling great today!")
    elif mood.lower() == "sad":
        print("I am not feeling so great today")
    elif mood.lower() == "excited":
        print("I am just so excited! I just can't hide it!")
    elif mood.lower() == "mad":
        print("I am in a serious grumpy mood right now.")
    else:
        print("Enter a valid emotion!")