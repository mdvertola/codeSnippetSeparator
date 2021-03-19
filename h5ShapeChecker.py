

import h5py
# filename = "data/train.methname.h5"
# filename = "data/train.git_token.txt"
filename = "data/train.tokens.h5"
# filename = "data.h5"

with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])
    print(data[0])

# hf = h5py.File('data.h5', 'w')

# hf.create_dataset('dataset', data=filename)
