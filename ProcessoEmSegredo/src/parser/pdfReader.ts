import { readFile } from "node:fs/promises";
import pdfParse from "pdf-parse";

export async function readPdfText(pdfPath: string): Promise<string> {
  const buffer = await readFile(pdfPath);
  const parsed = await pdfParse(buffer);

  return parsed.text;
}
