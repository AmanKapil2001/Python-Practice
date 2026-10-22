Lists
Tuples
Sets
Dictionaries
List Comprehension
String Manipulation
Modules
Packages
File Handling
Exception Handling

LIST:---> A COLLECTION OF MULTIPLE VALUES STORED IN ONE VARIABLE. IT CAN STORE MIXED DATA. List are mutables and can be change.
APPEND --> self.append(num) add the numbers.
Insert :---> add value at specific index. self.insert(number)
remove :---> self.remove(number) remove the values
pop :---> number.pop(num) remove the last value.
len :---> len(number) return the length of item.
modify list :----> number[0] = 90 add the number at 0 position.
Slicing :----> print(num(1:4)) start:End.

data = [1,2,2,3,4,4,5]
def duplicate(number):
   count = []
  try:
      for i in number:
          if i not in count:
              count.append(i)
      return count
   except AttributeError:
          print("correct the error")
result = duplicate(data)
print(result)
Split = self.split() split or extract the two strings.["Aman Kapil"] to ["Aman,Kapil"]

names = ["Aman Sharma", "Raj Varma"]
def extract(first):
   add = []
   for f in first:
       first_name = f.split()[0]
       add.append(first_name)
   return add
result = extract(names)
print(result)

data = [1,2,3,4,5,6,7,8]
def batch(two):
   add = []
   for b in range(0,len(two),2):
       piece = two[b:b+2]
       add.append(piece)
   return add
result = batch(data)
print(result)

numbers = [10,12,11,500,13,9]
def outlier(self):
   add = []
   for s in self:
       if s> 100:
           add.append(s)
   return add
result = outlier(numbers)
print(result)

TUPLES :---> A collection of multiple values stored in one variables. And the Tuples can not be changed. the sighn , is required otherwise it treat the value as integer.
for instance number[0]=100
count---> print(number.count) count the numbers.
print(number.index(3))
import math
point1 = (2,3)
point2 = (5,7)
def distance(p1 , p2):
      result =(math.sqrt(
          (p2[0] - p1[0]))**2 +
           (p2[1] - p1[1])**2
       )
      return result
answer = distance(point1,point2)
print(answer)

tokens = [("Python",1),("AI",2),("ML",3)]
for words,position in tokens:
   print(f"words: {words}, positions:{position}")

data = [
   ("Aman",85),
   ("Raj",72),
   ("Simran",95)
]
toppers = data[0]
for i in data:
   if i[1] > toppers[1]:
       toppers = i
print("toppers name", toppers[0])
print("toppers value", toppers[1])

images = [
   ("cat.jpg",(224,224,3)),
   ("dog.jpg",(128,128,3))
]
for image,(height,width,chanel) in images:
   print(f"image name: {image} , height: {height}, weidth :{width}, channels :{chanel}",)

models = [
   ("CNN",92),
   ("RNN",88),
   ("Transformer",97)
]
best_model = models[0]
for m in models:
   if m[1] > best_model[1]:
       best_model = m
print(f"model name :{m[0]} and the accuracy is {m[1]}")

SETS:---> sets are the collection of the unique values. duplicates are not allowed, no indexing and unordered.
number.add(10) to add the values.
numbers.remove(2) to remove the values.
union (|) this sign is used to combine the sets.
Intersection (&) it will give the unique values.
Differnce (a - b) values in one set.
Set(data) this will convert list ot set.

data = [1,2,2,3,4,4,5]
result = set(data)
print(result)

a = {"python","machine","learning"}
b = {"deep","learning","python"}
result = a & b
print ( result)

user1 = {"Laptop","Phone","Tablet"}
user2 = {"Phone","Watch","Laptop"}
result = user1 & user2
print(result)

registered = {"Aman","Raj","Simran"}
login_attempts = {"Raj","Unknown","Aman"}
result = login_attempts - registered
print(result)

labels = ["cat","dog","cat","bird","dog"]
result = set(labels)
print(result)

