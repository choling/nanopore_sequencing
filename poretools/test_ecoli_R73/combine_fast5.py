import h5py
#for every dataset Dn.h5 you want to merge to Output.h5 
f = h5py.File('\*\.fast5','r+') #file to be merged 
h5_keys = f.keys() #get the keys (You can remove the keys you don't use)
f.close() #close the file
for i in h5_keys:
        h5copy -i '*.fast5' -o 'test_all.fast5' -s {i} -d {i}
