Classes & Objects
Constructors (__init__)
ethods
Inheritance
super()
Method Overriding
Encapsulation
Polymorphism
Composition
Static Methods
Class Methods
Property Decorators
Magic Methods (__str__, __len__, __getitem__, __call__)
Abstraction
Abstract Base Classes (ABC)
Multiple Inheritance
Method Resolution Order (MRO)

Class and Objects
class Student:
   pass
s1 = Student()
s2 = Student()
s1.name = "Aman"
s1.age =23
s2.name = "rishabh"
s2.age = 25
print(s1.name,s1.age)
print(s2.name,s2.age)

class Car:
   pass
car1 = Car()
car2 = Car()
car1.brand = "BMW"
car1.speed = "300/h"
car2.brand = "TESLA"
car2.speed = "200/h"
print(car1.brand,car1.speed)
print(car2.brand,car2.speed)

class Model:
   pass
m1 = Model()
m2 = Model()
m3 = Model()
m1.name = "RNN"
m1.accuracy = 89
m2.name = "CNN"
m2.accuracy = 78
m3.name = "Transformer"
m3.accuracy = 73
print(m1.name, m1.accuracy)
print(m2.name, m2.accuracy)
print(m3.name,m3.accuracy)

class Employee:
   pass
e1 = Employee()
e2 = Employee()
e1.name = "Aman"
e1.salary = "8000$/month"
e1.department = "Ai engeniar"
e2.name = "rishi"
e2.salary = "90000/month"
e2.department = "Ai engeniear"
print(e1.name,e1.salary,e1.department)
print(e2.name,e2.salary,e2.department)

class Model:
   pass

CNN = Model()
RNN = Model()
Transformer = Model()
LSTM = Model()
BERT = Model()
model = [CNN, RNN, Transformer, LSTM, BERT]
for m in model:
    m.name = None
    m.accuracy = None

CNN.name = "CNN"
CNN.accuracy = 92
RNN.name = "RNN"
RNN.accuracy = 88
Transformer.name = "Transformer"
Transformer.accuracy = 97
LSTM.name = "LSTM"
LSTM.accuracy = 90
BERT.name = "BERT"
BERT.accuracy = 99
for m in model:
   print(m.name, m.accuracy)

class Book:
   pass
book1 = Book()
book2 = Book()
book3 = Book()
books = [book1, book2, book3]

book1.title = "harrry"
book1.author = "me"
book1.pages = 90
book2.title = "swami"
book2.author = "vivekananda"
book2.pages = 100
book3.title = "romw"
book3.author = "she"
book3.pages = 50
max_book = max([book.pages for book in books])
print(max_book)
max_book = max(books,key = lambda b:b.pages)
print(max_book.pages, max_book.author, max_book.title)

max_pages = 0
for book in books:
   if book.pages > max_pages:
      max_pages = book.pages
print("max_pages :",max_pages)

class Product:
   pass
product1 = Product()
product2 = Product()
product3 = Product()
product4 = Product()
product = [product1, product2, product3, product4]
product1.name = "Apple"
product1.price = 2000
product2.name = "hp"
product2.price = 200
product3.name = "charger"
product3.price = 30
product4.name = "TV"
product4.price = 3000
result = list(filter(lambda x : x.price>1000,product))
for p in result:
   print(p.name,p.price)

INIT constructer :---> its job is to intialise the object with data.
class Employee:
   def __init__(self,name,salary,department):
       self.name = name
       self.salary = salary
       self.department = department
e1 = Employee("Aman",8000,"AI")
e2 = Employee("Rishi",9000,"ML")
print(e1.name,e1.salary,e1.department)
print(e2.name,e2.salary,e2.department)

class Book:
   def __init__(self,title,author,pages):
       self.title = title
       self.author = author
       self.pages = pages
b1 = Book("swami","vivekananda",200)
b2 = Book("Ram","aman",800)
b3 = Book("vidya","Rishabh",300)
book = [b1,b2,b3]
all = [(b.title,b.author,b.pages) for b in book]
print(all)

all_book =list(map(lambda b : (b.title,b.author,b.pages),book))
print(all_book)

for b in book:
   print(b.title,b.author,b.pages)

class Dataset:

   def __init__(self,name,samples,classes):
       self.name = name
       self.samples = samples
       self.classes = classes
d1 = Dataset("MONIST",51000,34)
d2 = Dataset("CIFAR10",90000,45)
d3 = Dataset("ImageNet",40000,69)
data = [d1,d2,d3]

samples_max = list(filter(lambda s : (s.samples > 50000),data))
print(samples_max)

for d in data:
   if d.samples >50000:
       print(d.name,d.samples,d.classes)

max_samples = [ d for d in data if d.samples >50000]
for d in max_samples:
   print(d.name,d.samples,d.classes)


class Employee:
   def __init__(self,name,salary,department):
       self.name = name
       self.salary = salary
       self.department = department
e1 = Employee("aman",8000,"Ai")
e2 = Employee("rishabh",7100,"GST")
e3 = Employee("Anuj",5000,"police")
e4 = Employee("guglu",7000,"shop")
e5 = Employee("tarun",6000,"army")
employee = [e1,e2,e3,e4,e5]
result = list(filter(lambda e : e.salary > 7000,employee))
for r in result:
   print(r.name,r.salary,r.department)

class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self .accuracy = accuracy
m1 = Model("CNN",92)
m2 = Model("RNN",88)
m3 = Model("Transformer",97)
m4 = Model("LSTM",90)
m5 = Model("BERT",99)
model = [m1,m2,m3,m4,m5]
max_accuracy = max(model,key=lambda m:m.accuracy)
print(max_accuracy.name,max_accuracy.accuracy)


class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
m1 = Model("CNN",92)
m2 = Model("RNN",88)
3 = Model("Transformer",97)
m4 = Model("LSTM",90)
m5 = Model("BERT",99)
model = [m1,m2,m3,m4,m5]
total_accuracy = 0
for m in model:
   total_accuracy +=m.accuracy
total_model = len(model)
result = total_accuracy/total_model
rint("Accuracy:",result)

class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
m1 = Model("CNN",92)
m2 = Model("RNN",88)
m3 = Model("Transformer",97)
m4 = Model("LSTM",90)
m5 = Model("BERT",99)
model = [m1,m2,m3,m4,m5]
result = sorted(model,key=lambda x:x.accuracy,reverse=True)
for m in result:
   print(m.name,m.accuracy)

class Model:
   def __init__(self,name,accuracy,framework):
       self.name = name
       self.accuracy = accuracy
       self.framework = framework
m1 = Model("CNN",92,"done")
m2 = Model("RNN",88,"done")
m3 = Model("Transformer",97,"done")
m4 = Model("LSTM",90,"done")
m5 = Model("BERT",99,"done")
m6 = Model("DNN",56,"done")
m7 = Model("ZNN",67,"done")
m8 = Model("GNN",87,"done")
m9 = Model("NNN",83,"done")
m10 = Model("SNN",57,"done")
model = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
filtered = list(filter(lambda x : x.accuracy>90,model))
sorted_v = sorted(filtered, key=lambda x: x.accuracy,reverse=True)
extract = list(map(lambda x : x.name,sorted_v))
print(extract)

Instance method :---> self reffered to the current object. instance method. it work with the class of the object. it work with the data stored in the object.
class Model:
   def __init__(self,name, accuracy,epoch_trained):
       self.name = name
       self.accuracy = accuracy
       self.epoch_trained = epoch_trained
   def train(self,epochs):
       self.accuracy += epochs * 0.5
       self.epoch_trained += epochs

   def is_good(self):
       return self.accuracy >90

   def show(self):
       print(self.name,self.accuracy,self.epoch_trained)
m1 = Model("CNN",99,78)
m1.train(6)

m2 = Model("RNN",91,56)
m2.train(12)
m3 = Model("Transformers",78,89)
m3.train(12)

m1.show()
print(m1.is_good())
m2.show()
print(m2.is_good())
m3.show()
print(m3.is_good())


class Model:
   def __init__(self,name,accuracy):
      self.name = name
       self.accuracy = accuracy
   def compare(self,other_model):
       if self.accuracy > other_model.accuracy:
           return "self is better"
       elif self.accuracy < other_model.accuracy:
           return "other model is better"
       else:
           return "equal performance"

   def show(self):
       print(self.name,self.accuracy)
m1 = Model("CNN",90)
m2 = Model("Rnn",85)

m1.show()
m2.show()
print(m1.compare(m2))

class Model:
   def __init__(self,name , accuracy):
       self.name = name
       self.accuracy = accuracy

   def show(self):
       print(self.name,self.accuracy)
class ModelBatch:
   def __init__(self,models):
       self.models = models

   def train_all(self,boost):
       for model in self.models:
           model.accuracy += boost

   def best_model(self):
       return max(self.models,key=lambda m : m.accuracy)

   def average_accuracy(self):
       total = 0
       for model in self.models:
           total += model.accuracy
       return total/len(self.models)

   def show_all(self):
        for model in self.models:
            model.show()

m1 = Model("CNN",92)
m2 = Model("RNN",97)
m3 = Model("Transformers",99)
m4 = Model("LSTM",100)
batch = ModelBatch([m1,m2,m3,m4])
print("before Training")
batch.show_all()
batch.train_all(5)
print("\nafter Training")
batch.show_all()
best = batch.best_model()
print("\n best model")
print(best.name,best.accuracy)
print("\n Avrage accuracy")
print(batch.average_accuracy())


class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy

   def merge(self,other_model):
       new_name = self.name+ "+" + other_model.name
       new_accuracy = (self.accuracy + other_model.accuracy)/2
       return Model(new_name,new_accuracy)
   def show(self):
       print(self.name,self.accuracy)
m1 = Model("CNN",92)
m2 = Model("RNN",88)
m3 = m1.merge(m2)
m1.show()
m2.show()
m3.show()

class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
   def compete(self,other_model):
       if self.accuracy > other_model.accuracy:
           self.accuracy +=1
           other_model.accuracy -=1
       elif self.accuracy<other_model.accuracy:
               other_model.accuracy +=1
               self.accuracy -=1
       else:
           pass

   def show(self):
       print(self.name,self.accuracy)

m1 = Model("CNN",92)
m2 = Model("RNN",88)
print("before completion")
m1.show()
m2.show()
print("after completion")
m1.compete(m2)
m1.show()
m2.show()

import random
class Models:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
   def show(self):
       print(self.name,self.accuracy)
class CompetitionSystem:
   def __init__(self,models):
       self.models = models
   def compete_round(self):
       for i in range(len(self.models)):
           model1 = self.models[i]
           model2 = random.choice(self.models)
          if model1 != model2:
             if model1.accuracy > model2.accuracy:
               model1.accuracy +=1
               model2.accuracy -=1
             elif model1.accuracy < model2.accuracy:
               model2.accuracy +=1
               model1.accuracy -=1
             else:
               pass
#    def ranking(self):
       return sorted(self.models,key=lambda x:x.accuracy,reverse=True)
#    def champion(self):
       return max(self.models,key= lambda m: m.accuracy)
   def show_all(self):
       for m in self.models:
           m.show()

m1 = Models("CNN",92)
m2 = Models("RNN",88)
m3 = Models("Transformers",97)
m4 = Models("LSTM",93)
system = CompetitionSystem([m1,m2,m3,m4])
print("before completion")
m1.show()
m2.show()
m3.show()
m4.show()
system.compete_round()
print("after competition")
#m1.show()
m2.show()
m3.show()
m4.show()
print("\n Ranking")
for m in system.ranking():
   print(m.name,m.accuracy)
print("\n Champion")
best = system.champion()
print(best.name,best.accuracy)

Inheritence:----> child class get properties from the parent class. means reuse the propeties of the parent class

class Employee:
   def __init__(self,name,salary):
       self.name = name
       self.salary = salary
   def show(self):
       print(self.name,self.salary)
class AIEngineer(Employee):
   pass
e1 = AIEngineer("Aman",8000000)
1.show()


class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
   def evaluate(self):
       print(self.name,self.accuracy)
class CNN(Model):
   pass
class RNN(Model):
   pass
class Transformer(Model):
   pass
cnn = CNN("CNN",92)
rnn = RNN("RNN",88)
t =   Transformer("Transformer",97)
cnn.evaluate()
rnn.evaluate()
t.evaluate()

class Dataset:
   def __init__(self,name,samples):
       self.name = name
       self.samples = samples
   def is_large(self):
       if self.samples > 50000:
           return "Large dataset"
       else:
           return "Small dataset"
   def show(self):
       print(self.name,self.samples)
class ImageDataset(Dataset):
   pass
class TextDataset(Dataset):
   pass
class AudioDataset(Dataset):
   pass
d1 =ImageDataset("ImageNet",10000)
d2 = TextDataset("WikiText",30000)
d3 = AudioDataset("AudioSet",70000)
d1.show()
d2.show()
d3.show()

print(d1.is_large())
print(d2.is_large())
print(d3.is_large())

class Model:
   def __init__(self,name,accuracy,epoch):
       self.name = name
       self.accuracy = accuracy
       self.epoch = epoch
   def show(self):
       print(self.name,self.accuracy,self.epoch)
   def train(self,boost):
       self.accuracy += boost
       return self.accuracy
