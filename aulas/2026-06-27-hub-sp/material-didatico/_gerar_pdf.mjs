// Gera PDF backup dos slides reveal.js via Playwright/Chromium.
// Receita: ?print-pdf + injeção do pdf.css do reveal 5.1.0 + page.pdf landscape.
// Proveniência: receita-deck-pdf do IMI (reveal-js-print-pdf, playwright-pdf).
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const file = process.argv[2];
if (!file) { console.error('uso: node _gerar_pdf.mjs <arquivo.html>'); process.exit(2); }

const abs = path.resolve(file);
const url = pathToFileURL(abs).href + '?print-pdf';
const out = abs.replace(/\.html$/, '.pdf');

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
// regras essenciais do pdf.css do reveal 5.1.0, inline (robusto/offline) — 1 slide/página
await page.addStyleTag({ content: `
  @media print { html, body { width:100%; height:100%; margin:0; padding:0; -webkit-print-color-adjust:exact; } }
  html.print-pdf .reveal.slides { position:static; width:100%; height:auto; overflow:visible; }
  html.print-pdf .reveal .slides section {
    visibility:visible !important; display:block !important; position:relative !important;
    page-break-after:always; page-break-inside:avoid;
    min-height:100vh; height:auto !important; left:0 !important; top:0 !important;
    margin:0 !important; padding:3vh 4vw !important; transform:none !important; opacity:1 !important;
    box-sizing:border-box;
  }
  html.print-pdf .reveal .slides section .fragment { opacity:1 !important; visibility:visible !important; }
`});
await page.waitForTimeout(2500); // deixa reveal/SVG/Chart.js assentarem
await page.pdf({
  path: out,
  landscape: true,
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});
await browser.close();
console.log('PDF gerado:', out);
