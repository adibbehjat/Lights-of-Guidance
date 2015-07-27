# Lights of Guidance 
##(The Baha'i Guidance Library)

## What it is?
I crawled the  *Lights of Guidance* page (http://bahai-library.com/hornby_lights_guidance), cleaned the HTML, and then built a JSON data format of the whole guidance available for developers and designers.

## Why?
The available *Lights of Guidance* page is useful; however, it is very cluncky and it is not well designed for crawling and parsing purposes. My goal was to create a universal and easy to use *Lights of Guidance* data format for developers and designers to use and build with it more modern libraries without the need to crawl the website (that's what I did).

## The Good Stuff

### Current Available Formats of Light of Guidance
* JSON
* Text (listed as .html)

### Future Formats
* XML
* SQL
* noSQL

## Data Structure

There are three branches/nodes in the JSON data format:
* **main_topics**
    * Position is based on roman numerals (I, II, III, IV, etc.)
    * Some main_topic items do not have sub_topics, but have subjects
* **sub_topics**
    * Position is alphabetical (A, B, C, etc.)
* **subjects**
    * Organized by numbers
    * Numbers are in string format

```JSON
{
  "total_subjects": int, 
  "total_subtopics": int, 
  "total_main": int, 
  
  
  "main_topic": {
    
    "ADMINISTRATIVE ORDER": {
      "position": "I", 
      "sub_topics": [
        "Administrative Order",
      ],
      "subjects": []
      },
    "THE FAST": {
        "position": "XVII", 
        "sub_topics": [], 
        "subjects": ["775", "776", "777", "778", "779", "780", "781", "782", "783", "784"]
        },
    },
    
    
    "sub_topics": {
        "Universities and Colleges": {
        "position": "B",
        "subjects": ["714","715","716","717","718","719","720","721"],
        "parent": "EDUCATION"
        },
    },
    
    
    "subjects": {
        "344": {
        "guidance": "\"The prohibition on representing the Manifestation of God in paintings and drawings or in dramatic presentations applies to all the Manifestations of God. There are, of course, great and wonderful works of art of past Dispensations, many of which portrayed the Manifestations of God in a spirit of reverence and love. In this Dispensation however the greater maturity of mankind and the greater awareness of the relationship between the Supreme Manifestation and His servants enable us to realize the impossibility of representing, in any human form, whether pictorially, in sculpture or in dramatic representation, the Person of God's Manifestations. In stating the Bahá'í prohibition, the beloved Guardian pointed out this impossibility.\"\n(From a letter written on behalf of the Universal House of Justice to an individual believer, March 9, 1977)\n",
        "parent": "Bahá'í Arts and Drama",
        "title": "Prohibition on Representing Manifestations of God in Paintings or Drawings Applies to All Manifestations"
    },
```

### Example

Here are few examples on how you can access the data using Python. Note you need to encode into UTF-8 if you don't want it to crash or yield error:



```python
import json

with open('lights_of_guidance.json') as data_file:    
    data = json.load(data_file)

# Show subject numbers for the topic "ADMINISTRATIVE ORDER" 
print data['main_topic']['ADMINISTRATIVE ORDER']['subjects']

# Show all the subtopics
for subtopic in data['sub_topics']:
  print subtopic.encode('utf8')

# Print the guidance that has subject number 63
print data['subjects']['63']['guidance'].encode('utf8')
```

## Feel free to contribute, support, fork, or improve!