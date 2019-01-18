# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/areyoulistening
# Complexity: O(N) where N is the optimal radius size
# Memory: O(N) for N listening devices

# helper method for determining how many sensors are detecting
def touching_sensors(x, y, r, devices):
  touching = 0
  for dev in devices:
    delta_x = x - dev[0]
    delta_y = y - dev[1]
    # use squares to avoid floating point
    distance = delta_x**2 + delta_y**2
    coverage = (r + dev[2])**2
    # strictly grater than to intersect circle at 2 points
    if coverage > distance:
      touching += 1
  return touching

def main():
  # start location
  cx, cy, n = map(int, input().split())

  # holds device locations and radii
  devices = []
  for i in range(n):
    x, y, r = map(int, input().split())
    devices.append((x, y, r))

  # start at 0 and increase
  # could be made faster with binary search
  radius = 0
  touching = touching_sensors(cx, cy, radius, devices)
  while touching < 3:
    radius += 1
    touching = touching_sensors(cx, cy, radius, devices)

  if radius != 0:
    print(radius-1)
  # edge case if radius 0 is already detected by 3 sensors
  else:
    print(radius)

if __name__ == "__main__":
  main()
