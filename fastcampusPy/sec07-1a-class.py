# 예제2
# self의 이해

class SelfTest:
    def functionc():  # this is class method
        print("IN fnc:class method called! class id: ", id(SelfTest))
        # MUST called by ClassName

    def functioni(self): # this is instance method
        print("IN fni:instance method called! instance id: ", id(self))
        # MUST called by InstanceName after Create


print("-------------------------------- SelfTest Class, 1111 - dir ")
print("---dir(class), dir(instance): 해당 Object(class,instance)에 대한 외형 구조 정보")
f = SelfTest()
f2 = SelfTest()

print(dir(SelfTest))
print(dir(f))
print(dir(f2))

print("-------------------------------- SelfTest Class, 222 - dict ")
print("---print(instance.__dict__) : 해당 instance의 __dict__ 정")
#print(SelfTest.__dict__) $ cant call, SelftTest is class
print(f.__dict__)
print(f2.__dict__)

print("-------------------------------- SelfTest Class, 333 - function call ")
print("---print(method call : class method call, instance method call")
SelfTest.functionc()
#f.functionc()          # cant call, functionc() is class method
#f2.functionc()

#SelfTest.finctioni()   # cant call, functioni() is instance method
f.functioni()
f2.functioni()

print("---print( id(): print id of Class,Instance,Methods")
print("---all method of class,instance has same ID")
print("id for class SelfTest(): ", id(SelfTest))
print("id for class SelfTest.f(): ", id(SelfTest.functionc()) )
print("id for instance f: ", id(f))
print("id for instance f.f(): ", id(f.functioni()) )
print("id for instance f2: ", id(f2))
print("id for instance f2.f(): ", id(f2.functioni()) )

print("=============================== F Instance, 4444 - ")
# print(SelfTest.functioni()) #예외 발생
# SelfTest.functioni() # 예외 발생
SelfTest.functioni(f)
f.functioni()

SelfTest.functioni(f2)
f2.functioni()

# python has self, therefore
# instance.method() == class.method(instance)
print("*** SAME CALL & USE: Selftest.functioni(f) == f.functioni()")
print( f.functioni() )
#print( f.functioni(f) )  #예외발생


print(".............")
print("OUT id for instance f: ",id(f2))
print("call calss, id for method : ", id(f2.functioni()) )
print("call calss, id for method : ", id(SelfTest.functioni(f2)) )
print("END use case : SelfTest class and instance =------------------------")
