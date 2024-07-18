#K-fold_test.py
k = 4
data = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]
#validation_data = [17, 18, 19, 20]
num_validation_samples = len(data) // k
#np.random.shuffle(data)
validation_scores = []
#validation_data = []
for fold in range(k):
validation_data = data[num_validation_samples * fold:
num_validation_samples * (fold + 1)]
training_data = data[:num_validation_samples * fold] + data[num_validation_samples * (fold + 1):]