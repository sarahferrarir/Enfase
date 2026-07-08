import type { ProcessoPauta } from "../models/ProcessoPauta.js";
import type { PautaMetadata } from "../models/PautaMetadata.js";
import { PROCESS_IDENTIFIER_REGEX } from "./itemSplitter.js";

const RELATOR_REGEX = /^RELATOR(?:A)?\s*:\s*(.+)$/im;
const FIELD_LINE_REGEX = /^[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]{3,}\s*:/u;

export function extractProcessFields(block: string, metadata: PautaMetadata): ProcessoPauta {
  const titleLine = findTitleLine(block);
  const identifierMatch = titleLine.match(PROCESS_IDENTIFIER_REGEX);

  if (!identifierMatch?.[1] || !identifierMatch[2] || !identifierMatch[3]) {
    throw new Error(`Bloco sem identificacao processual valida: ${titleLine}`);
  }

  const [identifierText, numeroProcesso, uf, numeroRegistro] = identifierMatch;
  const classeProcesso = titleLine.slice(0, titleLine.indexOf(identifierText)).trim();
  const relator = extractRelator(block);

  return {
    tituloCompleto: titleLine,
    classeProcesso,
    numeroProcesso,
    uf,
    numeroRegistro,
    relator,
    tipoSessao: metadata.tipoSessao,
    dataPauta: metadata.dataPauta,
    textoCompleto: block
  };
}

function findTitleLine(block: string): string {
  const lines = block.split("\n");
  const titleStartIndex = lines.findIndex((candidate) => PROCESS_IDENTIFIER_REGEX.test(candidate));

  if (titleStartIndex === -1) {
    throw new Error("Nao foi possivel identificar o titulo do processo.");
  }

  const titleLines: string[] = [];
  for (const line of lines.slice(titleStartIndex)) {
    if (titleLines.length > 0 && FIELD_LINE_REGEX.test(line)) {
      break;
    }

    titleLines.push(line.trim());
  }

  return titleLines.join(" ").replace(/\s+/g, " ").trim();
}

function extractRelator(block: string): string {
  const match = block.match(RELATOR_REGEX);
  return match?.[1]?.trim() ?? "";
}
