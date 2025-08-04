# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is The Block Auditer Gamification Software, a system that combines blockchain technology, NFT minting, and audit tools. The project appears to be part of the gTek Industries ecosystem and includes multiple components:

- **Chat Builder Business**: React-based NFT mint portal with Solana wallet integration
- **The Block Auditer**: Core gamification software with system audits, NFT minting, and governance templates
- **CodexVault**: Private vault system with licensing and environment management
- **Smart Contracts**: TypeScript-based NFT minting using Helius Labs SDK
- **Audit Tools**: Python scripts for chat intelligence gathering and terminal auditing

## Architecture

The repository contains multiple project directories with overlapping functionality:

- `Chat_Builder_Business-main/` - React app for NFT minting portal
- `The_Block_Auditer_Gamification_Software/` - Main software package
  - `src/` - Core source code (currently empty)
  - `ui/` - User interface components (currently empty)
  - `smart_contracts/` - Solana NFT minting contracts
  - `scripts/` - Utility scripts and environment management
  - `CodexVault/` - Private licensing and vault system
  - `templates/` - Legal and governance document templates
  - `assets/` - Project assets and resources
  - `installers/` - Installation utilities

## Common Commands

### NFT Minting (TypeScript)
```bash
# Navigate to smart contracts directory
cd "The_Block_Auditer_Gamification_Software/smart_contracts"

# Run NFT minting script (requires proper environment setup)
npx ts-node mint_lexvault_nft.ts
```

### Audit Tools (Python)
```bash
# Run chat intelligence aggregator
python sovereign_chat_aggregator.py

# Run terminal audit
python sovereign_terminal_audit.py
```

### Development Scripts
```bash
# Create files with nano editor
./scripts/create_with_nano.sh filename.txt

# Advanced codex utility
./scripts/nano_advanced_codex_utility.sh
```

## Key Technologies

- **Frontend**: React, JavaScript
- **Blockchain**: Solana, Helius Labs SDK
- **Backend**: Python, TypeScript
- **Licensing**: Custom gTek Sovereign OmniLicense system
- **NFT Standards**: Solana NFT with metadata upload

## Environment Configuration

The project uses environment files for API keys and configuration:
- `scripts/lexvault_env.json` - Contains Helius API keys and licensing information
- `CodexVault/vault_env_snapshot.json` - Vault environment snapshots

## License and Legal

This project uses the "gTek Sovereign OmniLicense v2.2.2.2" with specific terms for derivatives and commercial use. The license requires preservation of attribution and explicit licensing for commercial use.

## Security Notes

- API keys are currently hardcoded in some files - move to environment variables for production
- Private keys should never be committed to repository
- The audit tools scan for chat-related content across the system

## File Structure Patterns

- Multiple duplicate directories suggest this may be a development/staging environment
- Core functionality is distributed across several subdirectories
- Template files are provided for legal and governance documents
- Asset files include logos and branding materials