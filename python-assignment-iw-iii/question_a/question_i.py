# Make pythonic solutions for each of the following data structure
# and algorithm problems.

# i) Tower of Hanoi problem for ‘n’ number of disks.

def tower_of_hanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = 3
tower_of_hanoi(n, 'X', 'Y', 'Z')
