import { NextApiRequest, NextApiResponse } from 'next';
import OpenAI from 'openai';

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

interface ChatRequest {
  messages: ChatMessage[];
  language?: string;
  codex_mode?: boolean;
}

interface ChatResponse {
  message: string;
  language_detected?: string;
  codex_processed?: boolean;
  error?: string;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ChatResponse>
) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ 
      message: 'Method not allowed', 
      error: 'Only POST requests are accepted' 
    });
  }

  try {
    const { messages, language = 'auto', codex_mode = true }: ChatRequest = req.body;

    // Validate request body
    if (!messages || !Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({
        message: 'Invalid request',
        error: 'Messages array is required and must not be empty'
      });
    }

    // Add system context for the gTok-Tok platform
    const systemMessage: ChatMessage = {
      role: 'system',
      content: `You are an AI assistant for the gTok-Tok-Chat-Mandar-n-AfroAsiaticFuturistic-Language-Codex-Platform. 
      You specialize in AfroAsiatic languages and futuristic linguistic technologies. 
      You can process and understand multiple language families including Semitic, Berber, Cushitic, Chadic, and Omotic languages.
      ${codex_mode ? 'Codex mode is enabled - provide enhanced linguistic analysis and processing.' : ''}
      ${language !== 'auto' ? `User's preferred language context: ${language}` : 'Detect and adapt to the user\'s language automatically.'}
      
      Always be helpful, informative, and culturally sensitive when discussing AfroAsiatic languages and cultures.`
    };

    // Prepare messages for OpenAI
    const openaiMessages = [systemMessage, ...messages];

    // Call OpenAI API
    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: openaiMessages,
      max_tokens: 1000,
      temperature: 0.7,
      presence_penalty: 0.1,
      frequency_penalty: 0.1,
    });

    const assistantMessage = completion.choices[0]?.message?.content;

    if (!assistantMessage) {
      throw new Error('No response generated from OpenAI');
    }

    // Simulate language detection (in a real implementation, you'd use actual language detection)
    const language_detected = detectLanguage(messages[messages.length - 1]?.content || '');

    // Return successful response
    return res.status(200).json({
      message: assistantMessage,
      language_detected,
      codex_processed: codex_mode
    });

  } catch (error) {
    console.error('OpenAI API Error:', error);
    
    // Handle specific OpenAI errors
    if (error instanceof Error) {
      if (error.message.includes('API key')) {
        return res.status(401).json({
          message: 'Authentication error',
          error: 'Invalid or missing OpenAI API key'
        });
      }
      
      if (error.message.includes('quota')) {
        return res.status(429).json({
          message: 'Rate limit exceeded',
          error: 'OpenAI API quota exceeded'
        });
      }
    }

    // Generic error response
    return res.status(500).json({
      message: 'Internal server error',
      error: 'Failed to process chat request'
    });
  }
}

/**
 * Simple language detection function
 * In a production environment, you'd use a proper language detection library
 */
function detectLanguage(text: string): string {
  // Simple heuristic-based detection for demo purposes
  const arabicPattern = /[\u0600-\u06FF]/;
  const hebrewPattern = /[\u0590-\u05FF]/;
  const geezPattern = /[\u1200-\u137F]/;
  const tifinghPattern = /[\u2D30-\u2D7F]/;

  if (arabicPattern.test(text)) {
    return 'Arabic (Semitic)';
  } else if (hebrewPattern.test(text)) {
    return 'Hebrew (Semitic)';
  } else if (geezPattern.test(text)) {
    return 'Ethiopic (Semitic)';
  } else if (tifinghPattern.test(text)) {
    return 'Tifinagh (Berber)';
  } else {
    return 'English (Default)';
  }
}
