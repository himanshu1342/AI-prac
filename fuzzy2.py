# Define two fuzzy sets A and B
A = fuzz.trimf(x, [0, 5, 10])
B = fuzz.trimf(x, [3, 6, 9])

# Perform fuzzy operations
fuzzy_and = np.fmin(A, B)
fuzzy_or = np.fmax(A, B)
fuzzy_not_A = 1 - A

# Plot results
plt.figure(figsize=(10, 6))

plt.plot(x, A, 'b', label='A')
plt.plot(x, B, 'g', label='B')
plt.plot(x, fuzzy_and, 'r--', label='A AND B')
plt.plot(x, fuzzy_or, 'm--', label='A OR B')
plt.plot(x, fuzzy_not_A, 'k--', label='NOT A')

plt.title('Fuzzy Logic Operations')
plt.xlabel('x')
plt.ylabel('Membership')
plt.legend()
plt.grid(True)
plt.show()
