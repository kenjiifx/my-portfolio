# Moosa Alam — Portfolio

Personal site built with Next.js (App Router), deployed on Vercel.

## Tech stack

- **Next.js 15** — App Router, static export
- **TypeScript**
- **Tailwind CSS**
- **Framer Motion** — section transitions and micro-interactions
- **@vercel/analytics** — Web Analytics on the live deployment

## Development

```bash
npm install
npm run dev
```

```bash
npm run build
```

Static export is configured in `next.config.ts` (`output: "export"`).

## Deployment

Connected to GitHub; pushes to `main` deploy via Vercel.

Optional: set `NEXT_PUBLIC_SITE_URL` (e.g. `https://moosaalam.vercel.app`) for canonical / Open Graph base URLs.

## License

© 2026 Moosa Alam. All rights reserved.
