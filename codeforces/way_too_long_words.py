"""
File: way_too_long_words.py 
-------------------
Problem source: Codeforces
Problem link: https://codeforces.com/problemset/problem/71/A 
"""

# Input: 
"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""

# Output:
"""
word
l10n
i18n
p43s
"""


def main():

	file = open('inputs/way_too_long_words.txt')
	next(file)
	for line in file:
		line = line.strip()
		if len(line) > 10:
			first_letter = line[0]
			last_letter = line[-1]
			counter = 0
			for i in range(len(line)):
				if i != 0 and i != (len(line) - 1):
					counter += 1
			print(first_letter + str(counter) + last_letter)
		else:
			print(line)


# boilerplate 
if __name__ == '__main__':
    main()