import type { Metadata } from "next";
import { Plus_Jakarta_Sans, Outfit } from "next/font/google";
import "./globals.css";

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
  description: "Computer Science student at University of Guelph. Cloud, security & DevSecOps. Open to work.",
  metadataBase: process.env.NEXT_PUBLIC_SITE_URL ? new URL(process.env.NEXT_PUBLIC_SITE_URL) : undefined,
  openGraph: {
    title: "Moosa Alam — CS · Cloud & Security",
    description: "Computer Science student at University of Guelph. Cloud, security & DevSecOps.",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Moosa Alam",
    description: "Computer Science student. Cloud & Security. Open to work.",
  },
  themeColor: "#0a0a0a",
  robots: "index, follow",
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
      </body>
    </html>
  );
}
