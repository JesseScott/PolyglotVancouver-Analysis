#!/usr/bin/python

# Util file to import in all of the notebooks to allow for easy code re-use


# Calculate Percent of Attendees that did not speak
def percent_silent(df):
    total = len(df)
    silent = 0
    for row in df.iteritems():
        if row[1] == 0:
            silent = silent + 1

    percent = {}
    percent['TOTAL'] = total
    percent['SILENT'] = silent
    percent['VERBOSE'] = total - silent
    return percent

# Calculate Percent of Attendees that left
def percent_left(df):
    total = len(df)
    left = 0
    for row in df.iteritems():
        if row[1] == 0:
            left = left + 1

    percent = {}
    percent['TOTAL'] = total
    percent['LEFT'] = left
    percent['STAYED'] = total - left
    return percent

# Calculate Percent of Attendees along gender
def percent_gender(df):
    total = len(df)
    female = 0
    for row in df.iteritems():
        if row[1] == 1:
            female = female + 1

    percent = {}
    percent['TOTAL'] = total
    percent['FEMALE'] = female
    percent['MALE'] = total - female
    return percent

# Calculate Percent of Talking points by
def percent_talking_gender(df):
    total = 0
    male = 0
    female = 0
    for talks, gender in df.itertuples(index=False):
        if talks > 0:
            total = total + 1
            if gender == 0:
                male = male + 1
            elif gender == 1:
                female = female + 1

    percent = {}
    percent['TOTAL'] = total
    percent['FEMALE'] = female
    percent['MALE'] = male
    return percent