class CNN(Model):
   pass
class RNN(Model):
   pass
class Transformer(Model):
   pass
cnn =CNN("CNN",92,1)
rnn = RNN("RNN",88,1)
t = Transformer("Transformer",97,1)
print("before")
cnn.show()
rnn.show()
t.show()
print(" after Train")
print(cnn.train(3))
print(rnn.train(3))
print(t.train(3))


class Employee:
   def __init__(self,name,salary):
       self.name = name
       self.salary = salary
   def show(self):
       print(self.name,self.salary)
   def bonus(self):
       self.salary +=self.salary*0.10
class AIEngineer(Employee):
   pass
class DataScientist(Employee):
   pass
class MLEngineer(Employee):
   pass
class ResearchScientist(Employee):
   pass
e1 = AIEngineer("AMAn",80000)
e2 = DataScientist("rishi",54000)
e3 = MLEngineer("ram",70000)
e4 = ResearchScientist("Krishna",59000)
employees = [e1,e2,e3,e4]
print("before Bonus")
for e in employees:
   e.show()
for e in employees:
   e.bonus()
print("after Bonus")
for e in employees:
   e.show()
print("highest salary")
highest_salary_employee =max(employees,key = lambda x:x.salary)
print(highest_salary_employee.name,highest_salary_employee.salary)


class Participant:

   def __init__(self, name,score):
       self.name = name
       self.score = score
   def show(self):
       print(self.name,self.score)

   def update_score(self,points):
       self.score += points
class Beginner(Participant):
   pass
class Intermediate(Participant):
   pass
class Expert(Participant):
   pass
class GrandMaster(Participant):
   pass
p1 =Beginner("Aman",23)
p2 = Beginner("Rishabh",25)
p3 = Intermediate("Ram",30)
p4 = Intermediate("Narayan",30)
p5 = Expert("Prince",60)
p6 = Expert("rishi",78)
p7 = GrandMaster("Shiva",99)
p8 = GrandMaster("Durga",101)
God = [p1,p2,p3,p4,p5,p6,p7,p8]
print("BEFORE")
for g in God:
   g.show()
print("updated points")
for g in God:
   g.update_score(3)
print("AFTER update")
for g in God:
   g.show()

leaderboard = list(sorted(God, key = lambda x:x.score, reverse = True))

for g in leaderboard:
 print(g.name,g.score)

class Dataset:
   def __init__(self,name,samples,classes):
       self.name = name
       self.samples = samples
       self.classes = classes
   def show(self):
       print(self.name,self.samples,self.classes)
   def is_large(self):
       if self.samples >100:
           return "Large dataset"
       else:
           return "Small dataset"
class ImageDataset(Dataset):
   pass
class TextDataset(Dataset):
   pass
class AudioDataset(Dataset):
   pass
class VideoDataset(Dataset):
   pass
d1 = ImageDataset("CNN",201,3)
d2 = ImageDataset("Rnn",100,3)
d3 = TextDataset("Transformer",301,4)
d4 = TextDataset("CNN",100,5)
d5 = AudioDataset("brod",300,7)
d6 = AudioDataset("CNN",200,4)
d7 = AudioDataset("RNN",100,2)
d8 = VideoDataset("Transformer",90,5)
d9 = VideoDataset("brod",21,3)
d10 = VideoDataset("CNN",390,5)
data = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
print("LArge DATASET")
for d in data:
   d.is_large()
   print(d.is_large())
print("MAXIMUM SAMPLES")

result = max(data,key=lambda x: x.samples)
print(result.name,result.samples)
print("AVERAGE SAMPLES")
total = 0
for d in data:
   total +=d.samples
   print(total/len(data))
print("SORT BY SAMPLES")
results = sorted(data,key = lambda x : x.samples)
for d in results:
  print(d.name,d.samples)

print("PRINT ONLY NAME")
final = list(map(lambda x : x.name,data))
print(final)

Method Overriding:----> child class instead of using method of parent class it implement its own.
class Employee:
   def __init__(self,name):
       self.name = name
   def show(self):
       print(self.name)
   def work(self):
       print("Employees are working")
class AIEngineer(Employee):

   def work(self):
       print("AIEngineer is building AI Model")

class DataScientist(Employee):

   def work(self):
       print("DataScientist is analysing data")
a1 = AIEngineer("AMan")
d2 = DataScientist("Man")
a1.work()
d2.work()

class Model:
   def __init__(self,name,accuracy):
       self.name = name
   def train(self):
       print("Training genric model")
   def evaluate(self):
       print("Evaluating genric model")
   def show(self):
       print(self.name,self.accuracy)
class CNN(Model):
   def train(self):
       print("Training CNN with convolutional layer")
   def evaluate(self):
       print("Evaluating CNN accuracy")
class RNN(Model):
   def train(self):
       print("Training RNN with sequential data")
   def evaluate(self):
       print("Evaluating Rnn accuracy")
class Transformer(Model):
   def train(self):
       print("Training transformer with attention mechanism")
   def evaluate(self):
       print("Evaluating transformer accuracy")
class GAN(Model):
   def train(self):
       print("Training Gan generator and discriminator")
   def evaluate(self):
       print("Evaluating gan quality")
class BERT(Model):
   def train(self):
     print("Training BErt on NLP corpus")
   def evaluate(self):
       print("Evaluating BERT language understanding")
cnn = CNN("CNN",92)

rnn = RNN("RNN",88)

transformer = Transformer("Transformer",97)

gan = GAN("GAN",85)

bert = BERT("BERT",99)
models = [cnn,rnn,transformer,gan,BERT]
for m in models:
   m.train()
   m.evaluate()

class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
   def deploy(self):
       print("Deploying genric Model...")
   def predict(self):
       print("Making genric predictions")
   def show(self):
       print(self.name,self.accuracy)
class CNN(Model):

   def deploy(self):
       print("Deploying CNN on image server...")
   def predict(self):
       print("predicting image class")

class Transformer(Model):
   def deploy(self):
       print("Deploying transformer on Nlp ...")
   def predict(self):
       print("Predicting text output")
class RecommendationModel(Model):
   def deploy(self):
       print("Deploying Recommendation engin...")
   def predict(self):
       print("Generating product recommendations")
class FraudDetectionModel(Model):
   def deploy(self):
     print("Deploying Fraud detection Service")
   def predict(self):
       print("Detecting Fraudulent Transection")
cnn = CNN("CNN",92)

transformer = Transformer("BERT",97)

rec = RecommendationModel("AmazonRec",95)

fraud = FraudDetectionModel("FraudNet",99)
model = [cnn,transformer,rec,fraud]
for m in model:
   m.deploy()
   m.predict()
print("BEST MODEL")
bestModel = max(model,key= lambda x:x.accuracy)
print(bestModel.name,bestModel.accuracy)

print("SORT DESCENDING")
sortModel = sorted(model,key = lambda x: x.accuracy,reverse = True)
for s in sortModel:
   print(s.name,s.accuracy)

print("ONLY NAMES")
onlyName = list(map(lambda x:x.name,model))
for b in onlyName:
   print(b)

SUPER():----> it use the parent class behaviour instead of replacing it.
class Employee:
   def __init__(self,name,salary):
       self.name = name
       self.salary = salary
   def work(self):
       print("Working")
   def show(self):
       print(self.name,self.salary)
class AIEngineer(Employee):
   def work(self):
       super().work()
       print("AIEngineer")
n1 = AIEngineer("Nick",5000)

n1.show()
n1.work()

class Model:

   def train(self):
       print("Training...")
class CNN(Model):
   def train(self):
       super().train()
       print("Training new data...")
cnn = CNN()
cnn.train()

class Dataset:
   def load(self):
       print("loading dataset")
class ImageDataset(Dataset):
   def load(self):
       super().load()
       print("add image processing ")
im = ImageDataset()
im.load()

class Trainer:
   def load_data(self):
       print("Loading data...")
   def setup_model(self):
       print("Setting up model...")
   def train(self):
       print("Training base model...")
   def save_checkpoint(self):
       print("Saving model...")
class CNNTrainer(Trainer):
   def load_data(self):
       super().load_data()
       print("Loading CNN data...")
   def setup_model(self):
       super().setup_model()
       print("Setting up CNN model...")
   def train(self):
       super().train()
       print("Training CNN model...")
   def save_checkpoint(self):
       super().save_checkpoint()
       print("Saving CNN model...")
class TransformerTrainer(Trainer):
   def load_data(self):
       super().load_data()
       print("Loading transformer data")
  def setup_model(self):
       super().setup_model()
       print("setting up the transformer model")
   def train(self):
       super().train()
       print("Training transformer model...")
   def save_checkpoint(self):
       super().save_checkpoint()
#        print("Saving transformer model...")
class LLMTrainer(Trainer):
   def load_data(self):
       super().load_data()
       print("Loading LLM data...")
   def setup_model(self):
       super().setup_model()
       print("Setting up LLM model...")
   def train(self):
       super().train()
       print("Training LLM model...")
   def save_checkpoint(self):
       super().save_checkpoint()
       print("Saving LLM model...")
cnn = CNNTrainer()
tran = TransformerTrainer()
#llm = LLMTrainer()
model = [cnn, tran, llm]
for d in model:
   d.load_data()
   d.setup_model()
   d.train()
   d.save_checkpoint()


class BaseLLM:
   def __init__(self,model_name,parameters,accuracy):
       self.model_name = model_name
       self.parameters = parameters
       self.accuracy = accuracy
   def authenticate(self):
       print("authenticating in progress")
   def load_model(self):
       print("loading model")
   def generate(self):
       print("Genrating the genric response")
   def show(self):
       print(self.model_name,self.parameters,self.accuracy)
class GPT4(BaseLLM):
  def load_model(self):
       super().load_model()
       print("Loading GPT-4 language model")
  def generate(self):
       super().generate()
       print("Genrateing the GPT-4 language model")
class Claude(BaseLLM):
   def __init__(self,model_name,parameters,accuracy,context_window):
     super().__init__(model_name,parameters,accuracy)
      self.context_window = context_window
   def load_model(self):
       super().load_model()
       print("loading claude architecture")
   def generate(self):
       super().generate()
       print("Generating claude model")
   def show(self):
       super().show()
       print(self.context_window)
class Gemini(BaseLLM):
   def __init__(self,model_name,parameters,accuracy,multimodel_support):
       super().__init__(model_name,parameters,accuracy)
       self.multimodel_support = multimodel_support
   def load_model(self):
       super().load_model()
       print("Loading Gemini model")
   def generate(self):
       super().generate()
       print("Generating Gemini model")
   def show(self):
       super().show()
       print(self.multimodel_support)
gpt = GPT4("GPT-4",1800000000,98)
claude = Claude("CLAUDE-4",1300000000,97,200000)
gemini = Gemini("GEMINI-4",1800000000,96,True)
#model = [gpt,claude,gemini]
for m in model:
   m.authenticate()
   m.load_model()
   m.generate()
   m.show()

Abstect Base class:----->
from abc import ABC, abstractmethod
class BaseModel(ABC):
   @abstractmethod
   def train(self):
       pass
   @abstractmethod
   def predict(self):
       pass
class CNN(BaseModel):
   def train(self):
       print("Training the CNN")
   def predict(self):
       print("Pridicting the CNN")
class Transformer(BaseModel):
   def train(self):
       print("Training the Transformers")
   def predict(self):
       print("Predicting the transformers")
cnn = CNN()
t = Transformer()
cnn.train()
cnn.predict()
t.train()
t.predict()

from abc import ABC,abstractmethod
class Trainer(ABC):
   def __init__(self,model_name,dataset_name,accuracy,epochs):
       self.model_name = model_name
       self.dataset_name = dataset_name
       self.accuracy = accuracy
       self.epochs = epochs
   @abstractmethod
   def load_data(self):
       pass
   @abstractmethod
   def setup_model(self):
       pass
   @abstractmethod
   def train(self):
       pass
   @abstractmethod
   def save_checkpoint(self):
       pass
class CNNTrainer(Trainer):
   def load_data(self):
      print("Loading CNN data...")
  def setup_model(self):
      print("Setting up CNN model...")
   def train(self):
       print("Training CNN model...")
   def save_checkpoint(self):
       print("Saving model...")
class TransformerTrainer(Trainer):
   def load_data(self):
       print("Loading transformer data....")
   def setup_model(self):
       print("setting up transformer model...")
   def train(self):
       print("Training transformer model...")
   def save_checkpoint(self):
       print("saving the transformer model....")
class LLMTrainer(Trainer):
   def load_data(self):
       print("Loading LLM data...")
   def setup_model(self):
       print("Setting up LLM model...")
   def train(self):
       print("Training LLM model...")
   def save_checkpoint(self):
       print("saving the LLM model...")
cnn = CNNTrainer("CNN","CNNTrainer",96,2)
trn = TransformerTrainer("Transformer","TransformerTrainer",95,3)
llm = LLMTrainer("LLm","LLMTrainer",99,4)
models = [cnn,trn,llm]
for m in models:
   m.load_data()
   m.setup_model()
   m.train()
   m.save_checkpoint()
best_model = max(models, key = lambda x : x.accuracy)
print(best_model.model_name,best_model.accuracy)


