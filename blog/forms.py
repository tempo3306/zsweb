# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/2 16:10
'''
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
							   widget=forms.Textarea)