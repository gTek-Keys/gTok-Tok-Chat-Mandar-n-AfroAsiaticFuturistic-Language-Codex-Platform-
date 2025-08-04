export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).end('Method Not Allowed');
  }

  const { prompt } = req.body;

  const apiRes = await fetch('https://ai.cloudflare.com/gateway', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.CLOUDFLARE_AI_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'anthropic/claude-4-sonnet',
      prompt
    })
  });

  if (!apiRes.ok) {
    return res.status(500).json({ error: 'Claude API error' });
  }

  const reader = apiRes.body.getReader();
  const encoder = new TextEncoder();

  res.writeHead(200, {
    'Content-Type': 'text/plain; charset=utf-8',
    'Transfer-Encoding': 'chunked'
  });

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    res.write(encoder.encode(value));
  }

  res.end();
}
