# -*- coding:utf-8 -*-

'''
Created on 20171122
@author:wyl QQ635864540
'''
__author__ = 'wyl QQ635864540'


import urllib
import urllib2

class NGAPost:
	def __init__(self, url=None, tid=None):
		self.url = 'http://bbs.ngacn.cc/post.php'
		self.post_url = url
		self.post_tid = tid
	
	def Post(self):
		headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':'',#你的cookie
			'Host':'bbs.ngacn.cc',
			'Origin':'http://bbs.ngacn.cc',
			'Referer':'%s',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
			}
		headers['Referer'] = headers['Referer'] % self.post_url
		print 'please input your comment:'
		content = raw_input()
		#content = content.decode('utf-8').encode('gbk')
		formdata = {
			'action':'reply',
			'fid':'588',
			'tid':'%s',
			'post_content':content,
			'per_check_code':'1',
			'nojump':'1',
			'lite':'htmljs',
			'step':'2'
			}
		formdata['tid'] = formdata['tid'] % self.post_tid
		request = urllib2.Request(url=self.url, data = urllib.urlencode(formdata), headers = headers)
		response = urllib2.urlopen(request)
		html = response.read()
		print html
		response.close()
		
if __name__=='__main__':
	np = NGAPost()
	np.Post()