# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url="http://www.cnblogs.com/"
browser=webdriver.Firefox()
browser.get(url)


old_handle = browser.current_window_handle
new_handle=''


browser.find_element_by_xpath("//input[@id='zzk_q']").send_keys("selenium")
browser.find_element_by_xpath("//*[@id='search_block']/div[1]/input[2]").click()


'''
print 'old_handle����һҳ��'
print old_handle
print '�ڶ�ҳ����һҳ��browser.window_handles:'
print browser.window_handles

for handle in browser.window_handles:
    if old_handle != handle:
        new_handle = handle
        break
# �л����´�����,����´����еİ�ť
browser.switch_to.window(new_handle)

#for handle in browser.window_handles:
#    browser.switch_to.window(handle)
'''
browser.find_element_by_xpath("//*[@id='searchResult']/div[2]/div[1]/h3/a").click()
##################################################

old_handle = browser.current_window_handle
new_handle=''

print 'old_handle����һҳ��'
print old_handle
print '�ڶ�ҳ����һҳ��browser.window_handles:'
print browser.window_handles

for handle in browser.window_handles:
    if old_handle != handle:
        new_handle = handle
        break
print '�ڶ�ҳ'
print new_handle
print ''
########################################################
browser.switch_to.window(new_handle)
browser.find_element_by_xpath("//*[@id='MySignature']/p/a[2]").click()
print '����ҳ'
time.sleep(2)
print browser.window_handles[-1]
print '��ʾ����ҳ����'
print browser.window_handles
print ''
########################################################

#�лص��ڶ�ҳ���ٴδ���ͬ���ӣ��½�ҳ��
browser.switch_to.window(new_handle)
browser.find_element_by_xpath("//*[@id='MySignature']/p/a[2]").click()
time.sleep(2)
print '����ҳ'
print  browser.window_handles[-1]
print '��ʾ����ҳ����'
print browser.window_handles

handles=browser.window_handles
browser.switch_to.window(handles[1])
print handles[1]
print browser.title




