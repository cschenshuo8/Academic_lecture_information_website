import re
import pandas as pd
import csv
import os

def seize_from_graph(id, graph_id, ret):
	if (os.access("Images/" + str(id) + ".csv", os.F_OK) == False):
		return ret
	df = pd.read_csv("Images/" + str(id) + ".csv")
	boxes = list(df['box'])
	txts = list(df['txt'])
	
	if (graph_id == 1):
		#讲座标题
		while ('知存讲座' not in txts[0]):
			txts.pop(0)
			boxes.pop(0)
		while ('知存讲座' in txts[0]):
			txts.pop(0)
			boxes.pop(0)
		if ('时间' not in txts[0]):
			ret[0] = txts[0]
			txts.pop(0)
			boxes.pop(0)

		#时间
		if ('时间' in txts[0]):
			ret[2] = txts[0]
			txts.pop(0)
			boxes.pop(0)
		
		#地点
		if ('地点' in txts[0]):
			ret[3] = txts[0]
			txts.pop(0)
			boxes.pop(0)

		#除去多余的文字
		txts_tmp = []
		boxes_tmp = []
		for i in range(len(txts)):
			num_list = re.findall(r"[-+]?\d+\.?\d*[eE]?[-+]?\d*", boxes[i])
			
			if (float(num_list[3]) / float(num_list[4]) < 5.0):
				txts_tmp.append(txts[i])
				boxes_tmp.append(boxes[i])
		txts = txts_tmp
		boxes = boxes_tmp

		#报告人
		ret[1] = txts[0]
		txts.pop(0)
		boxes.pop(0)

		#报告人简介
		ret[7] = txts[0]
		txts.pop(0)
		boxes.pop(0)
		
		#通知内容
		ret[6] = ''
		while (len(txts) != 0):
			ret[6] = ret[6] + str(txts[0])
			txts.pop(0)
			boxes.pop(0)

	if (graph_id == 2):
		#讲座标题
		while (re.search('第.*期', txts[0]) == None):
			txts.pop(0)
			boxes.pop(0)
		txts.pop(0)
		boxes.pop(0)
		ret[0] = ''
		while ('时间' not in txts[0]):
			ret[0] += txts[0]
			txts.pop(0)
			boxes.pop(0)
		
		#文字分组
		txts_left = []
		txts_right = []
		boxes_left = []
		boxes_right = []
		for i in range(len(txts)):
			num_list = re.findall(r"[-+]?\d+\.?\d*[eE]?[-+]?\d*", boxes[i])
			if (float(num_list[0])< 300.0):
				txts_left.append(txts[i])
				boxes_left.append(boxes[i])
			else:
				txts_right.append(txts[i])
				boxes_right.append(boxes[i])
		
		#报告人
		ret[1] = txts_left[0]
		txts_left.pop(0)
		boxes_left.pop(0)

		#时间
		ret[2] = ''
		while ('地点' not in txts_right[0]):
			ret[2] += txts_right[0]
			txts_right.pop(0)
			boxes_right.pop(0)
		
		#地点
		ret[3] = ''
		while (len(txts_right) > 0):
			ret[3] += txts_right[0]
			txts_right.pop(0)
			boxes_right.pop(0)

		#报告人简介
		ret[7] = ''
		while (len(txts_left) > 0):
			ret[7] += txts_left[0]
			txts_left.pop(0)
			boxes_left.pop(0)
	
	if (graph_id == 3):
		#讲座标题
		while (re.search('第.*期', txts[0]) == None):
			txts.pop(0)
			boxes.pop(0)
		txts.pop(0)
		boxes.pop(0)
		ret[0] = txts[0]
		txts.pop(0)
		boxes.pop(0)

		#报告人
		ret[1] = ''
		while ('时间' not in txts[0]):
			ret[1] += txts[0]
			txts.pop(0)
			boxes.pop(0)
		
		#时间
		ret[2] = txts[0]
		txts.pop(0)
		boxes.pop(0)

		#地点
		ret[3] = txts[0]
		txts.pop(0)
		boxes.pop(0)

		#通知内容
		while ('报告摘要' not in txts[0]):
			txts.pop(0)
			boxes.pop(0)
		txts.pop(0)
		boxes.pop(0)
		ret[6] = ''
		while ('报告人简介' not in txts[0]):
			ret[6] += txts[0]
			txts.pop(0)
			boxes.pop(0)
		
		#报告人简介
		txts.pop(0)
		boxes.pop(0)
		ret[7] = ''
		while (len(txts) > 0):
			ret[7] += txts[0]
			txts.pop(0)
			boxes.pop(0)

	return ret

ret = [None, None, None, None, None, None, None, None]
seize_from_graph(10, 1, ret)
print(ret)