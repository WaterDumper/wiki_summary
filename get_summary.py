import wikipedia
import csv

areas = ['machine learning', 'robotics', 'artificial intelligence', 'computer vision', 'human-computer interaction', 'natural language processing', 'programming languages', 'computational biology', 'data mining', 'software engineering', 'motion planning', 'distributed systems', 'computer graphics', 'security', 'social computing', 'statistics', 'privacy', 'human-robot interaction', 'control', 'formal methods', 'algorithms', 'computer architecture', 'crowdsourcing', 'social network analysis', 'ubiquitous computing', 'computer science', 'educational data mining', 'machine translation', 'manipulation', 'networking', 'optimization', 'reinforcement learning', 'software architecture', 'education', 'intelligent tutoring systems', 'mobile computing', 'speech recognition', 'bioinformatics', 'computational linguistics', 'information retrieval', 'learning sciences', 'logic', 'operating systems', 'perception']
summary_dict ={}

def GetWikiSummary():
    for area in areas:
        try:
            summary = wikipedia.summary(area)
            summary_dict[area] = summary
        except:
            summary_dict[area] = ""
            continue
    print(len(summary_dict))
    with open('wiki_summaries.csv', 'w') as f:
        w = csv.DictWriter(f, summary_dict.keys())
        w.writeheader()
        w.writerow(summary_dict)
    return None

GetWikiSummary()