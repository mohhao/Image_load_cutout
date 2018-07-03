# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:15:32 2018

@author: Administrator
"""
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys
#import shutil

global count1, count2
count1 = count2 =0

def file_segmentation(lBound, rBound):
	dataSet = []
	for i in range(lBound, rBound):
		if os.path.exists('Shot_%d.txt' % i):
			with open('Shot_%d.txt' % i, 'r') as f:
				lines = f.readlines()
				ls = len(lines)
				for j in range(ls):
					lineArr = []
					line = lines[j].strip().split('       ')
					l = len(line)
					for k in range(l):
						la = line[k].strip()
						if la == '':
							pass
						else:
							lineArr.append(np.float32(la))
					dataSet.append(lineArr)
		else:
			pass
	length = len(dataSet)
	return dataSet, length

def normalization(dataMat):
	minVals = dataMat.min(0)
	maxVals = dataMat.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataMat))
	m = dataMat.shape
	normDataSet = dataMat - np.tile(minVals, m)
	normDataSet = normDataSet/np.tile(ranges, m)
	return normDataSet

# def check_filename_available(filename):
# 	def check_meta(file_name):
# 		n=[0]
# 		file_name_new=file_name
# 		if os.path.isfile(file_name):
# 			file_name_new=file_name[:file_name.rfind('.')]+'_'+str(n[0])+file_name[file_name.rfind('.'):]
# 			n[0] += 1
# 		if os.path.isfile(file_name_new):
# 			file_name_new=check_meta(file_name)
# 		return file_name_new
# 	return_name=check_meta(filename)
# 	return return_name

def cutout_pictures(firstArrival_point, finalDataMat, stride):
	global count1,count2
	axis_x = np.array(np.linspace(0, 3500, 876))	
	for i in range(876-stride):
		plt.figure(figsize=(2.99,2.99))
		plt.rcParams['savefig.dpi'] = 100
		plt.axis('off')	
		plt.subplots_adjust(top = 1, bottom = 0, 
							right = 1, left = 0,
							hspace = 0, wspace = 0)
		plt.margins(0,0)
		x = axis_x[i:i+stride+1]
		y = finalDataMat[i:i+stride+1]
		plt.plot(x, y, color = 'k', linewidth = 1.5)
		if firstArrival_point in x:
			# plt.savefig(check_filename_available('trainSet1\\1.jpg'))
			filename1 = ('trainSet\\1_%d.jpg' %count1)
			plt.savefig(filename1)
			count1 += 1
		else:
			filename2 = ('trainSet\\0_%d.jpg' %count2)
			#plt.savefig(check_filename_available('trainSet1\\0.jpg'))
			plt.savefig(filename2)	
			count2 += 1
		# plt.show()
		plt.close("all")
		sys.stdout.flush()
		#plt.clf()

# for i in range(13378,13538):
#   for j in range(20000):
#     os.chdir('d:\\1wyh\\2zhenyuan_huizong')
#     text = ('{:}_shuchu_{:}.txt'.format(i,j))
#     if not os.path.exists(text):
#       break
#     else:
#       file = ('%d' %i)
#       shutil.move(text, file)

if __name__ == '__main__':
	dataSet, dataSet_len = file_segmentation(13369, 13370)
	for i in range(int(dataSet_len/2), dataSet_len):		
		dataSet_segmentation = dataSet[i][12:]
		firstArrival_point = dataSet[i][11]
		if firstArrival_point == 0:
			pass
		else:
			dataMat = np.array(dataSet_segmentation)
			normDataSet = normalization(dataMat)
			cutout_pictures(firstArrival_point, normDataSet, 6)
	# dataSet_segmentation = dataSet[0][12:]
	# dataMat = np.array(dataSet_segmentation)
	# normDataSet = normalization(dataMat)
	# # print(dataSet_segmentation)
	# # print(dataMat)
	# # print(normDataSet)
	# plt.figure(figsize=(29.9,2.99))
	# plt.axis('off')	
	# plt.subplots_adjust(top = 1, bottom = 0, 
	# 					right = 1, left = 0,
	# 					hspace = 0, wspace = 0)
	# plt.margins(0,0)
	# axis_x = np.array(np.linspace(0, 3500, 876))
	# # x = axis_x[i:i+stride+1]
	# # y = finalDataMat[i:i+stride+1]
	# plt.plot(axis_x, normDataSet, color = 'k', linewidth = 1.5)
	# plt.show()