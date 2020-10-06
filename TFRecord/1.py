import tensorflow as tf

with tf.io.TFRcordWriter("my_data.tfrecord") as f:
    f.write(b"this is  the first record")
    f.write(b"And this is the second record")

filepaths = ["my_data.tfrecord"]
dataset = tf.data.TFRecordDataset(filepaths)
for item in dataset:
    print(item)
