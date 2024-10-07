import pickle

# Create empty lists for faces and labels
empty_faces = []
empty_labels = []

# Save the empty lists to the pickle files
with open('C:/Users/deept/Downloads/data/faces_data.pkl', 'wb') as f:
    pickle.dump(empty_faces, f)

with open('C:/Users/deept/Downloads/data/names.pkl', 'wb') as f:
    pickle.dump(empty_labels, f)

print("All faces and labels have been cleared!")
