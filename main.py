class User:

  def __init__(self, username, password):
    self.username = username
    self.password = password


user1 = User('ruben', '12345')

print(f'Username: {user1.username}')
print(f'Password: {user1.password}')
