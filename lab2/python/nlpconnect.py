from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("../../models/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("../../models/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("../../models/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_path):
  image = Image.open(image_path)

  if image.mode != "RGB":
    image = i_image.convert(mode="RGB")

  pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  return preds[0]