customer1 = {"Phone","Laptop","Mouse"}
customer2 = {"Laptop","Keyboard","Mouse"}
print(customer1 & customer2)

pixels = [255,0,255,128,0,64]
print(set(pixels))

model1 = {"accuracy","precision","recall"}
model2 = {"accuracy","f1-score","recall"}
print(model1 | model2)

sentence = {"python","is","very","powerful"}
stopwords = {"is","very"}
result =   sentence - stopwords
print(result)

ids = [101,102,101,103,104,104]
print(set(ids))


DICTIONARIES :---> IT STORE DATA IN KEY AND VALUE PAIRS.
students = {
   "Aman":85,
   "Raj":72,
   "Simran":95
}
topper = ""
highest_marks = 0
for name,marks in students.items():
   if marks > highest_marks:
       highest_marks = marks
       topper = name
print("topper name" , topper)
print("highest marks" , highest_marks)

words = ["python","ai","python","ml","ai","python"]
count = {}
for name in words:
   if name in count:
       count[name] += 1
   else:
       count[name] = 1
print(count)

messages = {
   "msg1" : "win money now",
   "msg2" : "hello friends",
   "msg3" : "free offer"
}
for key,value in  messages.items():
   if "win"in value or "free"in value or "offer" in value:
       print (f"this {key} is spam messages")
   else:
       print(key,value)

user = {
#    "name":"Aman",
   "email":"aman@gmail.com",
   "verified":True
}
if len(user["name"])>3 and "@" in user["email"] and user["verified"]:
       print(f"you are authorised person")

image = {
   "filename":"cat.jpg",
   "shape":(224,224,3)
}
height = image["shape"][0]
width = image["shape"][1]
channels = image["shape"][2]
print("height",height)
print("width",width)
print("channels",channels)

ratings = {
   "Laptop":4.8,
   "Phone":4.2,
   "Tablet":3.5
}
for k,v in ratings.items():
   if ratings[k] >= 4:
       print(f" this product {k} : {v} is recommend")
   else:
       print(f" this product {k} : {v} is not recommend")


bot = {
   "hello":"Hi there!",
   "bye":"Goodbye!",
   "thanks":"Welcome!"
}
while True:
   message = input ("enter the message: ")
   if message in bot:
      print(bot[message])
   else:
      print("i dont understand")

   if message == "bye":
     break


marks = {
   "Aman":85,
   "Raj":72,
   "Simran":95
}
count = 0
add = 0
for name,score in marks.items():
   count += 1
   add += score
average = add / count
print("average score is :" , average)

cnn = {
   "conv1":32,
   "conv2":64,
   "dense":128
}
for k,v in cnn.items():
   print(f"layer {k} has : {v} neurons")

words = ["the","python","is","powerful","the"]
count = 0
for w in words:
   if w =="the" or w =="is":
     continue
   else:
       count = count + 1
       print(w)
print("meaningful words:",count)

List Comprehension:---> A short and powerful way to create lists.

numbers = [1,2,3,4,5,6,7,8,9]
result = [n for n in numbers if n % 2==0]
print(result)

number = [1,2,3,4,5]
result = [n*n for n in number ]
print(result)

words = ["the","python","is","powerful"]
stopwords = ["the","is"]
result = [w for w in words if w not in stopwords]
print(result)

messages = [
   "win money now",
   "hello friend",
   "free offer"
]
result = [ m for m in messages if "win"in m or  "free"in m or "offer" in m  ]
print(result)

pixels = [0,128,255]
esult = [p / 255 for p in pixels]
print(result)

words = ["python","ai","ml"]
result = [w.upper() for w in words]
print(result)

data = ["Python","","AI"," ",None,"ML"]
result = [d for d in data if d not in [" ","",None]]
print(result)

images = [
   ("cat.jpg",(224,224,3)),
   ("dog.jpg",(128,128,3))
]
result = [k[0] for k in images   ]
print(result)

words = ["python","ai","machinelearning"]
result = [len(w) for w in words ]
print( result)

