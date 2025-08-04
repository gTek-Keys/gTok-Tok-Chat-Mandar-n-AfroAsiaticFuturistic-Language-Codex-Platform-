# 🚀 Vercel Deployment Guide

## Prerequisites
- GitHub repository connected to Vercel
- Environment variables configured in Vercel dashboard

## Environment Variables Required

Add these in your Vercel project settings:

```bash
OPENAI_API_KEY=your_openai_api_key_here
CLOUDFLARE_AI_KEY=your_cloudflare_ai_key_here
```

## Automatic Deployment

1. **Connect Repository**: Link your GitHub repo to Vercel
2. **Configure Environment**: Add the required environment variables
3. **Deploy**: Push to main branch for automatic deployment

## Manual Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

## Build Commands

Vercel will automatically detect Next.js and use:
- **Build Command**: `next build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`

## Post-Deployment

1. Test all API endpoints:
   - `/api/openai` - OpenAI integration
   - `/api/claude` - Claude streaming
   - `/api/referral` - Referral validation
   - `/api/audinate` - Audio processing
   - `/api/perplexity/search` - Search functionality

2. Verify Phantom wallet integration works
3. Test metadata capsule loading from `/vault/`

## Troubleshooting

- **Build Errors**: Check TypeScript compilation with `npm run type-check`
- **API Errors**: Verify environment variables are set correctly
- **Runtime Errors**: Check Vercel function logs in dashboard

## Performance

- All API routes use Edge Runtime when possible
- Static assets served from CDN
- Phantom wallet integration works client-side only
