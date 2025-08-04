# Next.js Integration Setup

This document describes the Next.js scaffold integration for the gTok-Tok-Chat-Mandar-n-AfroAsiaticFuturistic-Language-Codex-Platform.

## Project Structure

```
/public
  /vault
    digestive_capsule_metadata.json
    digestive_capsule_summary.md
  /icons
    icon1.png ... icon6.png
/pages
  index.tsx                    ← Home page
  launch.tsx                   ← Launch portal page (imports and renders <LaunchPortal />)
  api/
    openai.ts                  ← OpenAI API route
  _app.tsx                     ← Next.js app wrapper
/components
  LaunchPortal.tsx             ← Main launch portal component
/package.json                  ← Dependencies and scripts
/tsconfig.json                 ← TypeScript configuration
/vercel.json                   ← Vercel deployment config
/.env.local                    ← Environment variables
```

## Getting Started

### 1. Install Dependencies

```bash
npm install
```

### 2. Environment Setup

Copy `.env.local` and configure your environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key_here
NEXT_PUBLIC_APP_NAME=gTok-Tok-Chat-Mandar
NEXT_PUBLIC_CODEX_VERSION=1.0.0
NEXT_PUBLIC_LANGUAGE_SUPPORT=AfroAsiaticFuturistic
```

### 3. Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the application.

### 4. Build for Production

```bash
npm run build
npm start
```

## Features

### LaunchPortal Component
- Interactive launch interface
- Icon selection (6 different icons)
- Vault metadata integration
- System status monitoring
- Responsive design

### API Routes
- `/api/openai` - OpenAI integration for chat functionality
- Language detection for AfroAsiatic languages
- Codex mode processing

### Pages
- `/` - Home page with platform overview
- `/launch` - Launch portal interface

## Integration with Existing Python Backend

The Next.js frontend can integrate with your existing Python modules:

- `app.py` - Main Flask/FastAPI application
- `chat_arena.py` - Chat functionality
- `codex_api.py` - Codex processing
- `tts_module.py` - Text-to-speech features

## Deployment

### Vercel (Recommended)
1. Push to GitHub
2. Connect to Vercel
3. Configure environment variables
4. Deploy

### Manual Deployment
```bash
npm run build
npm run export  # For static export if needed
```

## Customization

### Styling
- Components use CSS-in-JS (styled-jsx)
- Responsive design included
- Customizable color schemes and gradients

### Icons
Replace placeholder icons in `/public/icons/` with actual PNG files:
- icon1.png through icon6.png
- Recommended size: 40x40px or larger

### Vault Integration
- Metadata files in `/public/vault/`
- Digestive capsule configuration
- Extensible for additional vault features

## Development Notes

- TypeScript enabled with strict mode
- Next.js 14+ with App Router support
- OpenAI API integration ready
- Modular component architecture
- Environment-based configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

*Part of the gTok-Tok-Chat-Mandar-n-AfroAsiaticFuturistic-Language-Codex-Platform ecosystem*