from abc import ABC, abstractmethod
class VehicleAI(ABC):
   def __init__(self,vehicle_name,sensor_count,response_time,safety_score):
       self.vehicle_name = vehicle_name
       self.sensor_count = sensor_count
       self.response_time = response_time
       self.safety_score = safety_score
   @abstractmethod
   def detect_obstacle(self):
       pass
   @abstractmethod
   def make_decision(self):
#        pass
   @abstractmethod
   def generate_drive_report(self):
       pass
class TeslaAi(VehicleAI):
   def __init__(self,vehicle_name,sensor_count,response_time,safety_score,camera_resolution):
       super().__init__(vehicle_name,sensor_count,response_time,safety_score)
       self.camera_resolution = camera_resolution
   def detect_obstacle(self):
#        print("detecting the obstacle")
   def make_decision(self):
       print("making the decision")
   def generate_drive_report(self):
       print("making the drive_report")
class WaymoAI(VehicleAI):
   def __init__(self,vehicle_name,sensor_count,response_time,safety_score,lidar_count):
       super().__init__(vehicle_name,sensor_count,response_time,safety_score)
       self.lidar_count = lidar_count
#    def detect_obstacle(self):
       print("Detecting the Waymo obstacle")
   def make_decision(self):
       print("waymo making the decision")
   def generate_drive_report(self):
       print("Waymo making the drive_report")
class CruiseAI(VehicleAI):
   def __init__(self,vehicle_name,sensor_count,response_time,safety_score,Pedestrain_detection_accuracy):
       super().__init__(vehicle_name,sensor_count,response_time,safety_score)
       self.pedestrain_detection_accuracy = Pedestrain_detection_accuracy
   def detect_obstacle(self):
       print("Cruise detected")
   def make_decision(self):
       print("Cruise making the decision")
   def generate_drive_report(self):
       print("Cruise making the drive_report")
tesla = TeslaAi("TESLA9",46,99,90,97)
waymo = WaymoAI("Waymo",44,98,95,93)
cruise = CruiseAI("Cruise",46,97,94,99)
tesla.generate_drive_report()
waymo.generate_drive_report()
cruise.generate_drive_report()
all = [tesla,waymo,cruise]
#safest_AI =max(all,key = lambda x:x.safety_score)
print(safest_AI.vehicle_name,safest_AI.safety_score)
fastest = min(all,key = lambda x:x.response_time)
print(fastest.vehicle_name,fastest.response_time)

from abc import ABC, abstractmethod
class ProductionModel(ABC):
   def __init__(self,model_name,version,accuracy,
                latency_ms,request_served,error_rate):
       self.model_name = model_name
       self.version = version
       self.accuracy = accuracy
       self.request_served = request_served
       self.latency_ms = latency_ms
       self.error_rate = error_rate

   @abstractmethod
   def collect_metrics(self):
       pass
   @abstractmethod
   def analyze_performance(self):
       pass
   @abstractmethod
   def take_action(self):
       pass
   @abstractmethod
#    def generate_report(self):
       pass
class GPTProdution(ProductionModel):
   def __init__(self,model_name,version,accuracy,latency_ms,request_served,error_rate,tokens_processed,context_window):
       super().__init__(model_name,version,accuracy,latency_ms,request_served,error_rate)
       self.tokens_processed = tokens_processed
       self.context_window = context_window
   def collect_metrics(self):
       self.request_served +=2000
       self.tokens_processed+=20400
       self.latency_ms += 50
       self.average = (self.tokens_processed
                       / self.request_served)
   def analyze_performance(self):
       if self.latency_ms > 250:
           self.status = "HIgh latency"
       else:
          self.status = "Healthy"
   def take_action(self):
       if self.status == "HIgh latency":
           self.action = "Scale GPU servers"
       else:
           self.action = "no action required"
   def generate_report(self):
       print(
           f"model name : {self.model_name}"
           f"Version : {self.version}"
           f"Request_served:{self.request_served}"
           f"average :{self.average}"
           f"tokens {self.tokens_processed}"
           f"Latency : {self.latency_ms}"
           f"status : {self.status}"
           f"action : {self.action}"
       )
class VisionProduction(ProductionModel):
   def __init__(self,model_name,version,accuracy,latency_ms,request_served,error_rate,image_processed,camera_count):
       super().__init__(model_name,version,accuracy,latency_ms,request_served,error_rate)
       self.image_processed = image_processed
       self.camera_count = camera_count
   def collect_metrics(self):
       self.image_processed += 2000
       self.camera_count+=1300
       self.error_rate +=1.2
       self.image_per_camera = (self.image_processed / self.camera_count)

   def analyze_performance(self):
      if self.error_rate > 3:
           self.status = "Vision failure risk"
       else:
           self.status = "Healthy"
   def take_action(self):
       if self.status == "Vision failure risk":
           self.action = "restart vision pipeline"
       else:
           self.action = "no action required"
   def generate_report(self):
       print(
           f"model name : {self.model_name}"
           f"Version : {self.version}"
           f"Request_served:{self.image_processed}"
           f"image camera : {self.image_per_camera}"
           f"status : {self.error_rate}"
           f"action : {self.action}"
           f"status : {self.status}"
       )
class RecommendationProduction(ProductionModel):
   def __init__(self,model_name,version,accuracy,latency_ms,request_served,error_rate,click_through_rate,product_recommended):
       super().__init__(model_name,version,accuracy,latency_ms,request_served,error_rate)
       self.click_through_rate = click_through_rate
       self.product_recommended = product_recommended
   def collect_metrics(self):
       self.request_served +=1500
       self.product_recommended +=2000
   def analyze_performance(self):
           self.status = "ctu failure risk"
       else:
           self.status = "Healthy"
   def take_action(self):
       if self.status == "ctu failure risk":
           self.action = "Retain recommendation model"
       else:
           self.action = "no action required"

   def generate_report(self):

       print(
           f"Model Name : {self.model_name}\n"
           f"Version : {self.version}\n"
           f"Accuracy : {self.accuracy}\n"
           f"Requests : {self.request_served}\n"
           f"CTR : {self.click_through_rate}\n"
           f"Products : {self.product_recommended}\n"
           f"Status : {self.status}\n"
           f"Action : {self.action}"
       )
gpt = GPTProdution("GPT",3.89,90,56,500,2.4,2000,340)
vision = VisionProduction("VISION",4.67,93,78,2000,3.45,3000,4000)
reco = RecommendationProduction("RECOMENDATION",5.78,96,56,3000,3.4,2000,3000)
model = [gpt,vision,reco]
for m in model:
   m.collect_metrics()
   m.analyze_performance()
   m.take_action()
   m.generate_report()
best_accuracy = max(model,key=lambda x:x.accuracy)
low_latency = min(model,key=lambda x:x.latency_ms)
most_request = max(model,key=lambda x:x.request_served)
leaderboard = list(sorted(model,key=lambda x:x.accuracy,reverse = True))
print(best_accuracy.model_name,best_accuracy.accuracy)
print(low_latency.model_name,low_latency.accuracy)
print(most_request.model_name,most_request.request_served)
for rank,models in enumerate(leaderboard,start = 1):
   print(rank,models.model_name,models.accuracy)

from abc import ABC, abstractmethod
#class HealthcareAI(ABC):
   def __init__(self,model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage):
       self.model_name = model_name
#        self.version = version
       self.accuracy = accuracy
       self.patients_monitored = patients_monitored
       self.response_time_ms = response_time_ms
       self.uptime_percentage = uptime_percentage
   @abstractmethod
#    def collect_patient_data(self):
#        pass
   @abstractmethod
   def analyze_health(self):
#        pass
   @abstractmethod
   def send_alert(self):
       pass
   @abstractmethod
   def generate_report(self):
      pass

class HeartDiseaseAI(HealthcareAI):
   def __init__(self,model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage,ecg_signals_processed,heart_attack_prediction):
       super().__init__(model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage)
       self.ecg_signals_processed = ecg_signals_processed
       self.heart_attack_prediction = heart_attack_prediction
   def collect_patient_data(self):
       self.patients_monitored +=300
       self.ecg_signals_processed +=1000
       self.signals_per_patient = (self.ecg_signals_processed
                                   / self.patients_monitored)
   def analyze_health(self):
       if self.accuracy < 95 :
           self.status = "Needs Retraining"
       else:
           self.status = "Healthy"
   def send_alert(self):
       if self.status == "Needs Retraining":
           self.action = 'Notify AI operations Team'
       else:
           self.action = "Continue Monitoring"

   def generate_report(self):
       print(f"model name : {self.model_name}\n"
             f"version : {self.version}\n"
             f"accuracy : {self.accuracy}\n"
             f"signals per patients : {self.signals_per_patient}\n"
             f"status : {self.status}\n"
#              f"uptime : {self.uptime_percentage}\n"
             f"action : {self.action}\n"
             f"response time : {self.response_time_ms}\n"
             f" patients monitored : {self.patients_monitored}\n")

class CancerDetectionAI(HealthcareAI):
   def __init__(self,model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage,scans_processed,tumors_detected):
       super().__init__(model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage)
       self.scans_processed = scans_processed
       self.tumors_detected = tumors_detected
   def collect_patient_data(self):
       self.scans_processed += 245
       self.tumors_detected +=564
       self.tumor_detection_rate = (self.tumors_detected /
                                    self.scans_processed)
   def analyze_health(self):
       if self.response_time_ms >250:
           self.status = "Slow Response"
       else:
           self.status = "Healthy"
   def send_alert(self):
       if self.status == "Slow Response":
           self.action = "Scale GPU cluster"
       else:
           self.action = "system stable"
   def generate_report(self):
       print(f"model name : {self.model_name}\n"
             f"version : {self.version}\n"
             f"accuracy : {self.accuracy}\n"
#              f"tumor detection rate : {self.tumor_detection_rate}\n"
             f"status : {self.status}\n"
             f"uptime : {self.uptime_percentage}\n"
             f"action : {self.action}\n"
             f"response time : {self.response_time_ms}\n"
             f" patients monitored : {self.patients_monitored}\n")#

class ICUAssistantAI(HealthcareAI):
   def __init__(self,model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage,vital_signals_processed,emergency_cases_detected):
       super().__init__(model_name,version,accuracy,patients_monitored,response_time_ms,uptime_percentage)
       self.vital_signals_processed = vital_signals_processed
       self.emergency_cases_detected = emergency_cases_detected
   def collect_patient_data(self):
       self.patients_monitored +=354
       self.emergency_cases_detected +=578
       self.cases_per_patient = (self.emergency_cases_detected /self.patients_monitored)

   def analyze_health(self):
       if self.uptime_percentage < 99:
           self.status = "Critical downtime"
       else:
           self.status = "Healthy"
   def send_alert(self):
       if self.status == "Critical downtime":
           self.action = "Restart Monitoring Services"
       else:
           self.action = "Continue Monitoring"#

   def generate_report(self):
       print(f"model name : {self.model_name}\n"
             f"version : {self.version}\n"
             f"accuracy : {self.accuracy}\n"
             f"cases per second : {self.cases_per_patient}\n"
             f"status : {self.status}\n"
             f"action : {self.action}\n"
             f"uptime : {self.uptime_percentage}\n"
             f"response time : {self.response_time_ms}\n"
             f" patients monitored : {self.patients_monitored}\n")
hert = HeartDiseaseAI("HEart diesease","HD3.4",94,400,245,45,34,43)
#cancer = CancerDetectionAI("CANCEr","CR 4.4",96,566,342,54,34,38)
icu = ICUAssistantAI("ICU","icu4.7",99,432,345,332,32,43)
model=[hert,cancer,icu]
for m in model:
   m.collect_patient_data()
   m.analyze_health()
   m.send_alert()
   m.generate_report()
#Best_accuracy = max(model,key=lambda x : x.accuracy)
lowest_response = min(model,key=lambda x : x.response_time_ms)
highest_patients_monitored = max(model,key=lambda x : x.patients_monitored)
leaderboard = list(sorted(model,key=lambda x : x.accuracy,reverse=True))
only_model_name = list(map(lambda x : x.model_name,model))
print("Best_accuracy : ",Best_accuracy.model_name,Best_accuracy.accuracy)
print("lowest_response : ",lowest_response.model_name,lowest_response.response_time_ms)
print("highest_patient_monitored : ",highest_patients_monitored.model_name,highest_patients_monitored.patients_monitored)
print("only_model_name : ",only_model_name)
for rank ,model in enumerate(leaderboard, start = 1):
   print(rank,model.model_name,model.accuracy)

Encapsulation:---->if we want to protect the attribute or data private than we use this.
class AIModel:
   def __init__(self,model_name,accuracy):
       self.model_name = model_name
       self.__accuracy = accuracy
   def get_accuracy(self):
       return self.__accuracy
   def set_accuracy(self,new_accuracy):
       if 0 < new_accuracy < 100:
           self.__accuracy = new_accuracy
           print("Accuracy update successfully")
       else:
           print("Invalid accuracy value")

   def show(self):
       print(self.model_name,self.__accuracy)
ai = AIModel(" GPT-2.4", 98)
ai.show()
ai.set_accuracy(97)
print(ai.get_accuracy())

