import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np

if __name__ == "__main__":
    names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Emily", "Frederik", 
    "Gabriel", "Hannah", "Isabella", "Jacob", "Katherine", "Liam", "Mia", 
    "Nathan", "Olivia", "Peter", "Quinn", "Rebecca", "Samuel", "Theresa", 
    "Ulysses", "Victoria", "William", "Xander", "Yasmine", "Zachary",
    "Amelia", "Aaron", "Sophia", "Noah", "Ava", "James", "Lucas", "Ethan", 
    "Ella", "David", "Elijah", "Aria", "Jackson", "Aiden", "Scarlett", 
    "Sofia", "Matthew", "Logan", "Abigail", "Grace", "Henry", "Isla", 
    "Ryan", "Evelyn", "Oliver", "Sebastian", "Harper", "Caleb", "Chloe", 
    "Julian", "Penelope", "Levi", "Victoria", "Dylan", "Aurora", "Luke", 
    "Hazel", "Isaac", "Samantha", "Theodore", "Lily", "Grayson", "Lillian", 
    "Joshua", "Layla", "Zoe", "Madison", "Owen", "Caroline", "Leo", 
    "Alice", "Mason", "Eleanor", "Wyatt", "Ellie", "Jack", "Nora", "Lucas",
    "Sarah", "Evan", "Luna", "Mila", "Eli", "Sadie", "Landon", "Addison",
    "Jaxon", "Piper", "Lincoln", "Stella", "Connor", "Grace", "Hudson", 
    "Ruby", "Carson", "Sophia", "Asher", "Kinsley", "Christian", "Brielle",
    "Maverick", "Vivian", "Nolan", "Emilia", "Hunter", "Camila", "Adrian", 
    "Archer", "Easton", "Emery", "Maddox", "Faith", "Roman", "Riley"
    ]
    lennames = sorted(names, key=lambda name: len(name))
    alphanames = sorted(names)
    letters = {}
    lengths = {}
    print(lennames)
    print(alphanames)
    for name in names:
        if len(name) not in lengths.keys():
            lengths[len(name)] =1
        else:
            lengths[len(name)] = lengths[len(name)] + 1
        for char in name:
            if char.lower() not in letters.keys():
                letters[char.lower()] = 1
            else:
                letters[char.lower()] = letters[char.lower()] + 1
    average = 0
    for lenght in lengths.values():
        average = average + lenght
    average = average / len(lengths.values())
    plt.figure()
    print(letters)
    plt.bar(letters.keys(),letters.values())
    wc = WordCloud().generate_from_frequencies(letters)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.show()
    plt.figure()
    plt.imshow(wc)
    plt.show()
    plt.figure()
    ax = plt.subplot()
    bar = ax.bar(lengths.keys(),lengths.values(),label = "Name lengths")
    plt.axhline(average,label="Average",linestyle = "--", color = "red")
    plt.xlabel("Lengths")
    plt.ylabel("Frequency")
    bar[int(len(lengths.keys())/2-2) if len(lengths.keys())%2==0 else int((len(lengths.keys())+1)/2-2)].set_color("green")
    bar[int(len(lengths.keys())/2-2) if len(lengths.keys())%2==0 else int((len(lengths.keys())+1)/2-2)].set_label("Median")
    plt.legend()
    plt.show()
