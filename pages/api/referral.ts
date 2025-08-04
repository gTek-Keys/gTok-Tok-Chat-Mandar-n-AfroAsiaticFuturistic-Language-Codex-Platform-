import { NextApiRequest, NextApiResponse } from 'next';

interface ReferralRequest {
  referral: string;
}

interface ReferralResponse {
  status: string;
  message: string;
  data?: {
    referralCode: string;
    validated: boolean;
    rewards?: number;
    referrer?: string;
  };
  error?: string;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ReferralResponse>
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ 
      status: 'error',
      message: 'Method not allowed',
      error: 'Only POST requests are accepted' 
    });
  }

  try {
    const { referral }: ReferralRequest = req.body;
    
    if (!referral || !referral.trim()) {
      return res.status(400).json({
        status: 'error',
        message: 'Missing referral code',
        error: 'Referral code is required'
      });
    }

    // Simulate referral validation
    console.log('[Referral API] Processing referral:', referral);
    
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 600));

    // Mock validation logic
    const isValidReferral = referral.length >= 4 && referral.length <= 20;
    const mockRewards = isValidReferral ? Math.floor(Math.random() * 100) + 10 : 0;
    
    // Mock referrer data
    const mockReferrers = ['gTekSovereign', 'CodexMaster', 'MandarPrime', 'AfroAsiaticGuru'];
    const referrer = isValidReferral ? mockReferrers[Math.floor(Math.random() * mockReferrers.length)] : null;

    if (isValidReferral) {
      return res.status(200).json({
        status: 'success',
        message: `Referral code validated successfully: ${referral}`,
        data: {
          referralCode: referral,
          validated: true,
          rewards: mockRewards,
          referrer: referrer || undefined
        }
      });
    } else {
      return res.status(400).json({
        status: 'invalid',
        message: `Invalid referral code: ${referral}`,
        data: {
          referralCode: referral,
          validated: false
        }
      });
    }

  } catch (error) {
    console.error('Referral API Error:', error);
    
    return res.status(500).json({
      status: 'error',
      message: 'Internal server error',
      error: 'Failed to process referral request'
    });
  }
}
