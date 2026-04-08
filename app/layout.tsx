import type { Metadata, Viewport } from "next";
import { Plus_Jakarta_Sans, Outfit } from "next/font/google";
import "./globals.css";
import { Analytics } from "@vercel/analytics/next";

const plusJakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  variable: "--font-display",
  weight: ["400", "500", "600", "700", "800"],
});

const outfit = Outfit({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["300", "400", "500", "600"],
});

export const metadata: Metadata = {
  title: "Moosa Alam",
  description:
    "Computer Science @ University of Guelph. Aspiring Security Engineer. Open to security-focused internships and co-op roles.",
  metadataBase: process.env.NEXT_PUBLIC_SITE_URL ? new URL(process.env.NEXT_PUBLIC_SITE_URL) : undefined,
  openGraph: {
    title: "Moosa Alam — CS · Security Engineering",
    description:
      "Computer Science student at University of Guelph. Aspiring Security Engineer focused on secure, reliable systems.",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Moosa Alam",
    description:
      "Computer Science @ Guelph. Aspiring Security Engineer. Open to security-focused roles.",
  },
  robots: "index, follow",
};

export const viewport: Viewport = {
  themeColor: "#0a0a0a",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth">
      <body
        className={`${plusJakarta.variable} ${outfit.variable} font-sans antialiased bg-[#0a0a0a] text-white min-h-screen`}
      >
        {children}
        <Analytics />
      </body>
    </html>
  );
}
