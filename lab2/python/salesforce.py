from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("../../models/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("../../models/blip-image-captioning-base")

def generateCaption(image_path):
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert(mode="RGB")
    
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    
    return processor.decode(out[0], skip_special_tokens=True)  