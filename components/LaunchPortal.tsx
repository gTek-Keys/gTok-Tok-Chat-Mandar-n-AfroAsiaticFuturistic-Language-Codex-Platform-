import React, { useState, useEffect } from 'react';
import CodexPhaseTracker from './CodexPhaseTracker';

const phases = [
  'Awakening',       // Phase 1: Name or wallet
  'Embodiment',      // Phase 2: Role
  'Instruction',     // Phase 3: Directives
  'Voice',           // Phase 4: Interface tone
  'Understanding',   // Phase 5: Cognition profile
  'Capabilities',    // Phase 6: Powers
  'Essence'          // Phase 7: Signature
];

// Phantom Wallet Interface
interface PhantomProvider {
  connect(options?: { onlyIfTrusted?: boolean }): Promise<{ publicKey: { toString(): string } }>;
  disconnect(): Promise<void>;
  isPhantom: boolean;
}

declare global {
  interface Window {
    solana?: PhantomProvider;
  }
}

const audinateQuery = async (query: string) => {
  const res = await fetch('/api/audinate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  return await res.json();
};

const perplexityQuery = async (prompt: string) => {
  const res = await fetch('/api/perplexity', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });
  return await res.json();
};

export default function LaunchPortal() {
  const [walletConnected, setWalletConnected] = useState(false);
  const [metadata, setMetadata] = useState(null);
  const [referral, setReferral] = useState('');
  const [claudeText, setClaudeText] = useState('');
  const [currentPhase, setCurrentPhase] = useState(0);

  useEffect(() => {
    if ('solana' in window && window.solana?.isPhantom) {
      window.solana.connect({ onlyIfTrusted: true })
        .then(() => {
          setWalletConnected(true);
          setCurrentPhase(1);
        })
        .catch((err) => console.warn('Silent connect failed:', err));
    } else {
      console.warn('Phantom wallet not detected');
    }
  }, []);

  const connectWallet = async () => {
    try {
      if ('solana' in window && window.solana?.isPhantom) {
        await window.solana.connect();
        setWalletConnected(true);
        setCurrentPhase(1);
      } else {
        alert('Phantom wallet not detected. Please install Phantom Wallet.');
      }
    } catch (err) {
      console.error('Failed to connect to Phantom wallet:', err);
      alert('Connection to Phantom wallet failed');
    }
  };

  const mintBadge = () => {
    if (!walletConnected) return alert("Connect wallet first");
    alert("[LIVE MINT] Sovereign badge mint initiated");
    setCurrentPhase(6);
  };

  const handleReferralChange = (e: React.ChangeEvent<HTMLInputElement>) => setReferral(e.target.value);

  const submitReferral = async () => {
    const res = await fetch('/api/referral', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ referral })
    });
    const result = await res.json();
    alert(`Referral response: ${result.status}`);
    setCurrentPhase(2);
  };

  const downloadCapsule = () => {
    window.open('/vault/digestive_capsule_metadata.json', '_blank');
  };

  const loadMetadata = async () => {
    const res = await fetch('/vault/digestive_capsule_metadata.json');
    const data = await res.json();
    setMetadata(data);
    setCurrentPhase(5);
  };

  const generateClaudeText = async () => {
    const response = await fetch('/api/claude', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: 'Why is the sky blue?' })
    });
    
    if (!response.body) {
      setClaudeText('Error: No response stream available');
      return;
    }
    
    const stream = response.body.getReader();
    const decoder = new TextDecoder();
    let text = '';
    while (true) {
      const { done, value } = await stream.read();
      if (done) break;
      text += decoder.decode(value);
      setClaudeText(text);
    }
    setCurrentPhase(4);
  };

  return (
    <div className="p-6 max-w-6xl mx-auto text-white font-sans">
      <h1 className="text-3xl font-bold mb-4">🌌 Mandar:)N™ Codex Gateway Interface</h1>

      <CodexPhaseTracker current={currentPhase} />

      <div className="mb-2 text-sm italic text-indigo-300">Current Phase: {phases[currentPhase]}</div>

      <button onClick={connectWallet} className="btn">{walletConnected ? '🟢 Wallet Connected' : 'Connect Wallet'}</button>
      <button onClick={mintBadge} className="btn ml-2">Mint Badge</button>

      <div className="my-4">
        <input
          type="text"
          placeholder="Enter referral code"
          value={referral}
          onChange={handleReferralChange}
          className="input"
        />
        <button onClick={submitReferral} className="btn ml-2">Submit Referral</button>
      </div>

      <div className="my-4">
        <button onClick={loadMetadata} className="btn">Load Capsule Metadata</button>
        <button onClick={downloadCapsule} className="btn ml-2">Download Capsule JSON</button>
        {metadata && (
          <pre className="bg-gray-800 p-4 mt-2 rounded overflow-x-auto text-xs">
            {JSON.stringify(metadata, null, 2)}
          </pre>
        )}
      </div>

      <div className="my-4">
        <button onClick={generateClaudeText} className="btn">Generate Claude Response</button>
        {claudeText && (
          <p className="mt-2 text-green-300 whitespace-pre-wrap">Claude says: {claudeText}</p>
        )}
      </div>
    </div>
  );
}
