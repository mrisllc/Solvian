# Solvian Deployment Guide

## Quick Cloud Deployment (Recommended)

### Option 1: Deploy on Heroku (Free)

1. **Create Heroku Account**
   - Go to https://www.heroku.com/
   - Sign up for free account

2. **Deploy from GitHub**
   - Login to Heroku
   - Click "New" → "Create new app"
   - Name: `solvian-bot` (or any name)
   - Region: Choose your region
   - Click "Create app"

3. **Connect GitHub Repository**
   - Go to "Deploy" tab
   - Search for `mrisllc/Solvian`
   - Click "Connect"

4. **Add Environment Variables**
   - Go to "Settings" tab
   - Click "Reveal Config Vars"
   - Add two variables:
     ```
     OPENAI_API_KEY = your_openai_key_here
     TELEGRAM_BOT_TOKEN = 8589504681:AAFk2LmSzk85o8L20lWhaEFC-5F316h5Pn8
     ```

5. **Deploy**
   - Go to "Deploy" tab
   - Click "Deploy Branch"
   - Wait for deployment to finish
   - Check logs for any errors

6. **Done!** ✅
   - Bot is now running 24/7
   - Go to `t.me/solvian_chat_bot` and test it

### Option 2: Deploy on Replit (Super Easy)

1. Go to https://replit.com/
2. Click "Import from GitHub"
3. Paste: `https://github.com/mrisllc/Solvian`
4. Add Secrets (Environment Variables):
   - `OPENAI_API_KEY` = your key
   - `TELEGRAM_BOT_TOKEN` = 8589504681:AAFk2LmSzk85o8L20lWhaEFC-5F316h5Pn8
5. Click "Run"
6. Done! Bot is running

### Option 3: Deploy on Railway (Free)

1. Go to https://railway.app/
2. Sign up
3. Create new project → Import from GitHub
4. Select `mrisllc/Solvian`
5. Add environment variables
6. Deploy and done!

---

## Local Deployment (If you have a PC)

```bash
# Clone repository
git clone https://github.com/mrisllc/Solvian.git
cd Solvian

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add:
# OPENAI_API_KEY=your_key_here
# TELEGRAM_BOT_TOKEN=8589504681:AAFk2LmSzk85o8L20lWhaEFC-5F316h5Pn8

# Run bot
python telegram_bot.py
```

---

## Testing the Bot

Once deployed:
1. Open Telegram
2. Search: `@solvian_chat_bot`
3. Click "START"
4. Send a message and wait for response
5. If no response, check logs for errors

---

## Troubleshooting

**Bot not responding?**
- Check if bot process is running
- Verify TELEGRAM_BOT_TOKEN is correct
- Check OPENAI_API_KEY is valid
- View logs for errors

**Getting errors?**
- Make sure all dependencies are installed
- Check environment variables are set
- Verify internet connection

---

**Need Help?** Contact support or check GitHub issues.
