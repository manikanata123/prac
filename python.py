class A():
 def MyMethod(self):
  print("Iam in Class A")
class B():
  def MyMrthod(self):
   print("Iam in Class B")
class C(B,A):
 def MyMethod(self):
  print("I am Class C")
 
def main():
 obj=C()
 obj.MyMethod()
 
if __name__ = "__main__":
 main()
 
 
 
#Thanks :)