class Employee:
   def __init__(self,employee_name,salary):
       self.employee_name = employee_name
       self.__salary = salary
  def get_salary(self):
       return self.__salary
   def set_salary(self,new_salary):
       if 0 < new_salary :
           self.__salary = new_salary
           print("salary updated")
       else:
           print("Invalid salary")
   def show(self):
       print("Employee Name:",self.employee_name)
       print("Salary:",self.get_salary())
emp = Employee("AMan kapil",10000)
emp.show()
emp.set_salary(11000)
print(emp.get_salary())

class SecureModel:
   def __init__(self,model_name,api_key):
       self.model_name = model_name
       self.__api_key = api_key

   def verify_api_key(self,key):
       if key == self.__api_key:
           print("access granted")
       else:
           print("Invalid key")
   def change_api_key(self,old_key,new_key):
       if old_key == self.__api_key:
           self.__api_key = new_key
           print("API key updated")
       else:
           print("Invalid api key")
   def show(self):
       print("Model_name = ",self.model_name)
       print("api_key = ",self.api_key)
s = SecureModel("GEMINI","GPT4-5-3")
#s.verify_api_key("GPT4-5-3")
s.change_api_key("GPT4-5-3","CHAT 5-7-9")
s.verify_api_key("CHAT 5-7-9")

class BankAccount:
   def __init__(self,account_holder,balance):
       self.account_holder = account_holder
       self.__balance = balance
   def get_balance(self):
       return self.__balance
   def deposit(self,amount):
       if 0 < amount:
           self.__balance += amount
           print("given amount is deposited")
       else:
           print("given amount is not deposited")
   def withdraw(self,amount):
       if self.__balance < amount:
           print("insufficient funds")
       elif amount  <= 0:
           print("Invalid values")
       else:
           self.__balance -= amount
           print("given amount is withdrawn")

bank = BankAccount("Aman Kapil",10000)
print(bank.get_balance())
bank.deposit(500)
print(bank.get_balance())
bank.withdraw(3000)
bank.withdraw(14324)

class TrainingConfig:
   def __init__(self,model_name,learning_rate,batch_size):
       self.model_name = model_name
       self.__learning_rate = learning_rate
       self.__batch_size = batch_size
   def get_learning_rate(self):
       return self.__learning_rate
   def get_batch_size(self):
       return self.__batch_size
   def set_learning_rate(self,learning_rate):
       if 0 < learning_rate <= 1:
           self.__learning_rate = learning_rate
           print("this is acceptable")
       else:
           print("this is not acceptable")
   def set_batch_size(self,batch_size):
       if batch_size >= 1:
           self.__batch_size = batch_size
           print("this is valid")
       else:
           print("this is not valid")
train = TrainingConfig("CNN",0.5,56)
print(train.get_learning_rate())
print(train.get_batch_size())
train.set_learning_rate(0.0004)
train.set_batch_size(65)
print(train.get_learning_rate())
print(train.get_batch_size())

class PatientRecord:
   def __init__(self,patient_name,blood_pressure,heart_rate):
       self.patient_name = patient_name
       self.__blood_pressure = blood_pressure
       self.__heart_rate = heart_rate
   def get_blood_pressure(self):
       return self.__blood_pressure
   def get_heart_rate(self):
       return self.__heart_rate
   def set_blood_pressure(self,blood_pressure):
       if 50 < blood_pressure < 250:
           self.__blood_pressure = blood_pressure
           print("blood pressure is control")
       else:
           print("not control")
   def set_heart_rate(self,heart_rate):
       if 30 < heart_rate < 350:
           self.__heart_rate = heart_rate
           print("heart rate is control")
       else:
           print("not control")
   def show(self):
       print("patient name:",self.patient_name)
       print("blood pressure :",self.get_blood_pressure())
       print("heart rate:",self.get_heart_rate())
record = PatientRecord("Krishna",120,200)
record.show()
print(record.get_blood_pressure())
print(record.get_heart_rate())
record.set_blood_pressure(50)
record.set_heart_rate(30)

class DeploymentModel:
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,api_key):
       self.model_name = model_name
       self.version= version
       self.__accuracy = accuracy
       self.__latency_ms = latency_ms
       self.__gpu_count = gpu_count
       self.__api_key = api_key
   def get_accuracy(self):
       return self.__accuracy
   def get_latency_ms(self):
       return self.__latency_ms
   def get_gpu_count(self):
       return self.__gpu_count
   def set_accuracy(self,new_accuracy):
       if 0 < new_accuracy < 100:
           self.__accuracy = new_accuracy
           print("this accuracy is valid")
       else:
           print("this accuracy is invalid")
   def set_latency_ms(self,new_latency_ms):
       if 0 < new_latency_ms:
           self.__latency_ms = new_latency_ms
           print("this latency is valid")
       else:
           print("this latency is invalid")
   def set_gpu_count(self,new_gpu_count):
       if new_gpu_count >1:
           self.__gpu_count = new_gpu_count
           print("gpu count is good")
       else:
           print("invalid gpu count")
   def verify_api_key(self,key):
       if self.__api_key == key:
           print("access granted")
       else:
           print("access denied")
   def change_api_key(self,old_key,new_key):
       if old_key == self.__api_key:
           self.__api_key = new_key
           print("api key is changed")
       else:
           print("api key is invalid")
   def show(self):
       print("model name ",self.model_name)
       print("accuracy ",self.get_accuracy())
       print("latency ms ",self.get_latency_ms())
       print("gpu count ",self.get_gpu_count)

cnn = DeploymentModel("cnn","CNN4.5",90,17,40,"Gpt 5.6")
rnn = DeploymentModel("RNN","RNN 5.9",95,45,34,"RSND 4-5-7")
trans = DeploymentModel("Transformer","TRANS 4.6",98,37,56,"TRANS 5-2-3")
models = [cnn,rnn,trans]
for m in models:
   cnn.set_accuracy(98)
   cnn.set_latency_ms(96)
   cnn.set_gpu_count(78)
   rnn.set_accuracy(78)
   rnn.set_latency_ms(79)
   rnn.set_gpu_count(71)
   trans.set_accuracy(96)
   trans.set_latency_ms(95)
   trans.set_gpu_count(72)
   m.show()
highest_accuracy = max(models,key=lambda x : x.get_accuracy())
lowest_accuracy = min(models,key = lambda x : x.get_accuracy())
highest_gpu_count = max(models,key=lambda x : x.get_gpu_count())
model_name_only = list(map(lambda x : x.model_name,models))
print(highest_accuracy.model_name,highest_accuracy.get_accuracy())
print(lowest_accuracy.model_name,lowest_accuracy.get_accuracy())
print(highest_gpu_count.model_name,highest_gpu_count.get_gpu_count())
print(model_name_only)
for rank,values in enumerate(models,start=1):
   print(rank,values.model_name,values.get_accuracy())


from abc import ABC, abstractmethod
class BaseAIModel(ABC):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,api_key,uptime_percentage):
       self.model_name = model_name
       self.version =version
       self.__accuracy = accuracy
       self.__latency_ms = latency_ms
       self.__gpu_count =gpu_count
       self.memory_usage_gb = memory_usage_gb
       self.request_served = request_served
       self.__api_key = api_key
       self.uptime_percentage = uptime_percentage
   def get_accuracy(self):
       return self.__accuracy
   def get_latency_ms(self):
       return self.__latency_ms
   def get_gpu_count(self):
       return self.__gpu_count
   def get_api_key(self):
       return self.__api_key
   def set_accuracy(self,new_accuracy):
       if 0 < new_accuracy <=100:
           self.__accuracy = new_accuracy
           print("This is valid accuracy")
       else:
           print("Invalid accuracy")
   def set_latency_ms(self,new_latency):
       if 0< new_latency:
           self.__latency_ms = new_latency
           print("This is valid latency")
       else:
           print("Invalid latency")
   def set_gpu_count(self,new_gpu_count):
3        if new_gpu_count >= 1:
           self.__gpu_count = new_gpu_count
           print("This is valid gpu count")
       else:
           print("Invalid gpu count")
   def verify_api_keys(self,key):
       if self.__api_key == key:
           print("access Granted")
       else:
           print("access denied")#

   def change_api_key(self,old_key,new_key):
       if old_key == self.__api_key:
           self.__api_key = new_key
           print("key changed")
       else:
           print("Invalid key")#

   @abstractmethod
   def collect_metrics(self):
       pass
   @abstractmethod
   def analyze_health(self):
       pass
   @abstractmethod
   def deploy(self):
       pass
   @abstractmethod
   def generate_model(self):
       pass

class LLMModel(BaseAIModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,api_key,uptime_percentage,
                token_processed,context_window,active_users):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,memory_usage_gb,request_served,api_key,uptime_percentage)
       self.token_processed = token_processed
       self.context_window = context_window
       self.active_users = active_users
   def collect_metrics(self):
       self.token_processed += 20000
       self.request_served += 4000
       self.average_tokens = (self.token_processed / self.active_users)
   def analyze_health(self):
       if self.get_accuracy() < 95:
           self.status = "Need retraining"
       elif self.uptime_percentage < 88:
           self.status = "Critical"
       elif self.get_latency_ms() >100:
           self.status = "High  latency"
       else:
           self.status = "Healthy"
   def deploy(self):
       if self.status == "Need retraining":
           self.action = "Start Retraining Pipeline"
       elif self.status == "Critical":
           self.action = "Restart Kubernetes Pods"
       elif self.status == "High latency":
           self.action  = "Scale GPU Cluster"
       else:
           self.action = "Deploy normally"
class VisionModel(BaseAIModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,api_key,uptime_percentage,
                image_processed,camera_count,objects_detected):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,memory_usage_gb,
                        request_served,api_key,uptime_percentage)
       self.image_processed = image_processed
       self.camera_count = camera_count
       self.objects_detected = objects_detected
   def collect_metrics(self):
       self.image_processed += 12344
       self.objects_detected +=2000
       self.average_object_per_image = (self.image_processed / self.camera_count)
   def analyze_health(self):
       if self.get_accuracy() < 90:
           self.status = "Model Drift"
       elif self.get_latency_ms() > 90:
           self.status = "Critical Downtime"
       elif self.uptime_percentage < 88:
           self.status = " Camera Pipeline failure"
       else:
           self.status = "Healthy"
   def deploy(self):
       if self.status == "Model Drift":
           self.action = "Scale GPU cluster"
       elif self.status == "Critical Downtime":
           self.action = "Retrain Vision model"
       elif self.status == "Camera Pipeline failure":
           self.action = "Restart Vision Model"
       else:
#            self.action = "deploy normally"
class SpeechModel(BaseAIModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,api_key,uptime_percentage,
                audio_hours_processed,languages_supported,transcription_completed):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,memory_usage_gb,
                        request_served,api_key,uptime_percentage)
       self.audio_hours_processed = audio_hours_processed
       self.languages_supported = languages_supported
       self.transcription_completed = transcription_completed
   def collect_metrics(self):
       self.audio_hours_processed += 30000
       self.transcription_completed += 6000
       self.average_transcriptions_per_hour = (self.audio_hours_processed / self.transcription_completed)#

   def analyze_health(self):
       if self.get_accuracy() < 90:
           self.status = "Critical Downtime"
       elif self.get_latency() < 90:
           self.status = "slow response"
       elif self.uptime_percentage < 88:
           self.status = "streaming failure"
       else:
           self.status = "Healthy"
   def deploy(self):
       if self.status == "Critical Downtime":
          self.action = "Scale speech servers"
       elif self.status == "slow response":
           self.action = "Start retraining pipeline"
       elif self.status == "streaming failure":
           self.action = "restart streaming pipeline"
       else:
           self.action = "deploy Normally"
llm = LLMModel("GPT","GPT-4.5",96,90,5,"220 GB",2000,"Key-2.4",90,200,1000,3000)
ision = VisionModel("Gemini","Gemini-8.9",98,93,7,"210 GB",3000,"KII-7.3",98,1200,4500,340)
speech = SpeechModel("clude","c-6.9",99,99,9,"300 GB",4000,"koo 9-4",120,300,23,123)
models = [llm,vision,speech]
for model in models:
   model.collect_metrics()
   model.analyze_health()
   model.deploy()

regions = (
   "US - East",
   "Europe",
   "Asia - pacific"
)
Framework = {
   "Pytorch",
  "Tensor-flow",
   "JaX",
   "Pytorch"
}
deployment_count = {
   "Healthy" : 2,
   "Need Retraining": 1,
   "Critical Downtime":0
}
healthy_models = [
   model.model_name
   for model in models
   if model.status == "Healthy"
]
high_accuracy_model = [
   model.model_name
   for model in models
   if model.get_accuracy()>95
]
accuracy_map = {
   model.model_name :model.get_accuracy()
   for model in models
}
framework_upper = {
   Frame.upper()
   for Frame in Framework
}
model_names = list(map( lambda x : x.model_name,models))
High_accuracy = list(filter(lambda x : x.get_accuracy() > 95,models))
Highest_accuracy= max(models,key= lambda x:x.get_accuracy())
highest_gpu_count = max(models,key=lambda x : x.get_gpu_count())
highest_request_served = max(models, key=lambda x : x.request_served)
lowest_latency = min(models,key=lambda x : x.get_latency_ms())
accuracy_sorted = list(sorted(models,key=lambda x : x.get_accuracy(),reverse=True))
for rank,value in enumerate(accuracy_sorted,start=1):
   print(rank,value.model_name,value.get_accuracy(),value.get_latency_ms(),value.get_latency_ms(),value.status)

