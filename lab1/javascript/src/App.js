import { useState, useCallback } from 'react';
import OpenAI from 'openai';
import { Carousel } from 'react-responsive-carousel';

import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './App.css';

const openai = new OpenAI({
  organization: '',
  project: '',
  apiKey: '',
  dangerouslyAllowBrowser: true,
});

function App() {
  const [isGenerating, setIsGenerating] = useState(false);
  const [generatorRequest, setGeneratorRequest] = useState('');
  const [images, setImages] = useState([
    {
      url: '/img/generated-design.png',
      request: 'Design for image generation application, text input, panel with title and place for displaying the generated image, light theme',
    }
  ]);

  const handleOnChange = useCallback(event => {
    setGeneratorRequest(event.target.value);
  }, []);

  const handleSubmit = useCallback(async event => {
    event.preventDefault();

    setIsGenerating(true);

    const result = await openai.images.generate({
      prompt: generatorRequest,
      model: 'dall-e-3',
      n: 1,
      size: '1024x1024'
    });

    if (result?.data[0]?.url) {
      setImages(
        images.concat({
          ...result.data[0],
          request: generatorRequest,
        }),
      );

      setGeneratorRequest('');
    }

    setIsGenerating(false);
  }, [generatorRequest]);

  return (
    <div className="image-generator-app">
      <img src="/img/background.png" />
      <div className="image-generator-container">
        <div className="image-generator-container-inner">
          <header className="image-generator-app-header">
            Image generator
          </header>
          <form
            className="image-generator-input-form"
            onSubmit={handleSubmit}
          >
            <input
              type="text"
              placeholder="Enter text to generate an image"
              onChange={handleOnChange}
              value={generatorRequest}
            />
            <button
              type="submit"
            >
              {isGenerating ? 'Generating...' : 'Generate'}
            </button>
          </form>
          <div className="images-container">
            <Carousel>
              {images.map((images, index) => (
                <div key={index}>
                  <img src={images.url} />
                  <p className="legend">{images.request}</p>
                </div>
              ))}
            </Carousel>
          </div>
        </div>
      </div>
      <img src="/img/background.png" />
    </div>
  );
}

export default App;
