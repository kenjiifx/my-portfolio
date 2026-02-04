# 🚀 Deployment Guide

## Deploy to Vercel (Recommended)

### Method 1: Via GitHub (Easiest)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Modern portfolio with Next.js 15"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your GitHub repository
   - Vercel will automatically detect Next.js
   - Click "Deploy"
   - Done! Your site will be live in ~2 minutes

### Method 2: Via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Follow the prompts**
   - Login to your Vercel account
   - Confirm project settings
   - Deploy!

## 🎨 Customization Tips

### Colors
Edit `tailwind.config.ts` to change the color scheme:
```typescript
colors: {
  primary: "#8b5cf6",  // Purple
  secondary: "#6366f1", // Indigo
  accent: "#f59e0b",    // Amber
}
```

### Content
- Update your info in each component file
- Replace the resume PDF in `/public`
- Modify the experience, education, and certifications arrays

### Performance
- Images: Use Next.js Image component for optimization
- Fonts: Already using Next.js font optimization
- Animations: All animations are GPU-accelerated

## 📊 Performance Features

✅ Optimized for Core Web Vitals
✅ Static Export for lightning-fast loading
✅ Minimal JavaScript bundle
✅ Lazy loading for all sections
✅ GPU-accelerated animations

## 🛠️ Troubleshooting

**Build fails?**
- Clear the `.next` folder: `rm -rf .next`
- Clear node_modules: `rm -rf node_modules && npm install`

**Animations laggy?**
- Reduce particle count in `ParticlesBackground.tsx`
- Disable animations on mobile devices

**TypeScript errors?**
- Run `npm run build` to see all errors
- Most errors are auto-fixed on save

## 🌟 Features Included

- ✨ Smooth scroll animations
- 🎨 Custom particle background
- 🖱️ Custom cursor follower
- 📊 Scroll progress indicator
- 🎭 Glass morphism effects
- 🌈 Gradient text effects
- 📱 Fully responsive design
- ⚡ Lightning-fast performance

## 📝 Environment Variables (Optional)

Create a `.env.local` file for any environment variables:
```
NEXT_PUBLIC_ANALYTICS_ID=your_id_here
```

## 🔒 Security

- No API keys exposed
- All data is static
- Resume PDF is publicly accessible (as intended)

---

Made with ❤️ using Next.js 15, Framer Motion, and Tailwind CSS
