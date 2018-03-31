import pytest
import os
import application

def test_save_img():
    img_url = 'https://i1.wp.com/yroy.me/wp-content/uploads/2017/04/elephant.jpeg'
    img_file = application.save_img(img_url)
    with open(img_file, 'r') as f:
    	read_data = f.read()

def test_get():
	response = application.get()
	print(src(response))

# def test_post():
# 	response = application.post()
# 	print(src(response))
