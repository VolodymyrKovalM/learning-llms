import { useState, useCallback } from 'react';
import { Carousel } from 'react-responsive-carousel';

import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './App.css';

const models = [
  {
    name: 'nlpconnect/vit-gpt2-image-captioning',
    value: 'nlpconnect',
  },
  {
    name: 'Salesforce/blip-image-captioning-base',
    value: 'salesforce',
  }
];

function App() {
  const [isGenerating, setIsGenerating] = useState(false);
  const [model, setModel] = useState(models[0].value);
  const [image, setImage] = useState(null);

  const [imageSrc, setImageSrc] = useState('');
  const [imageCaption, setImageCaption] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    const reader = new FileReader();
      
    reader.onloadend = () => {
      setImageSrc(reader.result);
    };
      
    reader.readAsDataURL(file);

    setImage(file);
  };
  
  const handleSubmit = useCallback(async event => {
    event.preventDefault();

    if (!image) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("model", model);
    formData.append("image", image);
    
    setIsGenerating(true);

    const result = await fetch('http://127.0.0.1:8000/upload', {
      method: 'POST',
      body: formData,
    }).catch(error => {
      console.log(error);
      setIsGenerating(false);
    });
    const data = await result.json();

    setImageCaption(data.generatedCaption);
  
    setIsGenerating(false);
  }, [image]);

  return (
    <div className="caption-generator-app">
      <img src="/img/background.png" />
      <div className="caption-generator-container">
        <div className="caption-generator-container-inner">
          <header className="caption-generator-app-header">
            Genrate image capture
          </header>
          <form
            className="caption-generator-input-form"
            onSubmit={handleSubmit}
          >
            <select
              name="model"
              className="caption-generator-model-select"
              onChange={event => setModel(event.target.value)}
            >
              {models.map((model, index) => (
                <option key={index} value={model.value}>
                  {model.name}
                </option>
              ))}
            </select>
            <label for="file-upload" class="caption-generator-file-upload">
              Upload File
            </label>
            <input
              type="file"
              id="file-upload"
              className="caption-generator-file-upload-input"
              name="file"
              onChange={handleFileChange}
            />
            <button
              type="submit"
            >
              {isGenerating ? 'Generating...' : 'Generate'}
            </button>
          </form>
          <div className="images-container">
            {imageSrc && (
              <Carousel>
                {[imageSrc].map((images, index) => (
                  <div key={index}>
                    <img src={imageSrc} />
                    {imageCaption && <p className="legend">{imageCaption}</p>}
                  </div>
                ))}
              </Carousel>
            )}
          </div>
        </div>
      </div>
      <img src="/img/background.png" />
    </div>
  );
}

export default App;
