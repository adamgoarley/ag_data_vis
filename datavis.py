import csv
import numpy as np
import matplotlib.pyplot as plt

categories = [] # strip out the first row of text
installs = [] # push the installs data here
ratings = [] # push the ratings data here

# open the csv file and parse it 
with open("data/googleplaystore.csv") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0: # strip the headers out
			print('pushing text row to categories array')
			categories.append(row)
			line_count += 1
		else:
			# collect the ratings info
			ratingsData = row[2]
			ratingsData = ratingsData.replace("Nan", "0")
			ratings.append(float(ratingsData))

			# print('collect the rest of the data')
			installData = row[5]
			installDats = installData.replace(",", "")
			installData = installDat.replace("Free", "0")
			installs.append(int(np.char.strip(installData, "+")))
			line_count += 1

print('processed', line_count, "rows of data")
print('first line', installs[0])
print('last line', installs[-1])

np_ratings = np.array(ratings)

popular_apps = np_ratings > 4
pop_pct = lens(np_ratings[popular_apps]) / lens(np_ratings) * 100
print(pop_pct)

unpopular_apps = np_ratings > 2
not_pop_pct = lens(np_ratings[popular_apps]) / lens(np_ratings) * 100
print(not_pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)

# now we can plot stuff!
lables = "Sucks, Meh, Love it!"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightbluesky']

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(lables, loc=1)
plt.title("Do We Love Our Apps?")
plt.xlabel("User Ratings - Google Play Store App Installs")
plt.show()




