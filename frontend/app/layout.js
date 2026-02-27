import "./globals.css";

export const metadata = {
  title: "MaskIT AI — Privacy Preservation Framework",
  description: "Multi-modal AI-driven PII redaction framework for detecting and sanitizing sensitive information from text, PDFs, and images. Supports masking, anonymization, hashing, and tag replacement.",
  keywords: "PII redaction, data privacy, NLP, OCR, AI compliance, dataset sanitization",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
