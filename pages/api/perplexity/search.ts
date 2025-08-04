import { NextApiRequest, NextApiResponse } from 'next';

interface PerplexitySearchRequest {
  prompt: string;
  sources?: string[];
  max_results?: number;
}

interface PerplexitySearchResult {
  title: string;
  summary: string;
  url?: string;
  relevance_score?: number;
}

interface PerplexityResponse {
  status: string;
  message: string;
  results?: PerplexitySearchResult[];
  metadata?: {
    query_time: number;
    total_results: number;
  };
  error?: string;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<PerplexityResponse>
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ 
      status: 'error',
      message: 'Method not allowed',
      error: 'Only POST requests are accepted' 
    });
  }

  try {
    const { prompt, sources = [], max_results = 5 }: PerplexitySearchRequest = req.body;
    
    if (!prompt) {
      return res.status(400).json({
        status: 'error',
        message: 'Missing prompt',
        error: 'Prompt is required for search'
      });
    }

    // Simulate Perplexity API processing
    console.log('[Perplexity API] Processing search prompt:', prompt);
    
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 800));

    // Mock search results based on prompt content
    const mockResults: PerplexitySearchResult[] = [];
    
    if (prompt.toLowerCase().includes('referral')) {
      mockResults.push(
        {
          title: 'Referral Code Validation System',
          summary: 'A comprehensive guide to implementing secure referral validation in decentralized platforms.',
          url: 'https://example.com/referral-validation',
          relevance_score: 0.95
        },
        {
          title: 'Blockchain Referral Networks',
          summary: 'How blockchain technology enhances referral program transparency and security.',
          url: 'https://example.com/blockchain-referrals',
          relevance_score: 0.87
        }
      );
    } else if (prompt.toLowerCase().includes('sovereign')) {
      mockResults.push(
        {
          title: 'Sovereign Technology Platforms',
          summary: 'Understanding the principles of technological sovereignty and user autonomy in digital platforms.',
          url: 'https://example.com/sovereign-tech',
          relevance_score: 0.93
        },
        {
          title: 'Decentralized Governance Models',
          summary: 'Exploring governance mechanisms that empower communities while maintaining platform integrity.',
          url: 'https://example.com/governance',
          relevance_score: 0.89
        }
      );
    } else {
      mockResults.push(
        {
          title: 'gTok Platform Overview',
          summary: 'Comprehensive information about the gTok Mandar platform and its capabilities.',
          url: 'https://example.com/gtok-overview',
          relevance_score: 0.91
        },
        {
          title: 'AfroAsiatic Language Processing',
          summary: 'Advanced techniques for processing and understanding AfroAsiatic language families.',
          url: 'https://example.com/afroasiatic-nlp',
          relevance_score: 0.85
        }
      );
    }

    return res.status(200).json({
      status: 'success',
      message: `Perplexity search completed for: ${prompt}`,
      results: mockResults.slice(0, max_results),
      metadata: {
        query_time: Math.random() * 1000 + 200, // Mock query time
        total_results: mockResults.length
      }
    });

  } catch (error) {
    console.error('Perplexity API Error:', error);
    
    return res.status(500).json({
      status: 'error',
      message: 'Internal server error',
      error: 'Failed to process Perplexity search request'
    });
  }
}