POLIMORPHISM:--->(RUNTIME POLYMORPHISM )IT ALLOW us to write a genric code which works different objects  with common interface. each method have its own implementation of the same method so the correct one is chosen automatically at runtime.
METHOD OVERLOADING
from abc import ABC, abstractmethod
class Notification(ABC):
   @abstractmethod
   def send(self):
       pass
class EmailNotification(Notification):
   def send(self):
       print("Email Notification")
class SMSNotification(Notification):
   def send(self):
       print("Sms Notification")
class PushNotification(Notification):
   def send(self):
       print("Push Notification")
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()
notification = [email, sms, push]
for n in notification:
   n.send()

from abc import ABC, abstractmethod
class BaseInferenceModel(ABC):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,memory_usage_gb,request_served,uptime_percentage,api_key):
       self.model_name = model_name
       self.version = version
       self.__accuracy = accuracy
       self.__latency_ms = latency_ms
       self.__gpu_count = gpu_count
       self.memory_usage_gb = memory_usage_gb
       self.request_served = request_served
       self.uptime_percentage = uptime_percentage
       self.__api_key = api_key
   def get_accuracy(self):
       return self.__accuracy
   def get_latency(self):
3        return self.__latency_ms
 def get_gpu_count(self):
       return self.__gpu_count
   def get_api_key(self):
#        return self.__api_key
   def set_accuracy(self,new_accuracy):
       if 0 < new_accuracy <= 100:
           self.__accuracy = new_accuracy
           print("This is valid accuracy")
       else:
           print("Invalid accuracy")
   def set_latency(self,new_latency):
       if new_latency > 0:
           self.__latency_ms = new_latency
           print("This is valid latency")
       else:
           print("Invalid latency")
   def set_gpu_count(self,new_gpu_count):
       if new_gpu_count >= 1:
           self.__gpu_count = new_gpu_count
           print("thi is valid gpu count")
       else:
           print("Invalid gpu count")
   def verify_api_key(self,key):
       if self.__api_key == key:
           print("Access granted")
       else:
           print("access denied")
   def change_api_key(self,old_key,new_key):
       if old_key == self.__api_key:
           self.__api_key = new_key
           print("api key is changed")
       else:
#            print("not changed")
   @abstractmethod
   def collect_metrics(self):
       pass
   @abstractmethod
   def analyze_health(self):
       pass
   @abstractmethod
   def deploy(self):
       pass
   @abstractmethod
   def generate_report(self):
       pass
class LLMModel(BaseInferenceModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,uptime_percentage,api_key,
                token_processed,contex_window,active_users):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,
                       memory_usage_gb,request_served,uptime_percentage,api_key)
       self.token_processed = token_processed
       self.active_users = active_users
       self.contex_window = contex_window
   def collect_metrics(self):
       self.token_processed += 3000
       self.active_users += 1000
       self.average_token_per_user = (self.token_processed / self.active_users)#

   def analyze_health(self):
       if self.get_accuracy()<95:
           self.status = "Need retraining"
       elif self.get_latency()>120:
           self.status = "High latency"
       elif self.uptime_percentage <97:
           self.status = "Critical"
       else:
           self.status = "Healthy"
   def deploy(self):
       if self.status == "Need retraining":
           self.action = "start retraining pipeline"
       elif self.status == "High latency":
           self.action = "Scale Gpu cluster"
       elif self.status == "Critical":
           self.action = "Restart Kubernetes Pods"
       else:
           self.status == "Healthy"
           self.action = "deploy normally"
   def generate_report(self):
       print("model name :", self.model_name)
       print("version :", self.version)
       print("accuracy :", self.get_accuracy())
       print("latency :", self.get_latency())
       print("uptime percentage :", self.uptime_percentage)
       print("token processed:", self.token_processed)
       print("active users:", self.active_users)
       print("average users:",self.average_token_per_user)
class Visionmodel(BaseInferenceModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,uptime_percentage,api_key,
                image_processed,objects_detected,camera_count):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,uptime_percentage,api_key)
       self.image_processed = image_processed
       self.objects_detected = objects_detected
       self.camera_count = camera_count
   def collect_metrics(self):
       self.image_processed += 7000
       self.camera_count += 200
       self.objects_per_image = (self.image_processed / self.camera_count)
   def analyze_health(self):
       if self.get_latency()<92:
           self.status = "Need retraining"
#        elif self.get_latency()>100:
           self.status = "High latency"
       elif self.uptime_percentage <96:
           self.status = 'Critical'
       else:
           self.status = 'Healthy'
   def deploy(self):
       if self.status == "Need retraining":
           self.action = "start retraining pipeline"
       elif self.status == "High latency":
           self.action = "Scale Gpu cluster"
       elif self.status == "Critical":
           self.action = "Restart Kubernetes Pods"
       else:
          self.status = "Healthy"
           self.action = "deploy normally"
   def generate_report(self):
      print("model name :", self.model_name)
       print("version :", self.version)
3       print("accuracy :", self.get_accuracy())
       print("latency :", self.get_latency())
       print("uptime percentage :", self.uptime_percentage)
       print("camera count :", self.camera_count)
       print("image processed:", self.image_processed)
       print("objects per image :",self.objects_detected)

class SpeechModel(BaseInferenceModel):
   def __init__(self,model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,uptime_percentage,api_key,
                audio_hours_processed,languages_supported,transcriptions_completed):
       super().__init__(model_name,version,accuracy,latency_ms,gpu_count,
                memory_usage_gb,request_served,uptime_percentage,api_key)
       self.audio_hours_processed = audio_hours_processed
       self.languages_supported = languages_supported
       self.transcriptions_completed = transcriptions_completed3

   def collect_metrics(self):
       self.audio_hours_processed +=12000
       self.transcriptions_completed +=40000
       self.average_transcriptions_per_hour = (self.transcriptions_completed / self.audio_hours_processed)#

  def analyze_health(self):
       if self.get_latency()<90:
           self.status = "Need retraining"
       elif self.get_latency()>109:
           self.status = "High latency"
       elif self.uptime_percentage <99:
           self.status = 'Critical'
       else:
           self.status = 'Healthy'
   def deploy(self):
       if self.status == "Need retraining":
           self.action = "start retraining pipeline"
       elif self.status == "High latency":
           self.action = "Scale Gpu cluster"
      elif self.status == "Critical":
           self.action = "Restart Kubernetes Pods"
       else:
          self.status = "Healthy"
3           self.action = "deploy normally"

   def generate_report(self):
       print("model name :", self.model_name)
       print("version :", self.version)
      print("accuracy :", self.get_accuracy())
       print("latency :", self.get_latency())
       print("uptime percentage :", self.uptime_percentage)
       print("audio hours processed:", self.audio_hours_processed)
       print("transcriptions completed:", self.transcriptions_completed)
       print("average transcriptions per hour:", self.average_transcriptions_per_hour)

llm = LLMModel("GPT","GPT-3.6",96,120,34,
              "220 Gb",300,100,"GPT-09",3000,2000,1200)

vision = Visionmodel("Cloude","CL-99",97,102,23,
                    "400 GB",4000,100,"CL-909",34000,3400,1200)

speech= SpeechModel("GIMINI","GNI-99",98,99,49,"500 mb",2000,
                   190,"GM-918",20,303,23000)
models = [llm,vision,speech]
for m in models:
   m.collect_metrics()
   m.analyze_health()
   m.deploy()
   m.generate_report()

Highest_accuracy = max(models, key = lambda x:x.get_accuracy())
print(Highest_accuracy.model_name,Highest_accuracy.get_accuracy())

Highest_GPU_count = max(models, key = lambda x:x.get_gpu_count())
print(Highest_GPU_count.model_name,Highest_GPU_count.get_gpu_count())

Highest_request_served = max(models, key = lambda x:x.request_served)
print(Highest_request_served.model_name,Highest_request_served.request_served)

lowest_latency = min(models, key = lambda x:x.get_latency())
print(lowest_latency.model_name,lowest_latency.get_latency())

leaderboard = list(sorted(models,key = lambda x:x.get_accuracy(),reverse = True))
print(leaderboard)

Only_name = list(map(lambda x : x.model_name,models))
print(Only_name)
Only_healthy = list(filter(lambda x : x.status == "Healthy",models))
print(Only_healthy)
having_accuracy = [m.model_name for m in models if m.get_accuracy()>95]
print(having_accuracy)
having_latency = [m.model_name for m in models if m.get_latency()<100]
print(having_latency)
having_GPU = [m.model_name for m in models if m.get_gpu_count() > 4]
print(having_GPU)
dictionary = {
   m.model_name : m.get_accuracy()
   for m in models
}
print(dictionary)
regions = (
   "US - East",
   "Europe",
   "Asia - pacific"
)
print(regions)
FrameWork = {
   "tensorflow",
   "pytorch",
   "jax",
   "tensorflow",
   "jax"
}
all_upper = {
   f.upper()
   for f in FrameWork
}
print(all_upper)

from abc import ABC, abstractmethod
class BaseInferenceModel(ABC):
   def __init__(self,model_name,version,accuracy,latency_ms):
       self.model_name = model_name
       self.version = version
       self.accuracy = accuracy
       self.latency_ms = latency_ms
   @abstractmethod
   def collect_matrics(self):
       pass
   @abstractmethod
   def analyse_health(self):
       pass
   @abstractmethod
   def deploy(self):
       pass
   @abstractmethod
   def generate_report(self):
       pass
class LLMModel(BaseInferenceModel):
   def __init__(self,model_name,version,accuracy,latency_ms,token_processed,active_users):
       super().__init__(model_name,version,accuracy,latency_ms)
       self.token_processed = token_processed
       self.active_users = active_users
   def collect_matrics(self):
       self.active_users +=3000
       self.token_processed +=200
       self.average_users = (self.active_users / self.token_processed) * 100
   def analyse_health(self):
       if self.accuracy < 90:
           self.status = "retrain"
       elif self.latency_ms > 100:
           self.status = "Too fast"
       else:
           self.status = "healthy"
   def deploy(self):
       if self.status == "retrain":
           self.action = "train GPU"
       elif self.status =="Too fast":
           self.action = "retrain"
       else:
           self.action = "deploy normally"

   def generate_report(self):
       print(self.model_name)
       print(self.status)
       print(self.action)
class SpeechModel(BaseInferenceModel):
   def __init__(self,model_name,version,accuracy,latency_ms,audio_processed,languages_supported):
       super().__init__(model_name,version,accuracy,latency_ms)
       self.audio_processed = audio_processed
       self.languages_supported = languages_supported
   def collect_matrics(self):
       self.audio_processed +=5000
       self.languages_supported +=200
       self.average_audio_processed = (self.audio_processed / self.languages_supported) * 100#

  def analyse_health(self):
       if self.accuracy < 90:
           self.status = "retrain"
       elif self.latency_ms > 100:
           self.status = "Too fast"
       else:
           self.status = "healthy"

   def deploy(self):
       if self.status == "retrain":
           self.action = "train GPU"
       elif self.status == "Too fast":
           self.action = "retrain"
       else:
           self.action = "deploy normally"

   def generate_report(self):
       print(self.model_name)
       print(self.status)
       print(self.action)
class VisionModel(BaseInferenceModel):
   def __init__(self, model_name, version, accuracy, latency_ms,image_processed,objects_detected):
       super().__init__(model_name,version,accuracy,latency_ms)
       self.image_processed = image_processed
       self.objects_detected = objects_detected
   def collect_matrics(self):
       self.objects_detected +=400
       self.image_processed += 3000
       self.average_objects_detected = (self.objects_detected / self.image_processed) * 100#

   def analyse_health(self):
       if self.accuracy < 90:
           self.status = "retrain"
       elif self.latency_ms > 100:
           self.status = "Too fast"
       else:
           self.status = "healthy"3

   def deploy(self):
       if self.status == "retrain":
           self.action = "train GPU"
       elif self.status == "Too fast":
           self.action = "retrain"
       else:
           self.action = "deploy normally"

   def generate_report(self):
       print(self.model_name)
       print(self.status)
       print(self.action)
llm = LLMModel("GPT","GPT 2.5",98,100,2000,3000)
vision = VisionModel("GEMINI","GM 2.4",98,102,2000,300)
speech = SpeechModel("Cloude","CL 5.7",99,109,3000,340)
model = [llm,vision,speech]
for m in model:
   m.collect_matrics()
   m.analyse_health()
   m.deploy()
   m.generate_report()


class LLMDeployment():
  def deploy(self):
       print("Deploying LLM...")
class VisionDeployment():
   def deploy(self):
       print("Deploying Vision...")
class SpeechDeployment():
   def deploy(self):
       print("Deploying Speech...")
class RecommendationDeployment():
   def deploy(self):
       print("Deploying Recommendation...")
class FraudDetectionDeployment():
   def deploy(self):
       print("deploying fraud.....")
class RobotDeployment():
   def deploy(self):
       print("Deploying Robot...")
