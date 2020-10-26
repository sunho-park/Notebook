import tensorflow as tf
from tensorflow import keras

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.6):
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True
def solution_model():
    fashion_mnist = tf.keras.datasets.fashion_mnist


    # YOUR CODE HERE
    
    mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 28, 28, 1)
    x_train = x_train / 255.0
    
    y_test = y_test.reshape(10000, 28, 28, 1) 
    test_images = test_images/255.0
   
    callbacks = myCallback()

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu'),
        tf.keras.layers.Maxpooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    
    model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
    
    loss = model.evaluate(x_test, y_test)
    
    return model
