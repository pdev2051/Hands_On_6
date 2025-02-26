import matplotlib.pyplot as plt

sizes = [1000, 5000, 10000, 20000, 50000]
best_case_times = [256000, 73500, 127200, 386300, 635700]
worst_case_times = [160100, 123800, 195600, 438100, 914700]
average_case_times = [107400, 256200, 503400, 1056700, 3876600]

plt.figure(figsize=(10, 6))
for times, label, color in zip([best_case_times, worst_case_times, average_case_times],
                               ['Best Case (ns)', 'Worst Case (ns)', 'Average Case (ns)'],
                               ['green', 'red', 'blue']):
    plt.plot(sizes, times, marker='o', label=label, color=color, linestyle='-')

plt.title('Quicksort Benchmarking')
plt.xlabel('Array Size')
plt.ylabel('Time (nanoseconds)')
plt.xscale('log')
plt.yscale('log')
plt.xticks(sizes)
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.show()