llm = LLMDeployment()
vision = VisionDeployment()
speech = SpeechDeployment()
recommendation = RecommendationDeployment()
fraud = FraudDetectionDeployment()
robot = RobotDeployment()

deployments = [llm,vision,speech,recommendation,fraud,robot]
for d in deployments:
   d.deploy()

COMPOSITION :----> in this we use the one class as the another class object. It "has a" relationship.
class Engine:
   def __init__(self,brand,horsepower):
       self.brand = brand
       self.horsepower = horsepower
   def start(self):
       print("Engine started")

class Car:
   def __init__(self,name,engine):
       self.name = name
       self.engine =engine
   def car_info(self):
       print("car:",self.name)
       print("engine:",self.engine.brand)
       print("HorsePower",self.engine.horsepower)
engine = Engine("Honda",200)
car = Car("Toyota",engine)
#car.car_info()
car.engine.start()

class Address:
   def __init__(self,city,pincode,state):
       self.city = city
       self.pincode = pincode
       self.state = state
class Student:
   def __init__(self,name,age,address):
       self.name = name
       self.age = age
       self.address = address

address = Address("Delhi","110001","Delhi")
student = Student("Rahul",21,address)
print("Name :",student.name)
print("Age :",student.age)
print("city:",student.address.city)
print("pincode:",student.address.pincode)
print("state:",student.address.state)

class Battery:
   def __init__(self,capacity,brand):
       self.capacity = capacity
       self.brand = brand
class Laptop:
   def __init__(self,company,model,battery):
       self.company = company
       self.model = model
       self.battery = battery
   def show_details(self):
       print("Company:",self.company)
       print("Model:",self.model)
       print("Battery:",self.battery.capacity)
       print("Brand:",self.battery.brand)
battery = Battery(3000,"Samsung")
lap = Laptop("Dell","Inspiron",battery)
lap.show_details()

class Dataset:
   def __init__(self,name,number_of_rows,number_of_features):
       self.name = name
       self.number_of_rows = number_of_rows
       self.number_of_features = number_of_features
   def load(self):
       print("Loading...")
   def summery(self):
       print("Summing...")
class Model:
   def __init__(self,model_name,algorithm):
       self.model_name = model_name
       self.algorithm = algorithm
   def train(self):
       print("Training Random Forest")
  def predict(self):
       print("Predicting...")
class MLPipeline:
   def __init__(self,dataset,model):
       self.dataset = dataset
       self.model = model
   def run(self):
       print("==== ML Pipeline Start ====")
       self.dataset.load()
       self.dataset.summery()
       self.model.train()
       self.model.predict()
dataset = Dataset("Irish",150,54)
model = Model("Random forest","viral")
pipeline = MLPipeline(dataset,model)
pipeline.run()

class Customer:
   def __init__(self,customer_id,name,email):
       self.customer_id = customer_id
       self.name = name
       self.email = email
   def display_customer(self):
       print("customer id:",self.customer_id)
       print("Name",self.name)
       print("Email",self.email)
class Product:
   def __init__(self,product_id,product_name,price,quantity):
       self.product_id = product_id
       self.product_name = product_name
       self.price = price
       self.quantity = quantity
   def display_product(self):
       print(f"{self.product_name} - {self.price} x {self.quantity}")
class Payment:
   def __init__(self,payment_method,):
       self.payment_method = payment_method
   def pay(self,amount):
       print(f"\n ===== Payment Method =====")
       print(f"payment method : {self.payment_method}")
       print(f"amount : {amount}")
       print("payment successful")

class ShoppingCart:
   def __init__(self,customer,payment):
       self.customer = customer
       self.product = []
      self.payment = payment
   def add_product(self,product):
       self.product.append(product)
       print(f"{product.product_name} added to the cart....")
   def remove_product(self,product_id):
       for product in self.product:
           if product.product_id == product_id:
               self.product.remove(product)
               print(f"{product.product_name} removed from the cart....")
               return
           print("product not found....")
#    def show_cart(self):
       print("\n =====shoping cart =====")
       print(f"customer : {self.customer.name}\n")

       if not self.product:
           print("No products added to the cart....")
           return
       for product in self.product:
           print(
               f"{product.product_name}|"
               f"price: {product.price}|"
               f"quantity: {product.quantity}"
           )
   def calculate_total(self):
       total = 0
       for product in self.product:
           total += product.price * product.quantity
       return total
   def check_out(self):
       print("\n =====checkout =====")

       self.customer.display_customer()
       print("\n Product:")
       for product in self.product:
           product.display_product()
       total = self.calculate_total()
       print(f"\n Total ammount : {total}")
       self.payment.pay(total)
c = Customer(999,"Aman","amankapil@gmail.com")
p = Payment("UPI")
product1 = Product(1,"laptop",65000,1)
product2 = Product(2,"apple",69000,2)
product3 = Product(3,"samsung",45000,3)
cart = ShoppingCart(c,p)
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.show_cart()
cart.remove_product(2)
cart.show_cart()
cart.check_out()

class Department:
   def __init__(self,department_name,manager):
       self.department_name = department_name
       self.manager = manager
   def department_info(self):
       print(f"departmemt_name:,{self.department_name}")
       print(f"manager:,{self.manager}")
class Employee:
   def __init__(self,name,salary,department):
       self.name = name
      self.salary = salary
       self.department = department
   def employee_info(self):
       print(f"name:,{self.name}")
       print(f"salary:,{self.salary}")
       self.department.department_info()

department = Department("AI team","Aman")
employee = Employee("Rahul",40000,department)
department.department_info()
employee.employee_info()

class Professor:
   def __init__(self,name,subject):
       self.name = name
       self.subject = subject
   def display_professor(self):
       print("----professor----")
       print(f"name: {self.name}")
       print(f"subject: {self.subject}")
class Course:
   def __init__(self,course_name,duration,professor):
       self.course_name = course_name
       self.duration = duration
       self.professor = professor
   def display_course(self):
       print("------Course Details------")
       print(f"name: {self.course_name}")
#        print(f"duration: {self.duration}")
       self.professor.display_professor()
class Student:
   def __init__(self,name,age,course):
       self.name = name
       self.age = age
       self.course = course
   def display_student(self):
       print("------Student Details------")
       print(f"name: {self.name}")
       print(f"age: {self.age}")
       self.course.display_course()
prof = Professor("Dr. Smith","Machine Learning")
course = Course("Ai Engineering","6 Month",prof)
student = Student("Aman",25,course)
student.display_student()

class Book:
   def __init__(self,title,author,price):
       self.title = title
       self.author = author
       self.price = price
   def book_info(self):
       print("------Book info----")
       print("Title:", self.title)
       print("Author:", self.author)
       print("Price:",self.price)
class Library:
   def __init__(self,library_name):
       self.library_name = library_name
       self.books = []
   def add_book(self,book):
       self.books.append(book)
   def show_books(self):
       print(f"\n--------{self.library_name} books--------")
       for book in self.books:
#            print(book.title)
book1 = Book("python Basics","me",300)
book2 = Book("Machine Learning","me",300)
book3 = Book("Deep Learning","me",800)
lib = Library("central Library")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.show_books()


class Doctor:
   def __init__(self,name,specialization):
       self.name = name
       self.specialization = specialization
   def show_details(self):
       print("Doctor", self.name)
       print("Specialization",self.specialization)

class Patient:
   def __init__(self,name,age):
       self.name = name
       self.age = age
   def show_details(self):
       print("Patient", self.name)
       print("Age", self.age)

class Appointment:
   def __init__(self,doctor,patient):
       self.doctor = doctor
       self.patient = patient
   def book(self):
       print("------Appointment Booked-----")
   def show_details(self):
       self.doctor.show_details()
       self.patient.show_details()

doc = Doctor("Dr. Smith","Cardiologist")
pat = Patient("Aman",22)
app = Appointment(doc,pat)
app.book()
app.show_details()


class Dataset:
   def __init__(self,name,rows,columns):
       self.name = name
       self.rows = rows
       self.columns = columns
   def load(self):
       print("Loading Dataset")
class Model:
   def __init__(self,model_name,accuracy):
       self.model_name = model_name
       self.accuracy = accuracy
   def train(self):
       print("Training Model")
   def predict(self):
       print("Predicting Model")
class Pipeline:
   def __init__(self,dataset,model):
       self.dataset = dataset
       self.model = model
   def run(self):
       self.dataset.load()
       self.model.train()
       self.model.predict()
dataset = Dataset("Transformer",400,6785)
model = Model("Burt",100)
pipeline = Pipeline(dataset,model)
pipeline.run()


class Config:
   def __init__(self,learning_rate,batch_size,epochs):
       self.learning_rate = learning_rate
       self.batch_size = batch_size
       self.epochs = epochs
   def show_config(self):
       print("Learning rate:", self.learning_rate)
       print("Batch size:", self.batch_size)
       print("Epochs:",self.epochs)
class Model:
   def __init__(self,model_name,config):
       self.model_name = model_name
       self.config = config

   def train(self):
       print("Training BERT......")
       self.config.show_config()

   def show_model(self):
       print("Model Name:", self.model_name)
con = Config(0.001,32,10)
model = Model("BERT",con)
model.train()

class Dataset:
   def __init__(self,name,rows,features):
       self.name = name
       self.rows = rows
       self.features = features
   def load(self):
       print("loading dataset....")
class ModelConfig:
   def __init__(self,learning_rate,epochs):
       self.learning_rate = learning_rate
       self.epochs = epochs
   def show_config(self):
       print("learning rate:",self.learning_rate)
       print("epochs:",self.epochs)
class Model:
   def __init__(self,name,config):
       self.name = name
       self.config = config
   def train(self):
       print("training model....")
   def predict(self):
       print("predicting....")
class Optimizer:
   def __init__(self,name):
       self.name = name
   def step(self):
       print("optimizer Step.....")
class TrainingSystem:
   def __init__(self,dataset,model,optimizer):
       self.dataset = dataset
       self.model = model
       self.optimizer = optimizer
   def run(self):
       self.dataset.load()
       self.model.train()
       self.optimizer.step()
       self.model.predict()
data = Dataset("bert",34,45)
m = ModelConfig(0.7,45)
model = Model("bert",m)
opti = Optimizer("Adam")
train = TrainingSystem(data,model,opti)
train.run()

class Model:
   def __init__(self,name,algorithm,accuracy):
       self.name = name
       self.algorithm = algorithm
       self.accuracy = accuracy
   def show_details(self):
       print("Model:",self.name)
       print("Algorithm:",self.algorithm)
       print("Accuracy:",self.accuracy)
class ModelRegistry:
   def __init__(self,registry_name):
       self.registry_name = registry_name
       self.models = []
   def add_model(self,model):
       self.models.append(model)
   def remove_model(self,model_name):
       for model in self.models:
           if model.name == model_name:
               self.models.remove(model)
               return
   def show_models(self):
       for model in self.models:
           model.show_details()
   def get_best_model(self):
       best_model = self.models[0]

       for model in self.models:
           if model.accuracy > best_model.accuracy:
               best_model = model
       return best_model
model1 = Model("Random Forest.",2,0.91)
model2 = Model("XGBoost.",2,0.95)
model3 = Model("Neural Network",4,0.93)
M  = ModelRegistry("AI Models")
M.add_model(model1)
M.add_model(model2)
M.add_model(model3)
M.show_models()
best = M.get_best_model()
print("\n best model:")
best.show_details()

Magic Method
class Model:
   def __init__(self,name,algorithm,accuracy):
       self.name = name
       self.algorithm = algorithm
       self.accuracy = accuracy
   def __str__(self):
       return f"model Name : {self.name} | algorithm: {self.algorithm} | Accuracy:| {self.accuracy}"

class ModelRegistry:
   def __init__(self,registry_name):
       self.registry_name = registry_name
       self.models = []
   def add_model(self,model):
      self.models.append(model)
   def show_models(self):
       print(f"------ {self.registry_name} -------")
       for model in self.models:
           print(model)
model1 = Model("Random Forest","Ensemble",0.91)
model2 = Model("XGBoost","GradientBoosting",0.95)
model3 = Model("Neural Network","Deep Learning",0.93)

registry = ModelRegistry("AI Models")
registry.add_model(model1)
registry.add_model(model2)
registry.add_model(model3)
registry.show_models()


class Model:
   def __init__(self,name,algorithm,accuracy):
       self.name = name
       self.algorithm = algorithm
       self.accuracy = accuracy
   def __str__(self):
       return f"model name : {self.name} | algorithm : {self.algorithm} | Accuracy : {self.accuracy}"

class Dataset:
   def __init__(self,name,rows,features):
       self.name = name
       self.rows = rows
       self.features = features
   def __str__(self):
       return f" Dataset : {self.name} | Rows : {self.rows} | Features : {self.features}"

class Experiment:
   def __init__(self,experiment_name,model,dataset):
       self.experiment_name = experiment_name
       self.model = model
       self.dataset = dataset
   def __str__(self):
       return f" Experiment Name : {self.experiment_name} | Model : {str(self.model)} | Dataset : {str(self.dataset)}"

class ExperimentManager:
   def __init__(self,name):
       self.name = name
       self.experiment = []
   def add_experiment(self,experiment):
       self.experiment.append(experiment)
   def show_experiments(self):
         for experiment in self.experiment:
             print(experiment)
