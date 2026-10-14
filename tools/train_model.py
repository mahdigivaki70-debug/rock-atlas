#!/usr/bin/env python3
"""Trains an on-device stone classifier for the app's photo identification.

Folder layout (one folder per stone id or stone type id from seed.json):
    photos/
      mahallat_cream/  img1.jpg img2.jpg ...
      carrara/         ...
      granite/         ...   (a type id works too and covers every stone of that type)

Usage:
    pip install tensorflow
    python3 tools/train_model.py photos/

Writes app/src/main/assets/stone_model.tflite and stone_labels.txt. Rebuild the
app and the identification screen will use the model automatically. Use only
photos you have the right to use; aim for 50+ varied photos per class.
"""
import pathlib
import sys

import tensorflow as tf

IMG = 224


def main(data_dir: str) -> None:
    root = pathlib.Path(__file__).resolve().parent.parent
    train = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="training", seed=7, image_size=(IMG, IMG), batch_size=32)
    val = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="validation", seed=7, image_size=(IMG, IMG), batch_size=32)
    labels = train.class_names

    base = tf.keras.applications.MobileNetV3Small(input_shape=(IMG, IMG, 3), include_top=False, weights="imagenet")
    base.trainable = False
    augment = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal_and_vertical"),
        tf.keras.layers.RandomRotation(0.2),
        tf.keras.layers.RandomContrast(0.2),
    ])
    inputs = tf.keras.Input((IMG, IMG, 3))  # raw 0..255 pixels, as the app sends them
    x = augment(inputs)
    x = base(x, training=False)  # MobileNetV3 includes its own rescaling
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = tf.keras.layers.Dense(len(labels), activation="softmax")(x)
    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(train, validation_data=val, epochs=15)

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    assets = root / "app/src/main/assets"
    (assets / "stone_model.tflite").write_bytes(converter.convert())
    (assets / "stone_labels.txt").write_text("\n".join(labels) + "\n")
    print(f"saved model with {len(labels)} labels to {assets}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
