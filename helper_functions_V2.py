import tensorflow as tf

def model_prediction_class(model_name, test_data, sample_number):
  class_list = test_data.class_names 
  pred_prob = mode_name.predict(test_data)
  class_index = pre_prob[sample_number].argmax()
  print(f"Number of prediction probabilities for sample {sample_number} are len(pred_prob[sample_number])")
  print(f"Shape of prediction probabilities for this model: {pred_prob.shape}")
  print(f"predicted class index by the model for this sample: {class_index}")
  print(f"predicted class name by this model for this sample: {class_list[class_index]}")