model1 = Model("XGBoost","Gradient Boosting",0.95)
dataset1 = Dataset("Customer Data",10000,25)
experiment1 = Experiment("Customer Prediction",model1,dataset1)

model2 = Model("Random Forest","Ensemble",0.91)
dataset2 = Dataset("Fraud Data",50000,30)
experiment2 = Experiment("Fraud detection",model2,dataset2)

manager = ExperimentManager("Ai experiment")
manager.add_experiment(experiment1)
manager.add_experiment(experiment2)
manager.show_experiments()

repr magic method :-->
class Model:
   def __init__(self,name,algorithm,accuracy):
       self.name = name
      self.algorithm = algorithm
       self.accuracy = accuracy
   def __str__(self):
       return f"model : {self.name} | algorithm : {self.algorithm} | accuracy : {self.accuracy}"

   def __repr__(self):
       return f"Model(name = {self.name} | algorithm = {self.algorithm} | accuracy = {self.accuracy}"
model = Model("XGBoost","Gradient Boosting",0.95)
print(model)
print(repr(model))

class Dataset:
   def __init__(self,name ,rows,feature):
       self.name = name
       self.rows = rows
       self.feature = feature
   def __str__(self):
       return f"{self.name} | {self.rows} | {self.feature}"
   def __repr__(self):
       return f" Name : {self.name} | rows : {self.rows} | feature : {self.feature}"
   def __len__(self):
       return self.rows
dataset = Dataset("Customer Data",10000,25)
print(dataset)
print(repr(dataset))
print(len(dataset))

class Model:
   def __init__(self,name,algorithm,accuracy):
       self.name = name
       self.algorithm = algorithm
       self.accuracy = accuracy
   def __str__(self):
       return f"{self.name} | {self.algorithm} | {self.accuracy}"
   def __repr__(self):
       return f" Name: {self.name} | Algorithm: {self.algorithm} | accuracy: {self.accuracy}"
class ModelRegistry:
   def __init__(self,registry_name):
       self.registry_name = registry_name
       self.models = []
   def add_models(self,model):
       self.models.append(model)
   def __len__(self):
       return len(self.models)
   def __str__(self):
       return f" {self.registry_name} \n Models :{len(self)} "
   def __repr__(self):
       return f" Registry name : {self.registry_name} , Models : {len(self)} "
model1 = Model("XGBoost","Gradient Boosting",0.95)
model2 = Model("Random Forest","Ensemble",0.91)
model3 = Model("Neural Network","Deep Learning",0.93)
registry = ModelRegistry("AI Registry")
registry.add_models(model1)
registry.add_models(model2)
registry.add_models(model3)
print(model1)
print(repr(model1))
print(registry)
print(repr(registry))
print(len(registry))

class ExperimentResult:
   def __init__(self,model_name,accuracy,dataset):
       self.model_name = model_name
       self.accuracy = accuracy
       self.dataset = dataset
   def __eq__(self,other):
       return (self.model_name == other.model_name and
               self.accuracy == other.accuracy and
               self.dataset == other.dataset)
   def __add__(self,other):
       return ExperimentResult(self.model_name+ "x" +other.model_name,
                               (self.accuracy + other.accuracy)/2,
                               self.dataset + other.dataset)
result1 = ExperimentResult("XGBoost",0.95,"customer Data")
result2 = ExperimentResult("XGBoost",0.95,"customer Data")
result3 = ExperimentResult("Random Forest",0.91,"customer Data")
print(result1 == result2)
print(result1 == result3)
combined = result1 + result3
print(combined.model_name)
#print(combined.accuracy)
print(combined.dataset)

class Experiment:
   def __init__(self,model_name,accuracy,training_time,dataset,prediction):
       self.model_name = model_name
       self.accuracy = accuracy
       self.training_time = training_time
       self.dataset = dataset
       self.prediction = prediction
   def __eq__(self,other):
       return (self.model_name == other.model_name and
               self.accuracy == other.accuracy and
               self.training_time == other.training_time and
               self.dataset == other.dataset and
               self.prediction == other.prediction)
   def __add__(self,other):
       if not isinstance(other,Experiment):
           return NotImplemented
       if self.dataset == other.dataset:
           dataset = self.dataset
       else:
           dataset = self.dataset+ "+" + other.dataset
       accuracy = ((self.accuracy * self.prediction)
                   +(other.accuracy * other.prediction)
                   ) /(self.prediction+other.prediction)
       return Experiment(self.model_name+ "+" + other.model_name,
                         accuracy,
                         self.training_time + other.training_time,
                         dataset,
                         self.prediction + other.prediction)

exp1 = Experiment("XGBoost",0.95,120,"customer data",10000)
exp2 = Experiment("Random Forest",0.90,180,"customer Data",5000)
exp3 = Experiment("Nural Network",0.93,300,"Fraud data",8000)
print(exp1 == exp2)
print(exp1 == exp1)
combined1 = exp1 + exp2
combined2 = exp1 + exp3
print(combined1.model_name)
print(combined1.accuracy)
print(combined1.training_time)
print(combined1.dataset)
print(combined1.prediction)
print("\n-----combined 2----")
print(combined2.model_name)
print(combined2.accuracy)
print(combined2.training_time)
print(combined2.dataset)
print(combined2.prediction)

class Model:
   def __init__(self,name,accuracy,size_mb,inference_time):
       self.name = name
       self.accuracy = accuracy
       self.size_mb = size_mb
       self.inference_time = inference_time
   def __str__(self):
       return f" {self.name} | accuracy : {self.accuracy} | size : {self.size_mb} | inference : {self.inference_time}"
   def __repr__(self):
       return f'name = {self.name},accuracy = {self.accuracy}, size_mb = {self.size_mb},inference_time = {self.inference_time}'
   def __len__(self):
       return self.size_mb
   def __eq__(self,other):
       return (self.name == other.name and
               self.accuracy == other.accuracy and
               self.size_mb == other.size_mb and
               self.inference_time == other.inference_time)
   def __add__(self,other):
       if not isinstance(other,Model):
           return NotImplemented

       return Model(self.name+ "+" +other.name,
                    (self.accuracy + other.accuracy)/2,
                    self.size_mb + other.size_mb,
                    (self.inference_time + other.inference_time)/2)
   def __lt__(self,other):
       return self.accuracy < other.accuracy
   def __gt__(self,other):
       return self.accuracy > other.accuracy
   def __le__(self,other):
       return self.accuracy <= other.accuracy
   def __ge__(self,other):
       return self.accuracy >= other.accuracy
   def __ne__(self,other):
       return self.accuracy != other.accuracy
model1 = Model("XGBoost",0.95,250,12)
model2 = Model("Random Forest",0.91,300,18)
model3 = Model("Nural Network",0.97,500,25)
model4 = Model("XGBoost",0.95,250,12)
print(model1)
print(repr(model1))
print(len(model1))
print(model1 == model4)
print(model1 == model2)
combined = model1 +model2
print(combined)
print(model1 < model3)

print(model1 > model2)
print(model1 <= model4)
print(model3 >= model1)
print(model1 != model2)

class ModelResult:
    def __init__(self,model_name,predictions):
        self.model_name = model_name
        self.predictions = predictions
    def __getitem__(self,index):
        return self.predictions[index]
    def __setitem__(self,index,value):
         self.predictions[index]= value
result = ModelResult("XGBoost",[0.91,0.82,0.75,0.96])
print(result[0])
print(result[2])
result[2]=0.99
#print(result[2])
print(result[1])

class PredictionStore:
   def __init__(self,model_name,predictions):
       self.model_name = model_name
       self.predictions = predictions
   def __getitem__(self,index):
       if index < -len(self.predictions) or index >= len(self.predictions):
           raise IndentationError("prediction index out of range")
       return self.predictions[index]
   def __setitem__(self,index,value):
       if index < -len(self.predictions) or index >= len(self.predictions):
           raise IndexError("prediction index out of range")
       if value < 0 or value > 1:
           raise ValueError("Prediction must be between 0 and 1")
       self.predictions[index] = value
   def __len__(self):
       return len(self.predictions)
   def __contains__(self,value):
       return value in self.predictions
store = PredictionStore("Fraud detection",[0.91,0.23,0.87,0.45,0.76])
print(store[0])
print(store[2])
print(store[-1])
store[2] = 0.95
print(store[2])
print(len(store))
print(0.95 in store)
print(0.50 in store)


class ModelRegistry:
   def __init__(self):
       self.models = {}
   def __setitem__(self,model_name,accuracy):
       if accuracy < 0 or accuracy >1:
           raise ValueError("accuracy must be between 0 and 1")
       self.models[model_name] = accuracy
   def __getitem__(self,model_name):
       if model_name not in self.models:
           raise KeyError("Model not found")
       return self.models[model_name]
   def __contains__(self,model_name):
       return model_name in self.models
   def __len__(self):
       return len(self.models)
   def __delitem__(self,model_name):
       if model_name not in self.models:
           raise KeyError("Model not found")
       del self.models[model_name]
registry = ModelRegistry()
registry["XGBoost"] = 0.94
registry["RandomForest"] = 0.89
registry["NeuralNetwork"] = 0.97
print(registry["XGBoost"])
print("XGBoost" in registry)
print(len(registry))
del registry["RandomForest"]
print("RandomForest" in registry)
print(len(registry))

class ModelPipeline:
   def __init__(self,model):
       self.model = model
       self.current = 0
   def __iter__(self):
       return self
   def __next__(self):
       if self.current >= len(self.model):
           raise StopIteration
       result = self.model[self.current]
       self.current +=1
       return result
   def __call__(self,data):
       return f"{self.model} on {data}"
   def reset(self):
       self.current = 0
pipeline = ModelPipeline(["XGBoost",
                      "Random Forest",
                      "Neural Network"
                      ])
print(next(pipeline))
print(next(pipeline))

print(pipeline("customer Data"))

class ModelRegistry:
   def __init__(self,models):
       self.models = models
       self.current = 0
   def __iter__(self):
       return self
   def __next__(self):
       if self.current >= len(self.models):
           raise StopIteration
       result = self.models[self.current]
       self.current +=1
       return result
   def __call__(self,model_name):
       for model in self.models:
           if model == model_name:
              return f"Model {model_name} Found"
       return f"Model {model_name} Not Found"
   def reset(self):
       self.current = 0
model = ModelRegistry(["XGBoost",
                      "Random Forest",
                      "Neural Network",
                      "SVM"
                      ])
print(next(model))
print(next(model))
print("------ Loop-----")
model.reset()
for m in model:
   print(m)
print("-----Search----")
print(model("XGBoost"))
print(model("Bert"))
print("------Reset----")
model.reset()


class DataBatch:
   def __init__(self,data):
       self.data = data
       self.current = 0
   def __iter__(self):
       return self
   def __next__(self):
       if self.current >= len(self.data):
           raise StopIteration
       result = self.data[self.current]
       self.current += 1
       return result
   def __call__(self,operation):
           if operation == "sum":
               return sum(self.data)
           elif operation == "max":
               return max(self.data)
           elif operation == "min":
               return min(self.data)
           else:
               return "Unknown operation"
   def reset(self):
       self.current = 0
batch = DataBatch([10,20,30,40,50])
print("----Manual iteration----")
print(next(batch))
print(next(batch))
print("-----Reset-----")
batch.reset()
print(next(batch))
print("---for Loop-----")
for value in batch:
   print(value)
print("----operations----")
print(batch("sum"))
print(batch("max"))
print(batch("min"))
print(batch("average"))
print("----Final reset-----")
batch.reset()
print(next(batch))

class InferencePipeline:
   def __init__(self,inputs):
#        self.inputs = inputs
       self.current = 0
       self.processed = 0
   def __iter__(self):
       return self
   def __next__(self):
       if self.current >= len(self.inputs):
           raise StopIteration
       result = self.inputs[self.current]
       self.current +=1
       self.processed += 1
       return result
   def __call__(self,data):
       return f"prediction for {data}"
   def reset(self):
       self.current = 0
#pipeline = InferencePipeline(["image_1",
                             "image_2",
                             "image_3",
                             "image_4"
                             ])
print("------Manual inference-----")
print(next(pipeline))
print(next(pipeline))
print("------processed----")
print(pipeline.processed)
print("----Reset----")
pipeline.reset()
print(next(pipeline))
print("----Direct call ----")
print(pipeline("image_100"))
print("-----for loop----")
for p in pipeline:
   print(p)
print("------Total Processed-----")
print(pipeline.processed)


class InferenceEngine:
   def __init__(self,data):
       self.data = data
       self.current = 0
       self.processed = 0
       self.threshold = 0
   def __iter__(self):
       return self
   def __next__(self):
       while self.current < len(self.data):
           result = self.data[self.current]
           self.current += 1
           if result ["score"] < self.threshold:
               continue
           self.processed += 1
           return result['text']
       raise StopIteration
   def set_threshold(self,threshold):
           self.threshold = threshold
   def __call__(self,data):
       return f"Prediction for : {data}"
   def reset(self):
       self.current = 0
