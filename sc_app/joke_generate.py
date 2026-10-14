import pyjokes #m pip install pyjokes

for i in range(4):
    print(i+1,pyjokes.get_joke(category="all"))
