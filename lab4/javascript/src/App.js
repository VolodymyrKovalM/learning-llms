import { useState, useCallback } from 'react';
import { TextareaAutosize, Slider, SliderValueLabel, Button } from '@mui/material';

import './App.css';

function App() {
  const [isGenerating, setIsGenerating] = useState(false);
  const [generatedOutput, setGeneratedOutput] = useState('');
  const [formData, setFormData] = useState({
    prompt: '',
    maxTokens: 2000,
    temperature: 0.75,
    topP: 1,
  });

  const handleSubmit = useCallback(async event => {
    event.preventDefault();

    const payload = {
      prompt: formData.prompt,
      maxTokens: formData.maxTokens,
      temperature: formData.temperature,
      topP: formData.topP,
    };
    
    setIsGenerating(true);

    const result = await fetch('http://127.0.0.1:8000/generate-answer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    }).catch(error => {
      console.log(error);
      setIsGenerating(false);
    });
    const data = await result.json();

    setGeneratedOutput(data.generatedOutput);
  
    setIsGenerating(false);
  }, [formData]);

  return (
    <div className="prompt-engineering-app">
      <h2>Prompt Engineering</h2>
      <form
        className="prompt-engineering-app-form"
        onSubmit={handleSubmit}
      >
        <TextareaAutosize
          minRows={5}
          name="prompt"
          className="prompt-engineering-app-prompt"
          onChange={event => setFormData({
            ...formData,
            prompt: event.target.value,
          })}
          placeholder='Enter your prompt here'
        />
        <div className="prompt-engineering-app-form-field">
          <span>Max Tokens</span>
          <span className="prompt-engineering-app-form-field-value">
            {formData.maxTokens}
          </span>
          <Slider
            defaultValue={formData.maxTokens}
            min={1}
            max={10000}
            onChange={(_, value) => setFormData({
              ...formData,
              maxTokens: value,
            })}
            valueLabelDisplay="auto"
            slots={{ valueLabel: SliderValueLabel }}
            value={formData.maxTokens}
          />
        </div>
        <div className="prompt-engineering-app-form-field">
          <span>Temperature</span>
          <span className="prompt-engineering-app-form-field-value">
            {formData.temperature}
          </span>
          <Slider
            defaultValue={formData.temperature}
            min={0.10}
            max={1.00}
            step={0.01}
            onChange={(_, value) => setFormData({
              ...formData,
              temperature: value,
            })}
            valueLabelDisplay="auto"
            slots={{ valueLabel: SliderValueLabel }}
            value={formData.temperature}
          />
        </div>
        <div className="prompt-engineering-app-form-field">
          <span>Top P</span>
          <span className="prompt-engineering-app-form-field-value">
            {formData.topP}
          </span>
          <Slider
            defaultValue={formData.topP}
            min={0.10}
            max={1.00}
            step={0.01}
            onChange={(_, value) => setFormData({
              ...formData,
              topP: value,
            })}
            valueLabelDisplay="auto"
            slots={{ valueLabel: SliderValueLabel }}
            value={formData.topP}
          />
        </div>
        <Button
          type="submit"
          variant="contained"
          loading={isGenerating}
          disabled={!formData.prompt}
        >
          Generate Output
        </Button>
      </form>
      <div className="prompt-engineering-app-output">
        {generatedOutput}
      </div>
    </div>
  );
}

export default App;
