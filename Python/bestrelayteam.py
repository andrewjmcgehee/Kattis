# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/bestrelayteam
# Complexity: O(N^2) where N is number of runners
# Memory: O(N) for N runners

num_runners = int(input())
runners = dict()

# represent runners as tuple of first leg time to avg leg time
for i in range(num_runners):
  ins = input().split()
  runners[ins[0]] = (float(ins[1]), float(ins[2]))

# initial best set to an impossible value
best_time = 1000000
starter = None
followers = set()

# trie each runner as a starter
for runner in runners:
  temp_time = runners[runner][0]
  temp_starter = runner
  temp_followers = set()
  # get three best leg runners aside from starter, could sort here but would
  # have to define sort to work based on 2nd item in tuple
  for i in range(3):
    leg_time = 1000000
    leg_runner = None
    for runner in runners:
      if runner != temp_starter and runner not in temp_followers:
        if runners[runner][1] < leg_time:
          leg_runner = runner
          leg_time = runners[runner][1]
    temp_followers.add(leg_runner)
    temp_time += leg_time
  # take best time and set starter and followers
  if temp_time < best_time:
    starter = temp_starter
    followers = temp_followers
    best_time = temp_time

print(best_time)
print(starter)
for runner in followers:
  print(runner)
