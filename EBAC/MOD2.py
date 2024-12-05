movies = ["spiderman", "iron man", "die hard", "spiderman", "iron man", "die hard"]
newlist = set(movies)
newmovieslist = list(newlist)
movies.insert(2,"iception")
movies.pop()
# dictionarys
listpeople=[{
    'name': "joao",
    'age': 29,
    'cash': 8000.00
}]

listpeople.insert(1,{'name': "iza",'age': 19,'cash': 2.00})
listpeople.insert(1,{'name': "fulano",'age': 0,'cash': 0.00})
listpeople.pop()
print(listpeople)