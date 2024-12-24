from data import beta
def phraser(p):
  def alpha(y):
    if y == ' ': return ' ' * 49
    if not y.isalpha(): raise ValueError
    return "".join([*map(lambda x: y.upper() if x == '1' else ' ', [*bin(beta[ord(y.upper()) - 65])[3:]])])
  q = []
  for r in p:
    q.append(alpha(r))
  for i in range(7):
    j = i * 7
    k = j + 7
    for r in q:
      print (r[j:k], end="")
    print ()
  print()

phraser("Whitecaps on the bay")
phraser("A broken signboard banging")
phraser("In the April wind")
# — Richard Wright, collected in Haiku: This Other World, 1998

# F11 for full screen in portrait view
# CTRL + - until it renders as three lines of text
