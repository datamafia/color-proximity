#!/usr/bin/env python
# datamafia.com github @datamaifa see readme.md for information

from __future__ import division
from math import sqrt, pow

class color_proximity(object) :
	
	def __init__(self):
		pass
	
	def proximity(self, a, b):
		"""Return proximity value of a pair RGB tuple or list"""
		
		'''
		Init, convert list/tupel of int,int,int to color proximity value
		Args:
			a : required, int, 0-255 RGB color value
			b : required, int, 0-255 RGB color value
		Returns :
			float
		'''
		
		# support for RBG+alpha, slice to ignore alpha
		if len(a) > 3 :
			a = a[:3]
		if len(b) > 3 :
			b = b[:3]
		c1 = self.rgb2lab(a) # int int int
		c2 = self.rgb2lab(b)
		
		return sqrt(pow(c1[0]-c2[0],2)+pow(c1[1]-c2[1],2)+pow(c1[2]-c2[2],2))
	
	def rgb2lab(self, c):
		"""RGB to L.a.b. conversion"""
		
		'''
		Transform (int, int, int) from RGB to XYZ (CIE1931) to L.a.b.
			http://en.wikipedia.org/wiki/CIE_1931_color_space
			http://en.wikipedia.org/wiki/Lab_color_space
		Args:
			c : required, tuple/list of 3 int (RGB)
		Return :
			Lab value as 3 element list
		'''
		
		rgb = [0,0,0]
		xyz = [0,0,0]
		Lab = [0,0,0]
	
		i = 0
		while len(c) > i :
			value = float(c[i]/255)
			if value > 0.04045 :
				value = pow(((value+0.055 )/1.055), 2.4)
			else :
				value = value / 12.92
			rgb[i] = value * 100
			i += 1
		
		xyz[0] = (rgb[0] * 0.4124 + rgb[1] * 0.3576 + rgb[2] * 0.1805) / 95.047
			#// ref_X =  95.047   Observer= 2deg, Illuminant= D65
		xyz[1] = (rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722) / 100.0
			#// ref_Y = 100.000
		xyz[2] = (rgb[0] * 0.0193 + rgb[1] * 0.1192 + rgb[2] * 0.9505) / 108.883
			#// ref_Z = 108.883
		
		i = 0
		while len(xyz) > i :
			value = xyz[i];
			if(value > 0.008856) :
				value = pow(value,1/3);
			else :
				value = (7.787*value)+(16/116);
			xyz[i] = value;
			i += 1
		
		Lab[0] = round((( 116 * xyz[1]) - 16), 3)
		Lab[1] = round(( 500*(xyz[0]-xyz[1])), 3)
		Lab[2] = round(( 200*(xyz[1]-xyz[2])), 3)
		
		return Lab