matrix = [
   [1,2],
   [3,4],
   [5,6]
]
result = [num for row in matrix for num in row]
print(result)

tokens = ["Python!","AI,","ML."]
result = [t.replace("!","")
          .replace(",","")
          .replace(".","")
           for t in tokens
         ]
print(result)


tensor = [10,20,30]
result = [t/10 for t in tensor]
print(result)

text = ["the","python","","is","powerful"," ","ai"]
result = [t.upper() for t in text if t not in ["the","is",]  if t not in [""," "]]
print(result)

pixels = [12,255,34,180,90,255,10]
result = [round(p/255,2)for p in pixels if p > 100]
print(result)

tokens = ["Python","AI","deep-learning.","is","awesome!!"]
result = [
         t.replace("!","")
          .replace(".","")
          .lower()
         for t in tokens
       if len( t.replace("!","")
          .replace(".","")
               )>3
          ]
print(result)

transactions = [500,12000,300,45000,700,15000]
result = [t + (0.18 * t) for t in transactions if t > 10000]
print(result)

movies = [
   ("Inception",4.8),
   ("Random Movie",2.1),
   ("Interstellar",4.9),
   ("Average Film",3.0)
]
result = [m[0] for m in movies if m[1]>4]
print(result)

text = [
   "The",
   "Python!",
   "",
   "is",
   "VERY",
   "powerful.",
   " "
]
result = [t.replace("!","")
         .replace(".","")
        .lower()
         for t in text
         if t not in ["The","is"]
         if t not in [" ",""]]
print(result)

String Manipulation:----> it is a collection of characters.
String indexing -->  access characters by using the string. for instance python[0] = p or BACKEND PROCESS [-1] = n
string slicing --> [0:7] start:end points.
.lower --> lower all the characters.
.upper--> capitalize all the characters.
.replace---> replace all the characters. ("!","") change "!" to "".
.split()--> this will convert the string to list. for instance "python is very powerful" to ['python','is','powerful']
" ".join()--> Convert list to sentence for instance ['python','is','powerful'] to Python is powerful.
.strip()---> remove the extra spaces. " Python " to python

email = "aman@gmail.com"
result = email[email.index("@")+1:]
print(result)

messages = [
   "win money now",
   "hello friend",
   "free iphone",
   "normal text",
   "limited offer"
]
count = 0
for m in messages:
   if "win" in m or "free" in m or "offer" in m:
       count += 1
print(count)

password = "Python@123"
special = False
uppercase = False
lowercase = False
digit = False

for p in password:
   if p.isdigit():
       digit = True
   if p.isupper():
       uppercase = True
   if p.islower():
       lowercase = True
   if p == "@":
       special = True
if uppercase and lowercase and digit and special and len(password) > 8:
   print("password is strong")
else:
   print("password is weak")

sentence = "python ai python ml ai python"
word =    sentence.split()
frequency = {}
for w in word:
   if w in frequency:
       frequency[w] += 1
   else:
       frequency[w] = 1
print(frequency)

documents = [
   "python is powerful",
   "machine learning with python",
   "deep learning"
]
for d in documents:
   if "python" in d:
       print(d)

text = "the ai model is very powerful"
word = text.split()
result = []
for w in  word:
   if w not in  ["the","is","very"]:
       result.append(w)
print(" ".join(result))

comments = [
   "you are stupid",
   "great work",
   "idiot person",
   "excellent model"
]
result = []
for c in comments:
   if "stupid" in c or "idiot" in c  :
       result.append(c)
print(result)

messages = [
   "win money",
   "hello friend",
   "free iphone"
]
def spam(data):
   count = 0
   for m in data:
       if "win" in m or "free" in m:
         count += 1
   return count
print(spam(messages))

text = "PYTHON!!! is AWESOME."


def clean(data):
   result = [c.replace("!", "")
             .replace(".", "")
             .lower()

             for c in data
             ]
   return result
print(clean(text))

