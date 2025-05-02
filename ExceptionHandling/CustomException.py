# class UnderAgeException(Exception):

class MyClass:
    a = 2
    print("My Class")
    # def __init__(self, name):
    #     print(self)
    #     self.name = name

# Create an object (no 'new')
obj = MyClass()
print(obj.a)



"""
java-->
Class Student{
    int a  = 4;
    string name = "shiva"
    void method1(){
        this.name = "manideep"
        //some statements.
    }

    public static main(String args[]){
        Student st = new Student(); // oka object 
        st.method1();
        Student st2 = new Student(); // second object 
        print(st2.name);
    }
}
"""