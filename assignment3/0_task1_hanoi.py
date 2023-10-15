def tower_of_hanoi(d, t=3, s_max=None):
    def hanoi_recursive(n, source, auxiliary, target, step_limit):
        if step_limit == 0:
            return
        if n > 0:
            # Move n-1 disks from source to auxiliary peg
            hanoi_recursive(n-1, source, target, auxiliary, step_limit)
            
            if step_limit == 0:
                return

            # Move the nth disk from source to target peg
            print(f"Move disk {n} from peg {source} to peg {target}")
            step_limit -= 1
            
            # Move n-1 disks from auxiliary peg to target peg
            hanoi_recursive(n-1, auxiliary, source, target, step_limit)
            
    hanoi_recursive(d, 0, 1, 2, s_max)

# Example usage
if __name__ == '__main__':
    num_disks = 7
    max_steps = 127
    print(f"Solving Tower of Hanoi for {num_disks} disks within {max_steps} steps:")
    tower_of_hanoi(num_disks, s_max=max_steps)
