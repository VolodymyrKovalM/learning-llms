import { useState, useCallback } from 'react';
import classNames from 'classnames';
import { TextareaAutosize, Button } from '@mui/material';

import './App.css';

function App() {
  const [isSending, setIsSending] = useState(false);
  const [messages, setMessages] = useState([]);

  const [formData, setFormData] = useState({
    prompt: '',
  });

  const handleSubmit = useCallback(async event => {
    event.preventDefault();

    const payload = {
      prompt: formData.prompt,
    };

    setMessages([
      ...messages,
      {
        role: 'user',
        text: formData.prompt,
      },
    ]);
    setFormData({
      prompt: '',
    });
    
    setIsSending(true);

    const result = await fetch('http://127.0.0.1:8000/generate-answer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    }).catch(error => {
      console.log(error);
      setIsSending(false);
    });
    const data = await result.json();

    setMessages([
      ...messages,
      {
        role: 'assistant',
        text: data.message,
      },
    ]);
  
    setIsSending(false);
  }, [formData]);

  return (
    <div className="ai-chat-bot-app">
      <h2>Language learning assistant</h2>
      <div className="ai-chat-bot-app-output">
        {messages.map((message, index) => (
          <div
            key={`ai-chat-bot-message-${index}`}
            className={classNames('ai-chat-bot-app-message', {
              'message-user': message.role === 'user',
              'message-assistant': message.role === 'assistant',
            })}
          >
            <div
              className="ai-chat-bot-app-message-inner"
            >
              {message.text}
            </div>
          </div>
        ))}
      </div>
      <form
        className="ai-chat-bot-app-form"
        onSubmit={handleSubmit}
      >
        <TextareaAutosize
          minRows={5}
          name="prompt"
          className="ai-chat-bot-app-prompt"
          onChange={event => setFormData({
            ...formData,
            prompt: event.target.value,
          })}
          placeholder='Enter your prompt here'
        />
        <Button
          type="submit"
          variant="contained"
          loading={isSending}
          disabled={!formData.prompt}
        >
          Send
        </Button>
      </form>
    </div>
  );
}

export default App;
