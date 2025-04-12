class Agent:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.score = 0

    def pick(self, cards):
        return self.strategy(cards)


def max_strategy(cards):
    if cards[0] >= cards[-1]:
        return cards.pop(0)
    else:
        return cards.pop(-1)


def min_strategy(cards):
    if cards[0] <= cards[-1]:
        return cards.pop(0)
    else:
        return cards.pop(-1)


def run_game(cards):
    max_agent = Agent("Max", max_strategy)
    min_agent = Agent("Min", min_strategy)
    agents = [max_agent, min_agent]
    turn = 0

    print("Initial Cards:", cards)

    while cards:
        agent = agents[turn % 2]
        pick = agent.pick(cards)
        agent.score += pick
        print(f"{agent.name} picks {pick}, Remaining Cards: {cards}")
        turn += 1

    print(f"Final Scores - Max: {max_agent.score}, Min: {min_agent.score}")
    if max_agent.score > min_agent.score:
        print("Winner: Max")
    elif min_agent.score > max_agent.score:
        print("Winner: Min")
    else:
        print("It's a Draw!")



cards = [1, 10, 9, 15, 10, 1] 
run_game(cards)
