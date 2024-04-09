from te import Te

te_negro = Te()
te_verde = Te()

print(type(te_negro)) #<class 'te.Te'>
print(type(te_verde)) #<class 'te.Te'>

if type(te_negro) == type(te_verde):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")