File Handling:----> this is used for handling the files.
import csv
students = [["name","marks"],
          ["Aman", 85],
          ["Raj",72],
          ["Simran",95]]

file_path = "students.csv"
with open(file_path, "w",newline="") as file:
   write = csv.writer(file)
   write.writerows(students)
   print(f"csv file {file_path} created")

with open("students.csv","r") as file:
   reader = csv.reader(file)
   next(reader)
   for name,marks in reader:
       if int(marks) > 80:
           print(name,marks)



text = "PYTHON is AWESOME!!! \n AI is POWERFUL!!!"
file_path = "reviews.txt"
with open(file_path,"w",newline="") as file:
   file.write(text)
   print(f"text file {file_path} created")

with open(file_path,"r") as file:
    text = file.read()
cleaned = text.replace("!","").lower()

with open("cleaned.txt","w") as file:
   file.write(cleaned)
print(cleaned)
import json
auth = [
 {"name":"Aman","verified":True},
 {"name":"Raj","verified":False}
]
file_path = "users.json"
with open(file_path,"w", newline="") as file:
   json.dump(auth,file)
   print(f"json file {file_path} created")

with open(file_path,"r",newline="") as file:
   user = json.load(file)
   for u in user :
       if u["verified"] :
           print(u["name"])

import csv
scores = [
["model","accuracy"],
["CNN",92],
["RNN",88],
["Transformer",97]
]
file_path = "score.csv"
with open(file_path,"w",newline = "") as file:
   writer = csv.writer(file)
   writer.writerows(scores)
  print(f"csv file {file_path} is created")
try:
   with open(file_path,"r",newline = "") as file:
      reader = csv.reader(file)
      next(reader)
      best_model = ""
      best_accuracy = 0
      for model,accuracy in reader:
        accuracy = int(accuracy)
        if accuracy > best_accuracy:
           best_accuracy = accuracy
           best_model = model
except SyntaxError:
   print("Syntax Error")

print(best_model,best_accuracy)

message = ("win money now\n  "
"hello friend\n "
"free iphone \n "
"normal text")
file_path = "messages.txt"
with open (file_path,"w",newline="")as file:
   file.write(message)
   print(f"text file {file_path} created")
with open(file_path,"r",newline="")as file:
   user = file.readlines()
   spam_txt = ""
   for u in user:
       if "win" in u or "free" in u:
           spam_txt +=u
with open ("spam.txt","w") as file:
   file.write(spam_txt)
print("spam file created")

chat bot:-
user = input("enter your message :")
file_path = "chatlog.txt"
with open(file_path,"a") as file:
   file.write(user + "\n")
try:
  with open (file_path, "r") as file:
      user = file.read()
  print(user)
  print("\n chat history :")
except FileNotFoundError:
   print("file not found :")
finally:
   print("success")


Lambda Function:---> it is a fuction used for the small opration.
list(map()):--- this is used for change all the items.
list(filter()):--- Keep matching items.
list(shorted()):--- arrange the data.

messages = [
   ("win money now", 0.95),
   ("hello friend", 0.10),
   ("free iphone", 0.90),
   ("normal text", 0.05)
]
result = list(filter(
     lambda message:message[1]> 0.80,
   messages
)
)
print(result)

pixels = [0, 128, 255, 64, 200]
result = list(map(lambda pixel: pixel/255,pixels ))
print(result)

reviews = [
   "PYTHON IS AWESOME!!!",
   "AI IS POWERFUL!!!",
   "ML IS THE FUTURE..."
]
result = list(map(lambda x: x.lower().replace("!","").replace(".",""),reviews))
print(result)

models = [
   ("CNN",92),
   ("RNN",88),
   ("Transformer",97),
   ("LSTM",90)
]
result = list(filter(lambda model:model[1]>90,models))
print(result)

models = [
   ("CNN",92),
   ("RNN",88),
   ("Transformer",97),
   ("LSTM",90)
]
result = list(sorted(models, key=lambda x: x[1], reverse=True))
print(result)

