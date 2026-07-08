export function normalizeText(rawText: string): string {
  return rawText
    .replace(/\r\n?/g, "\n")
    .replace(/\u00a0/g, " ")
    .replace(/[ \t]+/g, " ")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

export function normalizeLine(line: string): string {
  return line.replace(/[ \t]+/g, " ").trim();
}
