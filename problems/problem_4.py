
# Convert to acronym
# Sample: Random Access Memory = RAM

data = input("Convert to acronym: ")

# Retrieve words ang making sure whitespaces are removed
words = data.strip().split()

acronym = ""
for word in words:
    acronym += word[0].upper()

print("%s = %s" % (acronym, data))
