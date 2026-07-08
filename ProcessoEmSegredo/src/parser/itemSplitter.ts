import { normalizeLine } from "./textNormalizer.js";

export const PROCESS_IDENTIFIER_REGEX =
  /\bN[º°o]\s*(\d+)\s*-\s*([A-Z]{2})\s*\((\d{4}\/\d{7}-\d)\)/;

const PROCESS_NUMBER_MARKER_REGEX = /\bN[º°o]/;
const MAX_TITLE_LINES_TO_JOIN = 4;

export function splitProcessItems(text: string): string[] {
  const normalizedLines = text
    .split("\n")
    .map(normalizeLine)
    .filter(Boolean);
  const lines = recomposeBrokenProcessTitleLines(normalizedLines);

  const startIndexes: number[] = [];

  /*
   * Nao tentamos prever a classe processual. Antes da deteccao, recompomos
   * titulos quebrados pelo PDF quando a linha com "Nº" continua nas linhas
   * seguintes, como:
   *
   * "Nº 1871255 - DF" + "(2021/0103670-4)"
   * "RECURSO ESPECIAL Nº" + "2524670 - SP (2023/0450752-8)"
   *
   * Depois disso, um novo processo e detectado quando a linha contem a
   * identificacao processual estavel: "Nº <numero> - <UF> (<registro>)".
   */
  lines.forEach((line, index) => {
    if (PROCESS_IDENTIFIER_REGEX.test(line)) {
      startIndexes.push(index);
    }
  });

  return startIndexes.map((startIndex, position) => {
    const nextStartIndex = startIndexes[position + 1] ?? lines.length;
    return lines.slice(startIndex, nextStartIndex).join("\n").trim();
  });
}

function recomposeBrokenProcessTitleLines(lines: string[]): string[] {
  const recomposedLines: string[] = [];

  for (let index = 0; index < lines.length; index += 1) {
    let currentLine = lines[index] ?? "";
    let joinedLines = 1;

    while (
      PROCESS_NUMBER_MARKER_REGEX.test(currentLine) &&
      !PROCESS_IDENTIFIER_REGEX.test(currentLine) &&
      index + 1 < lines.length &&
      joinedLines < MAX_TITLE_LINES_TO_JOIN
    ) {
      index += 1;
      joinedLines += 1;
      currentLine = `${currentLine} ${lines[index]}`.replace(/\s+/g, " ").trim();
    }

    recomposedLines.push(currentLine);
  }

  return recomposedLines;
}
