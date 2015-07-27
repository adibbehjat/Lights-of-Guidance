import json
import re

def start_process():

    # Open the file and let's explore
    html = open('log_page1.html', 'r')
    guidances = read_line_after_line(html)
    print guidances
    json_guidances = json.dumps(guidances)
    file_location = 'lights_of_guidance.json'
    f = open(file_location, 'w')
    f.write(json_guidances)
    f.closed
    print "JSON Delivered"
    return

def read_line_after_line(html):

    # Initialize Data Structure
    json_set = {}
    json_set['main_topic'] = {}
    json_set['sub_topics'] = {}
    json_set['subjects'] = {}

    # Initialize Variables
    total_m = 0
    total_s = 0
    total = 0
    parent = ''
    subtopic = ''

    # Array that includes data
    subjects = [] # Carries only the subject number for subtopics
    msubjects = [] # Carries only the subject number for main topics
    subtopics = [] # Carries only the subtopic title

    for line in html.readlines():

        '''
            The regular expression will collect two items, one is the 
            number/position of the topic, the second is the title of the topic.
            If the regex cannot satisfy the search, it'll return None type, enabling
            easy logical flow.

            is_object.group(1) is the number/position of the topic
            is_object.group(2) is the title of the subject/topic

            Both regex groups returns a string
        '''

        is_main_topic = re.search('^([A-Z]+)\. ([A-Z\W]+)$\n', line)
        
        is_sub_topic = re.search('^([A-Z])\. ([A-Za-z\W].+)?\n', line)

        is_subject = re.search('^(\d+)\. ([A-Za-z\s\W].+)?\n', line)

        if is_main_topic:
            
            # If the structure of parent already is present, provide link to sub-topics
            if total_m > 0:
                
                # Provide data to the subtopics and subjects in each main topic
                json_set['main_topic'][parent]['sub_topics'] = subtopics
                json_set['main_topic'][parent]['subjects'] = msubjects
                
                # Collect the subject numbers for the last subtopic
                if subtopic:
                    json_set['sub_topics'][subtopic]['subjects'] = subjects
                    subtopic = ''
                
                # Reset variables
                subtopics = []
                msubjects = []
                subjects = []

            # Set parent
            parent = is_main_topic.group(2)
            
            # Build the main topic branch
            json_set['main_topic'][parent] = {}
            json_set['main_topic'][parent]['position'] = is_main_topic.group(1)

            total_m += 1

        elif is_sub_topic:

            if total_s > 0:

                # Collect the subject numbers for the subtopic
                if subtopic:
                    json_set['sub_topics'][subtopic]['subjects'] = subjects
                    # Reset subjects
                    subjects = []

            # Build the subtopic branch
            subtopic = is_sub_topic.group(2)
            
            # Build the subtopic branch
            json_set['sub_topics'][subtopic] = {}
            json_set['sub_topics'][subtopic]['parent'] = parent
            json_set['sub_topics'][subtopic]['position'] = is_sub_topic.group(1)

            # Collect subtopic data
            subtopics.append(subtopic)

            total_s += 1

        elif is_subject:

            # Capture subject number (in String format)
            subject_num = is_subject.group(1)

            # Build Subjects branch
            json_set['subjects'][subject_num] = {}
            json_set['subjects'][subject_num]['parent'] = subtopic
            json_set['subjects'][subject_num]['title'] = is_subject.group(2)

            # Collect subject numbers for the parents
            subjects.append(subject_num)
            msubjects.append(subject_num)

            total += 1

        elif line != '\n':
            
            # The rest of the information received is the guidance itself
            try:
                json_set['subjects'][subject_num]['guidance'] += line
            except KeyError:
                json_set['subjects'][subject_num]['guidance'] = line

        json_set["total_main"] = total_m
        json_set["total_subtopics"] = total_s
        json_set["total_subjects"] = total

    return json_set

start_process()