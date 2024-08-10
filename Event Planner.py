# Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2 
sound = "audio system" if attendees > 100 else "speaker"
print(sound)

visual = "projector" if attendees > 100 else "large tv" 
print(visual)

#Task 3 
vegetarian = input("Would you like vegetarian food? (yes or no): ")
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else """
Gourmet Meals Caterers"""
print(caterer)