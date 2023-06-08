def freGrade(score):
    
    if score > 90:
        grade = "5th grade and lower (Very easy)"
    elif score >= 80:
        grade = "6th grade (Easy to read)"
    elif score >= 70:
        grade = "7th grade (Fairly easy to read)"
    elif score >= 60:
        grade = "8th & 9th grade (Plain English)"
    elif score >= 50:
        grade = "10th to 12th grade (Fairly difficult)"
    elif score >= 30:
        grade = "College (Difficult to read)"
    else:
        grade = "College graduate (Very difficult to read)"
    
    return grade

def fkraANDcliANDsmogGrade(score):

    if score <= 6:
        grade = "6th grade"
    elif score < 7:
        grade = "7th grade"
    elif score < 8:
        grade = "8th grade"
    elif score < 9:
        grade = "High school freshman"
    elif score < 10:
        grade = "High school sophomore"
    elif score < 11:
        grade = "High school junior"
    elif score < 12:
        grade = "High school senior"
    elif score < 13:
        grade = "College freshman"
    else:
        grade = "College sophomore"

    return grade

def ariGrade(score):

    if score <= 1:
        grade = "Kindergarten"
    elif score >= 14:
        grade = "College"
    else:
        grade = str(int(score)-1) + "th grade"

    return grade
