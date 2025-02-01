class Enviroment:
  def __init__(self):
    self.backups = ['failed','completed','completed','failed','completed']

  def act(self):
    for i in  range(len(self.backups)):
      if self.backups[i]=='failed':
        self.backups[i]='completed'

  def get_percept(self,position):
    return self.backups[position]

  def show_backups(self):
    print(f' | '.join(self.backups))

class Agent:
  def __init__(self):
    self.position = 0

  def act(self,percept,enviroment):
    enviroment.act()

  def move(self):
    if self.position<4:
      self.position+=1

def RunAgent(agent, enviroment, steps):
  for i in range(steps):
    print(f'\nstep {i}:')
    percept = enviroment.get_percept(i)  
    agent.act(percept,enviroment)

    print(f"Agent Position {agent.position} -> Percept: {percept}")
    enviroment.show_backups()
        
    agent.move() 
  
agent = Agent()
enviroment = Enviroment()
enviroment.show_backups()
RunAgent(agent,enviroment,5) 