engine = InferenceEngine([
   {"id": 1, "text": "I love this product", "score": 0.92},
   {"id": 2, "text": "Bad experience", "score": 0.41},
   {"id": 3, "text": "Excellent service", "score": 0.87},
   {"id": 4, "text": "Not good", "score": 0.32}
])
print(next(engine))
print(next(engine))
print("==== Processed====")
print(engine.processed)
print("=====Reset=====")
engine.reset()
print(next(engine))
print("======Threshold=====")
engine.reset()
engine.set_threshold(0.82)
for e in engine:
   print(e)
print("====Call+====")
print(engine("This is new sentence"))
print("======Total Processed=====")
print(engine.processed)

Static Method: it is mainly used for the helper utility function but do not belong to the class or object.
we use the static method where we do not depend on  the  class but logically it linked with the class.
class ModelValidator:
   def __inti__(self,model_name,accuracy,size_mb):
       self.model_name = model_name
       self.accuracy = accuracy
       self.size_mb = size_mb
   @staticmethod
   def validate_accuracy(accuracy):
       if not isinstance(accuracy,(int ,float)):
           raise TypeError("Accuracy must be a numeric value")
       if accuracy < 0 or accuracy > 1:
#            raise ValueError("accuracy must be between 0 and 1")
       else:
           return True
ModelValidator.validate_accuracy(0.95)
ModelValidator.validate_accuracy(1.5)
ModelValidator.validate_accuracy("0,95")

class DeploymentValidator:
   def __init__(self,model_name,size_mb,inference_time):
       self.model_name = model_name
       self.size_mb = size_mb
       self.inference_time = inference_time
   @staticmethod
   def validate_size(size_mb):
       if not isinstance(size_mb,(int,float)):
           raise TypeError('size_mb must be a number')
       if size_mb <= 0:
           raise ValueError("size must be grater than 0")
       if size_mb > 1000:
           raise ValueError("Size must be grater than 1000mb")
       return True
   @staticmethod
   def validate_inference_time(inference_time):
       if not isinstance(inference_time,(int,float)):
           raise TypeError('inference_time must be a number')
       if inference_time <= 0:
           raise ValueError("inference_time must be grater than 0")
       if inference_time > 100:
           raise ValueError("inference_time must be grater than 100mb")
       return True
   @staticmethod
   def validate_name(model_name):
       if not isinstance (model_name,str):
           raise TypeError('model_name must be a string')
       if not model_name.strip():
           raise ValueError("model name must not be empty")
       if len(model_name.strip()) < 3:
           raise ValueError("model_name must not be empty")
       return True
   def is_deployable(self):
       return(
           self.validate_name(self.model_name)
           and self.validate_size(self.size_mb)
           and self.validate_inference_time(self.inference_time)
       )
model1 = DeploymentValidator("XGBoost",250,25)
model2 = DeploymentValidator("Neural Network",1500,30)
model3 = DeploymentValidator("Ai",500,150)
model4 = DeploymentValidator("Random Forest",300,40)
print(model1.is_deployable())
print(model2.is_deployable())
print(model3.is_deployable())
print(model4.is_deployable())

class FeatureEngineer:
   def __init__(self,feature_name,values):
       self.feature_name = feature_name
       self.values = values
   @staticmethod
   def normalize(values,minimum,maximum):
       result = (values - minimum) / (maximum - minimum)
       if maximum == minimum:
           raise ValueError("maximum and minimum can not be the same")
       return result
   @staticmethod
   def clip(value,minimum,maximum):
       if value < minimum:
           return minimum
       if value > maximum:
           return maximum
       return value
   def transform(self):
       minimum = min(self.values)
       maximum = max(self.values)
       result = []
       for value in self.values:
           normalized = self.normalize(value,minimum,maximum)
           result.append(normalized)
       return result
feature = FeatureEngineer("score",[0,25,50,75,100])
print(FeatureEngineer.normalize(75,0,100))
print(FeatureEngineer.clip(150,0,100))
print(FeatureEngineer.clip(-10,0,100))
print(FeatureEngineer.clip(50,0,100))
print(feature.transform())

class PredictionMetrics:
   def __init__(self,actual,predicted):
       self.actual = actual
       self.predicted = predicted
   @staticmethod
   def accuracy(actual,predicted):
       correct = 0
       for a,p in zip(actual,predicted):
           if a == p:
               correct += 1
       return correct / len(actual)
   @staticmethod
   def error_count(actual,predicted):
       errors = 0
       for a,p in zip(actual,predicted):
           if a != p:
               errors +=1
       return errors
   def evaluate(self):
       return{
           "accuracy":self.accuracy(self.actual,self.predicted),
           "errors":self.error_count(self.actual,self.predicted)

   }
metrics = PredictionMetrics(
   [1, 0, 1, 1, 0],
   [1, 0, 0, 1, 1]
)

print(PredictionMetrics.accuracy(
   [1, 0, 1],
   [1, 1, 1]
))

print(PredictionMetrics.error_count(
   [1, 0, 1],
   [1, 1, 1]
))

print(metrics.evaluate())


Class Method:
class Model:
   total_model = 0
   def __init__(self,name,accuracy,framework):
       self.name = name
       self.accuracy = accuracy
       self.framework = framework
       Model.total_model +=1
   @classmethod
   def from_dict(cls,data):
       return cls(
           data['name'],
           data['accuracy'],
           data['framework']
       )
   @classmethod
   def show_total_models(cls):
        return cls.total_model
model1 = Model("XGBoost",0.95,"scikit-learn")
model2 = Model("ResNet",0.97,"pytorch")
data = {
   "name": "BErt",
   "accuracy": 0.94,
   "framework": "PyTorch"
}
model3 = Model.from_dict(data)
print(model3.name)
print(model3.accuracy)
print(model3.framework)
print(Model.show_total_models())


class AIModel:
   model_count = 0
   def __init__(self,name,framework,version,accuracy):
       self.name = name
       self.framework = framework
       self.version = version
       self.accuracy = accuracy
      AIModel.model_count +=1
   @classmethod
   def from_config(cls,config):
       return cls(
           config["model_name"],
           config["framework"],
           config["version"],
          config["accuracy"]
       )
   @classmethod
   def from_string(cls,model_string):
       parts = model_string.split(",")
       return cls(parts[0],parts[1],parts[2],parts[3])
   @classmethod
   def get_model_count(cls):
       return cls.model_count
model1 = AIModel("XGBoost","Scikit_learn","1.5",0.95)
config = {
   "model_name":"Llama",
   "framework":"Pytorch",
   "version":"3.1",
   "accuracy":0.94
}
model2 = AIModel.from_config(config)
model3 = AIModel.from_string("BERT,TensorFlow,2.1,0.91")
print(model1.name)
print(model2.name)
print(model3.name)
print(model2.framework)
print(model3.framework)
print(AIModel.get_model_count())


class Model:
   def __init__(self,name,accuracy):
       self.name = name
       self.accuracy = accuracy
   @classmethod
   def from_dict(cls,data):
       return cls(data["name"],data["accuracy"])
class DeepLearningModel(Model):
   def __init__(self,name,accuracy,framework):
      super().__init__(name,accuracy)
       self.framework = framework
   @classmethod
   def from_dict(cls,data):
       return cls (data["name"],data["accuracy"],data["framework"])
data1 = {
   "name" : "XGBoost",
   "accuracy" : 0.95
}
data2 = {
   "name" : "ResNet",
   "accuracy" : 0.97,
   "framework": "pytorch"
}
model1 = Model.from_dict(data1)
model2 = DeepLearningModel.from_dict(data2)
print(model1.name)
print(model2.name)
print(model1.accuracy)
print(model2.accuracy)
print(model2.framework)
print(type(model1).__name__)
print(type(model2).__name__)

property it make the method behave like an attribute. we can control over an attribute.
class ModelConfig:
   def __init__(self,model_name,learning_rate,batch_size):
       self._model_name = model_name
       self._learning_rate = learning_rate
       self._batch_size = batch_size
   @property
   def model_name(self):
       return self._model_name
   @model_name.setter
   def model_name(self,value):
       if not isinstance(value,str):
           raise TypeError("model_name must be a string")
       if not value.strip():
           raise ValueError("model_name must not be empty")
       if len(value.strip())<3:
           raise ValueError("model_name must contain at least 3 characters")
       self.model_name = value
   @property
   def learning_rate(self):
       return self._learning_rate
   @learning_rate.setter
   def learning_rate(self,value):
       if not isinstance(value,(int,float)):
           raise TypeError("Learning rate must be a number")
       if value < 0:
           raise ValueError("value must be grater than 0")
       if value > 1:
           raise ValueError("value is not grater than one")
       self._learning_rate = value
  @property
   def batch_size(self):
       return self._batch_size
   @batch_size.setter
   def batch_size(self,value):
       if not isinstance(value,int):
#            raise TypeError("Batch size must be a integer")
       if value < 0 :
           raise ValueError("Batch size must be grater than 0")
       if value % 8 != 0:
           raise ValueError("Batch size must be a multiple of 8")
config = ModelConfig("BERT",0.001,32)
print(config.model_name)
#print(config.learning_rate)
print(config.batch_size)
config.learning_rate = 0.01
config.batch_size = 64
print(config.learning_rate)
print(config.batch_size)


class DeploymentConfig:
   def __init__(self,model_name,memory_mb,inference_time_ms,confidence_threshold):
       self._model_name = model_name
       self._memory_mb = memory_mb
       self._inference_time_ms = inference_time_ms
       self._confidence_threshold = confidence_threshold
   @property
   def model_name(self):
       return self._model_name
   @model_name.setter
   def model_name(self,value):
       if not isinstance(value,str):
           raise TypeError('model_name must be a string')
#        if not value.strip():
           raise ValueError("model must not be empty")
       if len(value.strip())<3:
           raise ValueError("model must have at least 3 characters")
       self._model_name = value
   @property
   def memory_mb(self):
       return self._memory_mb
   @memory_mb.setter
   def memory_mb(self,value):
       if not isinstance(value,(int,float)):
           raise TypeError("memory_mb must be a int or float number")
       if value < 0:
           raise ValueError("memory_mb must be grater than zero")
       if value > 16000:
           raise ValueError("memory_mb must be less than 16000")
       self._memory_mb = value
   @property
   def inference_time_ms(self):
       return self._inference_time_ms
   @inference_time_ms.setter
   def inference_time_ms(self,value):
       if not isinstance(value,(int,float)):
           raise TypeError("inference must be a number")
       if value < 0:
           raise ValueError("inference must be grater than zero")
       if value > 1000:
           raise ValueError("inference must be less than 1000")
       self._inference_time_ms = value
   @property
   def confidence_threshold(self):
       return self._confidence_threshold
   @confidence_threshold.setter
   def confidence_threshold(self,value):
       if not isinstance(value,(int,float)):
           raise TypeError("interference must be a number")
       if value < 0 or value > 1:
           raise ValueError("confidence_threshold must be between zero and 1")
       self._confidence_threshold = value
   @property
   def is_deployable(self):
       if self.memory_mb <= 8000 and self.inference_time_ms <= 500 and self.confidence_threshold >= 0.80:
           return True
       else:
           return False
config = DeploymentConfig("BERT",6000,400,0.85)
print(config.model_name)
print(config.memory_mb)
print(config.inference_time_ms)
print(config.confidence_threshold)
print(config.is_deployable)
config.memory_mb = 9000
print(config.is_deployable)

class MlModel:
   def __init__(self,model_name,weight,bias):
       self._model_name = model_name
       self._weight = weight
       self._bias = bias

   @property
   def model_name(self):
       return self._model_name
   @model_name.setter
   def model_name(self,value):
       if not isinstance(value,str):
           raise TypeError("model name must be string")
       if not value.strip():
#            raise ValueError("model_name must not be empty")
       if len(value.strip()) < 3:
           raise ValueError("model name must not be empty")
       self._model_name = value
   @property
   def weight(self):
       return self._weight
   @weight.setter
   def weight(self,value):
       if not isinstance(value,list):
           raise TypeError("weight must be list")
       if not value:
           raise ValueError("weight must not be empty")
       for i in value:
           if not isinstance(i,(int,float)):
               raise TypeError("weight must be a number")
       self._weight = value
   @property
   def bias(self):
       return self._bias
   @bias.setter
   def bias(self,value):
       if not isinstance(value,(int,float)):
#           raise TypeError("bias must be int or float")
   @property
   def parameter_count(self):
       return len(self._weight) + 1
#model = MlModel("LinearModel",[0.2,0.5,0.8,0.1],0.3)
#print(model.parameter_count)
model.weight = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
print(model.parameter_count)

class DataProcessor:
   def preprocess(self):
       print("Preprocessing")
class ModelTrainer:
   def train(self):
       print("Training")
class AIModel(DataProcessor,ModelTrainer):
   pass
model = AIModel()
model.preprocess()
model.train()

class Model:
   def run(self):
       print("Model")
class VisionModel(Model):
   def run(self):
       print("Vision Model")
       super().run()
class LanguageModel(Model):
   def run(self):
       print("Language Model")
       super().run()
class MultimodelModel(VisionModel,LanguageModel):
   def run(self):
       print("Multimodel Model")
       super().run()
#class ProductionModel(MultimodelModel):
   def run(self):
       print("Production Model")
       super().run()
production = ProductionModel()
production.run()
print(ProductionModel.mro())
