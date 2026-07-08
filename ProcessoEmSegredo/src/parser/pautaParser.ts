import type { ProcessoPauta } from "../models/ProcessoPauta.js";
import type { PautaMetadata } from "../models/PautaMetadata.js";
import { extractProcessFields } from "./fieldExtractor.js";
import { extractHeaderMetadata } from "./headerExtractor.js";
import { splitProcessItems } from "./itemSplitter.js";
import { normalizeText } from "./textNormalizer.js";
import { readPdfText } from "./pdfReader.js";

export interface ParsePautaResult {
  metadata: PautaMetadata;
  processos: ProcessoPauta[];
}

export async function parsePautaPdf(pdfPath: string): Promise<ParsePautaResult> {
  const rawText = await readPdfText(pdfPath);
  const normalizedText = normalizeText(rawText);
  const metadata = extractHeaderMetadata(normalizedText);
  const blocks = splitProcessItems(normalizedText);
  const processos = blocks.map((block) => extractProcessFields(block, metadata));

  return {
    metadata,
    processos
  };
}
