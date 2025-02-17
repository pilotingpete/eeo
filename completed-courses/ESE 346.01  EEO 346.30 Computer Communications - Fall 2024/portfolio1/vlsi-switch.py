import random
import matplotlib.pyplot as plt

def simulate_switching_elements(num_slots, p):
    throughput_A = 0
    throughput_C = 0
    
    for _ in range(num_slots):
        # Step 1: Randomly generate arrivals at A and B based on probability p
        packet_A = random.random() < p  # True if a packet arrives at A
        packet_B = random.random() < p  # True if a packet arrives at B

        # Step 2: Process the switching element logic for A and B
        if packet_A and packet_B:
            # Both packets arrive, randomly discard one
            if random.random() < 0.5:
                output_A = True  # A forwards
            else:
                output_A = True  # B forwards
        elif packet_A or packet_B:
            # Only one packet arrives
            output_A = True
        else:
            output_A = False
        
        # Step 3: Process the output of C
        packet_C = output_A  # Only one input at C
        output_C = packet_C  # Forward the packet to C if it arrives
        
        # Step 4: Collect throughput statistics
        if output_A:
            throughput_A += 1
        if output_C:
            throughput_C += 1
    
    # Normalized throughput
    normalized_throughput_A = throughput_A / num_slots
    normalized_throughput_C = throughput_C / num_slots
    return normalized_throughput_A, normalized_throughput_C

# Simulation parameters
num_slots = 1000  # Increase for more accuracy
p_values = [i / 1000 for i in range(25, 1001, 25)]
throughput_A_list = []
throughput_C_list = []

# Outer loop: Vary p from 0.025 to 1.0
for p in p_values:
    norm_throughput_A, norm_throughput_C = simulate_switching_elements(num_slots, p)
    throughput_A_list.append(norm_throughput_A)
    throughput_C_list.append(norm_throughput_C)

# Plotting the results
plt.plot(p_values, throughput_A_list, label="Element A Throughput")
plt.plot(p_values, throughput_C_list, label="Element C Throughput")
plt.xlabel('Probability (p)')
plt.ylabel('Normalized Throughput')
plt.title('Throughput of Switching Elements A and C vs Probability p')
plt.legend()
plt.show()
