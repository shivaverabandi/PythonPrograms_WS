
try:
    manideep = open("C:\\Users\\V.SHIVA\\PythonPrograms_WS\\ExceptionHandling\\text.txt",'r')
    content = manideep.read()
    print(type (manideep))
    print(content)


except FileExistsError:
    print("file not there")
except FileNotFoundError:
    print("file path error")

except BaseException:
    print("base class")
    
except Exception:
    print("general error")
else :
    print("try block run successfully")

finally:
    print("I will excute even after try block or catch no matter i will execute")

# Parent extends Child{}

# Parent obj = new Child()