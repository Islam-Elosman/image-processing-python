import numpy as np
import cv2
# Read the image in greyscale
img = cv2.imread("forest.jpg", cv2.IMREAD_GRAYSCALE)

#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits
lst1 = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst1.append(np.binary_repr(img[i][j], width=16))  # width = no. of bits
lst2 = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst2.append(np.binary_repr(img[i][j], width=24))  # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
twentyfuor_bit_img = (np.array([int(i[0]) for i in lst2],dtype = np.uint32) * 8388608 ).reshape(img.shape[0],img.shape[1])
twentythree_bit_img = (np.array([int(i[1]) for i in lst2],dtype = np.uint32) * 4194304).reshape(img.shape[0],img.shape[1])
twentytwo_img = (np.array([int(i[2]) for i in lst2],dtype = np.uint32) * 2097152 ).reshape(img.shape[0],img.shape[1])
twentyone_bit_img = (np.array([int(i[3]) for i in lst2],dtype = np.uint32) * 1048576).reshape(img.shape[0],img.shape[1])
twenty_bit_img = (np.array([int(i[4]) for i in lst2],dtype = np.uint32) * 524288 ).reshape(img.shape[0],img.shape[1])
nineteen_bit_img = (np.array([int(i[5]) for i in lst2],dtype = np.uint32) * 262144 ).reshape(img.shape[0],img.shape[1])
eighteen_bit_img = (np.array([int(i[6]) for i in lst2],dtype = np.uint32) * 131072 ).reshape(img.shape[0],img.shape[1])
seventeen_bit_img = (np.array([int(i[7]) for i in lst2],dtype = np.uint32) * 65536).reshape(img.shape[0],img.shape[1])

sixteen_bit_img = (np.array([int(i[0]) for i in lst1],dtype = np.uint8) * 23768).reshape(img.shape[0],img.shape[1])
fifteen_bit_img = (np.array([int(i[1]) for i in lst1],dtype = np.uint8) * 16384 ).reshape(img.shape[0],img.shape[1])
fourteen_bit_img = (np.array([int(i[2]) for i in lst1],dtype = np.uint8) * 8192).reshape(img.shape[0],img.shape[1])
thirteen_bit_img = (np.array([int(i[3]) for i in lst1],dtype = np.uint8) * 4036 ).reshape(img.shape[0],img.shape[1])
twentyfour_bit_img = (np.array([int(i[4]) for i in lst1],dtype = np.uint8) * 2048 ).reshape(img.shape[0],img.shape[1])
eleven_bit_img = (np.array([int(i[5]) for i in lst1],dtype = np.uint8) * 1024).reshape(img.shape[0],img.shape[1])
ten_bit_img = (np.array([int(i[6]) for i in lst1],dtype = np.uint8) * 512).reshape(img.shape[0],img.shape[1])
nine_bit_img = (np.array([int(i[7]) for i in lst1],dtype = np.uint8) * 256 ).reshape(img.shape[0],img.shape[1])

eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])


# Display the images

cv2.imshow('eight bit',eight_bit_img)
cv2.imshow('sixteen bit', sixteen_bit_img)
cv2.imshow('twentyfour bit', twentyfour_bit_img)

cv2.waitKey(0)



