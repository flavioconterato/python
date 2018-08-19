#Benchmark de GPU e CPU para Tensorflow.
#O d2 acaba não utilizando o GPU pois não utiliza a sessão, apesar de tentar usar o "device"
#Foi testado com o monitoramento de processamento de uma GTX 1060

import tensorflow as tf
import time

def f(x):
    a, b = 0, 1
    n = 0
    while n < x:
        a, b = b, a+b
        n += 1
    return a
  
print("Inicou GPU Fibonacci: {}".format(time.strftime("%X")))  
for d2 in ['/device:GPU:0']:
  with tf.device(d2):
    var1 = 0
    for i2 in range(0, 3000000):
      f(40)

print("Inicou CPU Fibonacci: {}".format(time.strftime("%X")))  
for d3 in ['/cpu:0']:
  with tf.device(d3):
    var2 = 0
    for i3 in range(0, 3000000):
      f(40)

# Creates a graph.
print("Inicou GPU: {}".format(time.strftime("%X")))
c = []
for d in ['/device:GPU:0']:
  with tf.device(d):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
    c.append(tf.matmul(a, b))
    sum = tf.add_n(c)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(sum))
print("Acabou GPU: {}".format(time.strftime("%X")))

print("Inicou CPU: {}".format(time.strftime("%X")))
# Creates a graph.
c1 = []
for d1 in ['/cpu:0']:
  with tf.device(d):
    a1 = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    b1 = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
    c1.append(tf.matmul(a, b))
    sum1 = tf.add_n(c1)
# Creates a session with log_device_placement set to True.
sess1 = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess1.run(sum1))
print("Acabou CPU: {}".format(time.strftime("%X")))