words = [
   "the",
   "python",
   "is",
   "powerful",
   "ai"
]
result = list(filter(lambda word :word not in ["the","is"],words))
print(result)
Iterators :----> it gives values when we requested one by one.
scores = [92, 88, 97, 90, 85]
it = iter(scores)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

models = [92, 88, 97, 90, 85, 99, 78]
it = iter(models)
count = 0

while True:
   try:
       value = next(it)
       if value >= 90:
         count +=1
   except StopIteration:
       break
print(count)

transactions = [500, 12000, 300, 45000, 700]
total = 0
it = iter(transactions)
while True:
   try:
       value = next(it)
       total += value
   except StopIteration:
       break
print(total)

messages = [
   "hello friend",
   "normal text",
   "win money now",
   "free iphone"
]
it = iter(messages)
while True:
   try:
       m = next(it)
       if "win" in m:
         print("win")
         break
   except StopIteration:
     break

message = "hello\n win money\n normal text\n free iphone"
file_path = "chatlog.txt"
with open(file_path,"w") as file:
   file.write(message)
   print(f"file is created: {file_path}")
with open(file_path, "r") as file:
   lines = file.readlines()
it = iter(lines)
try:
   while True:
       m = next(it)
       if "win"in m or "free" in m:
               print (m.strip())
except StopIteration:
   pass

dataset = [
   ("cat.jpg", 0),
   ("dog.jpg", 1),
   ("bird.jpg", 2)
]
it = iter(dataset)
name = []
try:
   while True:
       d = next(it)
       name.append(d[0])
except StopIteration:
   pass
print(name)

nums = [10,20]
it = iter(nums)
try:
   print(next(it))
   print(next(it))
   print(next(it))
except StopIteration:
   print("No more numbers")

models = [
   ("CNN",92),
   ("RNN",88),
   ("Transformer",97),
   ("LSTM",90)
]
it = iter(models)
best_model = next(it)
try:
   while True:
       m = next(it)
       if m[1] > best_model[1]:
           best_model = m
except StopIteration:
   pass
   print(f"{best_model} is the best model.")

result = max(models,key = lambda x: x[1])
print(result)

text = "python ai machine learning deep learning"
word = text.split()
it = iter(word)
single = 0
try:
   while True:
       print(t)
except StopIteration:
   pass

reviews = [
   "PYTHON!!!",
   "AI!!!",
   "ML..."
]
new = []
it = iter(reviews)
try:
   while True:
       t = next(it)
       result = t.replace("!","").replace(".","").lower()
       new.append(result)
except StopIteration:
   pass
print(new)

result = [r.replace("!","").replace(".","").lower()for r in reviews]
print(result)


transactions = [500,12000,300,45000,700,15000]
it = iter(transactions)
count = 0
while True:
   try:
      t = next(it)
      if t > 10000:
        count +=1
   except StopIteration:
     break
print(f"we have {count} transactions")

Genrators:-----> genrator are useful for yeilding one output at a time.  SET() IS USED TO PREVENT FROM REPEATING.
enumerate() will give us the index and the value.
   for i in range(10,51,10):
      yield i
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

models = ["CNN", "RNN", "Transformer", "LSTM"]
def gen():
   for i in models:
       yield i
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

scores = [92, 88, 97, 90, 85]
def gen(data):
       for d in data:
         if d > 90:
            yield d
g = gen(scores)
print(next(g))
print(next(g))

reviews = [
   "PYTHON!!!",
   "AI!!!",
   "ML..."
]
def gen(data):
   for r in reviews:
      cleaned = r.replace("!", "").replace(".", "").lower()
      yield cleaned
g = gen(reviews)
print(next(g))
print(next(g))
print(next(g))

import csv
rows = [
   ["CNN", "92"],
   ["RNN", "88"],
   ["Transformer", "97"],
   ["LSTM", "90"]
]
file_path = "csv.file"
def gen(file_path):
 with open (file_path,"w") as file:
     writer = csv.writer(file)
     writer.writerows(rows)
     print("file is created")
 with open(file_path,"r")as file:
   reader = csv.reader(file)

   for model,accuracy in  reader:
       yield (model,int(accuracy))
