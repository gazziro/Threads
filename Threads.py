#!/usr/bin/env python
# coding: utf-8

# In[1]:


import multiprocessing


# In[2]:


multiprocessing.cpu_count()


# In[3]:


import threading
import urllib.request
import time


# In[4]:


def downloadImagens(imagePath, fileName):
    print("Realizando o download... ",imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    
t0 = time.time()
for i in range(10):
    imageName = "imagens/image-"+str(i)+".png"
    downloadImagens("http://lorempixel.com.br/500/400/?1", imageName)
t1 = time.time()
totalTime = t1 - t0
print("Tempo total de execução {}".format(totalTime))


# In[12]:


def downloadImagens(imagePath, fileName):
    print("Realizando o download... ",imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Download finalizado")
def executeThread(i):
    imageName = "imagens_thread/image-"+str(i)+".png"
    downloadImagens("http://lorempixel.com.br/500/400/?1", imageName)
t0 = time.time()
threads = []

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(1,))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()
t1 = time.time()
totalTime = t1 - t0
print("Tempo total de execução {}".format(totalTime))


# In[5]:


import threading
import time
from random import randint


# In[6]:


def funcao_1(num):
    n = num
    while n > 0:
        n -= 1
        print("n_1: {}".format(n))
        time.sleep(randint(0,1))

def funcao_2(num):
    n = num
    while n <10:
        n += 1
        print("n_2: {}".format(n))
        time.sleep(randint(0,1))
        
if __name__ == '__main__':
    t1 = threading.Thread(target=funcao_1, args=(10,))
    t2 = threading.Thread(target=funcao_2, args=(0,))   
    t1.start()
    t2.start()

    print("FIM!")


# In[ ]:




