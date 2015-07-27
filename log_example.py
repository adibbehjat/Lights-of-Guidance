import json

with open('lights_of_guidance.json') as data_file:    
    data = json.load(data_file)

# Show subject numbers for the topic "ADMINISTRATIVE ORDER" 
print data['main_topic']['ADMINISTRATIVE ORDER']['subjects']

# Show all the subtopics
for subtopic in data['sub_topics']:
	print subtopic.encode('utf8')

# Print the guidance that has the number 63
print data['subjects']['63']['guidance'].encode('utf8')