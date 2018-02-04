def saveimg(directory_path, size = [50, 50], is_gun = True):
	"""
	directory_path is an arg that designates the path to pictures with guns/non-guns
	size is a kwarg designating the size of the picture to crop later

	Basically, place all of your gun pictures in the same directory.

	"""
	import os
	from PIL import Image as img
	from resizeimage import resizeimage
	import numpy as np


	if directory_path.endswith("/"):
		ending = ""
	else:
		ending = "/"

	img_list = []
	for files in os.listdir(directory_path):
	    if files.endswith("jpg") or files.endswith("png"):
	        demo = open(directory_path + ending + files, "rb")
	        echantillon = img.open(demo)
	        cover = resizeimage.resize_contain(echantillon, size)
	        demo.close()
	        img_list.append(np.array(cover))

	if is_gun == True:
		gun = [1 for i in range(len(img_list))]
	else:
		gun = [0 for i in range(len(img_list))]

	return((img_list, gun))

def img_list(gun_path, non_gun_path = None, size = [50, 50], is_gun = True):

	"""
	gun_path and non_gun_path are paths to the gun/non_gun images
	size
	
	size is a kwarg designating the size of the picture to crop later

	Basically, place all of your gun pictures in the same directory.
	Also, place all of your non_gun pictures in another directory.

	Returns a list containing two lists: a list of gun and non_gun images in the first list
	and a second list identifying each image (0 for non-gun, and 1 for gun).

	"""
	gun = saveimg(gun_path, size, is_gun)

	if non_gun_path != None:
		non_gun = saveimg(non_gun_path, size, is_gun = False)

		for i, j in zip(non_gun[0], non_gun[1]):
			gun[0].append(i)
			gun[1].append(j)
	return(gun)

def grayscaling(gun_path, non_gun_path = None, size = [50, 50]):
	"""
	This function returns grayscaled images.
	"""
	from skimage.color import rgb2gray
	from skimage.exposure import equalize_hist

	gray_img = img_list(gun_path, non_gun_path, size)

	for num, colour_images in enumerate(gray_img[0]):
		grayscaled_img = rgb2gray(colour_images)
		equalized_image = equalize_hist(grayscaled_img)
		gray_img[0][num] = equalized_image

	return(gray_img)

def formatting(gun_list):
	nnlist = []
	for i in gun_list:
	    nlist = []
	    for j in i:
	        for k in j:
	            nlist.append(k)
	    nnlist.append(nlist)

	return(nnlist)

def training(gun_path, non_gun_path, size = [50, 50]):
	"""
	Trains a ML model using SVM from scikit learn
	"""
	from sklearn import model_selection, svm

	gray_img_list, gun = grayscaling(gun_path, non_gun_path, size)
	X_train, X_test, y_train, y_test = model_selection.train_test_split(gray_img_list, gun, test_size = 0, shuffle = True)

	X_train = formatting(X_train)
	
	clf = svm.SVC()

	#fit SVM to training data
	clf.fit(X_train[0:-1], y_train[0:-1])

	return(clf)

def predict(clf, img_path, loop = False):
	"""
	clf is the output of the function training
	img_path is the path of the image to predict
	loop will loop for user inputting an image path to predict until they hit @
	This function predicts whether the image presented is a gun or not.

	"""
	new_img = grayscaling(img_path)
	formatted = formatting(new_img[0])

	prediction = clf.predict(formatted)
	prediction = int(prediction[0])
	
	if prediction == 0:
		print("The machine predicts that there is no gun.")
		return(prediction)
	elif prediction == 1:
		print("The machine predicts that there is a gun.")
		return(prediction)
	else:
		print("The machine is broken.")


def save(clf):
	from sklearn.externals import joblib

	joblib.dump(clf, "C:/pythonfiles/mchacks/saveddata.pkl")

#foo = training("C:/pythonfiles/mchacks/gun_examples", "C:/pythonfiles/mchacks/no_guns")
#save(foo)

"""boo = predict(foo, "C:/pythonfiles/mchacks")

print(boo)
print(type(boo))"""