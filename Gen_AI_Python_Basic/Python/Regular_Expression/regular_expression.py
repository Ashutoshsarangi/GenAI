import re

# Basic Regex Pattern

# - \d matches any digit (0-9)
# - \w matches any word character (alphanumeric + underscore) (a-z, A-Z, 0-9, _)
# - \s matches any whitespace character (space, tab, newline)
# - . (dot) matches any character except newline

# Qunatifiers

# + matches one or more occurrences
# * matches zero or more occurrences
# ? matches zero or one occurrence
# {n} matches exactly n occurrences
# {n, m} matches between n and m occurrences

#Example

post = 'Exploreing the world with #genAi and #python + #regex, #artificialintelligence'

hashtags = re.findall(r'#\w+', post)

print(hashtags)

# anchors and grouping
# ^ matches the start of a string
# $ matches the end of a string


# Character Classes
print(re.findall(r'[aeiouAEIOU]', 'Generative AI'))

#key patterns

# [abc] matches a, b, or c
# [^abc] matches any character except a, b, or c (IMPORTANT)
# [a-z] matches any lowercase letter
# [A-Z] matches any uppercase letter
# [0-9] matches any digit
# [a-zA-Z] matches any letter (lowercase or uppercase)
# [a-zA-Z0-9] matches any alphanumeric character

print(re.findall(r'[^a-z]', 'Hello World!!! 123')) # matches all except lowercase letters


valid_user_name = 'GEN_AI_dev42'
invalid_user_name = 'GEN_AI_dev42!'
invalid_user_name2 = 'dev42'

#^ matches the start of the string
#[a-zA-Z0-9_] matches any alphanumeric character or underscore
#+ matches one or more occurrences of the previous pattern
#$ matches the end of the string

if re.match(r'^[a-zA-Z0-9_]+$', valid_user_name):
    print('Valid User Name for valid_user_name')
else:
    print('Invalid User Name')

# I wanted to match if the user name has more than 5 to 10 characters {n, m}
if re.match(r'^[a-zA-Z0-9_!]{5,}$', invalid_user_name):
    print('Valid User Name for invalid_user_name')
else:
    print('Valid User Name')

# replace using regEx
text = 'Hello World!!! 123'
# replace all non-alphanumeric characters with a space
print(re.sub(r'[^a-zA-Z0-9 ]', '%', text)) #sub --> substitution


text = 'AI conference is 23/05/2025'
# replace the date format dd/mm/yyyy with yyyy-mm-dd
print(re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text))

text = "Let's go! Ready now? Begin the test."
parts = re.split(r'[.!?]\s', text)
print(parts)
# Output: ["Let's go", 'Ready now', 'Begin the test']
#the regex pattern [.!?]\s 
# splits the text on punctuation marks followed by a whitespace.
#  While the original text contains punctuation marks like .,! and ?, 
# the pattern removes them during splitting