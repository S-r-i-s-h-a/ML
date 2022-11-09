#reduce hdf5

 #Slow write Fast read
    with h5py.File("test_h5py.hdf5","a") as f:
        dset = f.create_dataset("uncompchunk",(height,width,dataLen),chunks = (height,width,1), dtype = 'f')
        for i in range(height):
            for j in range(width):
                dset[i,j,:] = np.random.random(200000)
                
                
 #2
  #Fast write Slow read
    with h5py.File("test_h5py.hdf5","a") as f:
        dset = f.create_dataset("uncompchunk",(height,width,dataLen),chunks = (1,1,dataLen), dtype = 'f')
        for i in range(height):
            for j in range(width):
                dset[i,j,:] = np.random.random(200000)
                
