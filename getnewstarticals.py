# -*- coding:utf-8 -*-

'''
Created on 20171122
@author:wyl QQ635864540
'''
__author__ = 'wyl QQ635864540'

import urllib
import urllib2
import re
import time

import postcomment


class GetNewestArticals:
	def __init__(self):
		self.url = 'http://bbs.ngacn.cc/thread.php?fid=-7'
		self.compiler = re.compile(r'href=\'([^\s]*?)\'[\s]*id=', re.IGNORECASE)
		self.headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Cookie':'',#你的cookie
			'Host':'bbs.ngacn.cc',
			'Referer':'http://bbs.ngacn.cc/thread.php?fid=-7',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
			}
		self.commentcompiler = re.compile(r'class=\'forumbox postbox\'', re.IGNORECASE)
		self.multipagecompiler = re.compile(r'(name=\'pageball\' id=\'pagebtop\'[^\\\\]*?</div>)', re.IGNORECASE)
		self.titlecompiler = re.compile(r'id=\'postsubject0\'>([^\t\n\r\f\v]*?)</h3>',re.IGNORECASE)
		self.contentcompiler = re.compile(r'id=\'postcontent0\' class=\'postcontent ubbcode\'>([^\t\n\r\f\v]*?)</p>', re.IGNORECASE)
		
	def SearchArticals(self):
		result = []
		try:
			request = urllib2.Request(url=self.url, headers=self.headers)
			response = urllib2.urlopen(request)
			html = response.read()
			#print html
			response.close()
			result = self.compiler.findall(html)
		except Exception as e:
			print 'Exception in SearchArticals:',str(e)
		return result
		
	def GetZeroCommentAr(self, results=None):
		headurl = 'http://bbs.ngacn.cc'
		commentcount = 0
		for res in results:
			normalurl = headurl + res
			try:
				request = urllib2.Request(url=normalurl, headers = self.headers)
				response = urllib2.urlopen(request)
				html = response.read()
				response.close()
				comments = self.commentcompiler.findall(html)
				commentcount=len(comments)-1
				if commentcount != 0:
					continue
				pages = self.multipagecompiler.findall(html)
				titles = self.titlecompiler.findall(html)
				print 'url:',normalurl
				print 'title:'
				print titles[0]
				contents = self.contentcompiler.findall(html)
				contentresult = contents[0].replace('<br/>','\n')
				print 'content:'
				print contentresult
				print '**********************************'
				print '**********************************'
				print '**********************************'
				print 'input 0 to get next artical, otherwise you need to input your comment.'
				select = raw_input()
				if select == '0':
					return
				if normalurl.find('tid=') == -1:
					print 'no tid found in:',normalurl
					return
				tid = normalurl[normalurl.find('tid=') + 4:]
				pm = postcomment.NGAPost(normalurl, tid)
				pm.Post()
				#print html
				#print 'page:',pages[0]
				#print normalurl,commentcount,' comments...'
				#print '..............'
			except Exception as e:
				print 'Exception in GetZeroCommentAr:',str(e)
		
				
				
			
if __name__=='__main__':
	gna=GetNewestArticals()
	while True:
		results = gna.SearchArticals()
		gna.GetZeroCommentAr(results)