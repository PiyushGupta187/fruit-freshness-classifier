import tensorflow as tf
import gradio as gr

model = tf.keras.models.load_model(r"D:\fruits\fruit_model.keras")

class_names = ['freshapples', 'freshbanana', 'freshoranges',
               'rottenapples', 'rottenbanana', 'rottenoranges']

def predict(img):
    img = tf.image.resize(img, (224, 224))
    img = tf.expand_dims(img, 0)
    probs = model.predict(img)[0]
    return {class_names[i]: float(probs[i]) for i in range(6)}

gr.Interface(fn=predict,
             inputs=gr.Image(),
             outputs=gr.Label(num_top_classes=3),
             title="Fruit Freshness Classifier").launch(share=True)