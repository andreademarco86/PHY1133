import numpy as np

# Generate vectors:
vector_1 = np.random.random(100)
vector_2 = np.random.random(100)

# Compute scalar product
current_sum = 0
for i in range(len(vector_1)):
    current_sum += vector_1[i] * vector_2[i]

# Print result
print("Scalar product is", current_sum)

# Note, if using numpy this can be performed as follows:
print("Scalar product is", np.sum(vector_1 * vector_2))
# Or
print("Scalar product is", np.dot(vector_1, vector_2))
