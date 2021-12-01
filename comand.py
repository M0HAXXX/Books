import requests


books_start = []

print('--------------------------')
print('Commands:')
print('Add')
print('Read')
print('Delele')
print('Edit')
print('Exit')
print('--------------------------')

def read():
  print(books_start)



def add():
  print('book')
  name_book = str(input())
  books_start.append(name_book)
  print(books_start)
  result = requests.post('https://teasd.chsv-marasa-sha.repl.co/books', data = {
  'books_start': books_start
  })
  print(result)


def delete():
  print(books_start)
  print('delete NAME')
  delete = str(input())
  books_start.remove(delete)
  print(books_start)
  result = requests.post('https://teasd.chsv-marasa-sha.repl.co/books', data = {
  'books_start': books_start
  })
  print(result)


def edit():
  print('positions')
  numbers = int(input())
  print('edit elements')
  rename_books = input()
  position = numbers - 1
  books_start.pop(position)
  books_start.insert(position, rename_books)
  print(books_start)
  result = requests.post('https://teasd.chsv-marasa-sha.repl.co/books', data = {
  'books_start': books_start
  })
  print(result)


while True:
  request = input()
  if request == 'add':
    add()
  elif request == 'read':
    read()
  elif request == 'edit':
    edit()
  elif request == 'delete':
    delete()
  elif request == 'exit':
    print("anti-hello")
    break
  else:
    print('to retry :( ')


# result = requests.post('https://teasd.chsv-marasa-sha.repl.co/books', data = {
# 'books_start': books_start
# })
# print(result)