g = gen("csv.file")
print(next(g))

data = [1,2,3,4,5,6,7,8,9,10]
def gen(data,batch_size):
   i = 0
   while True:
       if i < len(data):
           yield data[i:i+batch_size]
           i +=batch_size
g = gen(data,3)
for batch in g:
   print(batch)

models = ["CNN","RNN","Transformer"]
def gen(data):
   while True:
       for m in data:
         yield m
g = gen(models)
for f in g:
   print(f)

messages = [
   "hello",
   "win money now",
   "normal text",
   "free iphone",
   "good morning"
]

def gen(data):
   for d in data:
       if "win" in d or "free" in d:
           yield d
g = gen(messages)
print(next(g))
print(next(g))

users = [
   "Aman",
   "Raj",
   "Aman",
   "Simran",
   "Raj",
   "Rohit"
]
def gen(data):
   unique = set()
   for d in data:
       if d not in unique:
           unique.add(d)
           yield d
g = gen(users)
for u in g:
   print(u)

text = """
Python is awesome.
AI is powerful.
Machine learning is the future.
"""
def gen(data):
   for line in data.split("\n"):
       for word in line.lower().replace(".","").split():
         yield word
g = gen(text)
for i in g:
   print(i)

logs = [
   "INFO: Model loaded",
   "ERROR: Dataset missing",
   "INFO: Training started",
   "ERROR: GPU unavailable"
]
def gen(data):
   for d in data:
       if "ERROR" in d:
           yield d
g = gen(logs)
for d in g:
   print(d)

scores = [90, 95, 80, 100, 85]
def gen(data):
   total = 0
   for i,d in enumerate(data,start=1):
       total +=d
       yield total/i
g = gen(scores)
for v in g:
   print(v)

data = [
   ("CNN", 92),
   ("RNN", 88),
#    ("Transformer", 97),
   ("LSTM", 90),
   ("BERT", 99),
   ("MLP", 85)
]
def gen(dis):
   batch = []
   for model,accuracy in dis:
       if accuracy >90:
           batch.append((model,accuracy/100))
           if len(batch) == 2:
               yield batch
               batch = []
g = gen(data)
for i in g:
   print(i)


scores = [92,88,97,90,85,99,78]
def filter_d(data):
   for d in data:
       if d >=90:
           yield d
def norma_lise(scores):
   for s in scores:
       yield s/100
def batch(data,size):
   batch = []
   for a in data:
       batch.append(a)
       if len(batch)==size:
           yield batch
           batch = []
   if batch:
       yield batch
g = batch(norma_lise(filter_d(scores)),2)
for i in g:
   print(i)


data = [1,2,3,4,5,6]

def gen(num,size):
   for i in range(len(data)-size + 1):
       yield num[i:i + size]
       i += size
g = gen(data,2)
for e in g:
   print(e)

data = [10, 20, 30, 40, 50]
def gen(num,size):
   for i in range(len(num)-size+1):
       yield num[i:i+size]
g = gen(data,2)
for x in g:
   print(x)


data = [
   ("CNN",92),
   ("RNN",88),
   ("Transformer",97),
   ("LSTM",90),
   ("BERT",99),
   ("MLP",85)
]
def filter(data):
   for model,accuracy in data:
       if accuracy >90:
           yield (model,accuracy)
def normalize(data):
   for model,accuracy in data:
       yield(model,accuracy/100)
def sorted_v(data):
   sorted_data = sorted(data, key =lambda x : x[1],reverse=True)
   for i in sorted_data:
       yield i
def top_n(data,n):
   count = 0
   for item in data:
       if count < n:
           yield item
           count += 1
       else:
           break
g = top_n(sorted_v(normalize(filter(data))),2)
for i in g:
   print(i)
