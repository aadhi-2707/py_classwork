python={"sam","Adithyan","joseph","jacob"}
datascience={"sam","Adithyan","ashik","joseph"}
python.add("james")
datascience.remove("sam")
print(python)
print(datascience)
print(python & datascience)
print(python - datascience)
print(python | datascience)
# Create dictionary with number of students
course={
    "python":(len(python)),
    "datascience":(len(datascience))  
}
print(course)
# Print with loop
for name, count in course.items():
    print(f"Course: {name}, Students: {count}")
    
double = {name: count * 2 for name, count in course.items()}
print(double)