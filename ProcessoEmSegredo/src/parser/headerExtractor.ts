import type { PautaMetadata, TipoSessao } from "../models/PautaMetadata.js";

const MONTHS: Record<string, string> = {
  janeiro: "01",
  fevereiro: "02",
  marco: "03",
  março: "03",
  abril: "04",
  maio: "05",
  junho: "06",
  julho: "07",
  agosto: "08",
  setembro: "09",
  outubro: "10",
  novembro: "11",
  dezembro: "12"
};

export function extractHeaderMetadata(text: string): PautaMetadata {
  const headerSlice = text.slice(0, 2500);

  /*
   * O tipo da sessao aparece no cabecalho como "Sessão Ordinária" ou
   * "Sessão Virtual", e normalmente se repete na frase "Pauta de Julgamentos
   * da Sessão ...". Procuramos apenas no inicio do texto para evitar capturar
   * algum uso acidental dentro dos blocos dos processos.
   */
  const tipoSessaoMatch = headerSlice.match(/Sess[aã]o\s+(Ordin[áa]ria|Virtual)\b/i);
  if (!tipoSessaoMatch?.[1]) {
    throw new Error("Nao foi possivel identificar o tipo da sessao no header.");
  }

  const tipoSessao = normalizeTipoSessao(tipoSessaoMatch[1]);

  /*
   * A data principal da pauta e a primeira data por extenso apos a referencia
   * ao "dia" da sessao. Em pautas virtuais pode existir tambem uma data de
   * encerramento; por isso usamos a primeira ocorrencia como dataPauta.
   */
  const dataMatch = headerSlice.match(/\bdia\s+(\d{1,2})\s+de\s+([a-zçã]+)\s+de\s+(\d{4})\b/i);
  if (!dataMatch?.[1] || !dataMatch[2] || !dataMatch[3]) {
    throw new Error("Nao foi possivel identificar a data principal da pauta no header.");
  }

  return {
    tipoSessao,
    dataPauta: formatDate(dataMatch[1], dataMatch[2], dataMatch[3])
  };
}

function normalizeTipoSessao(value: string): TipoSessao {
  return value.toLowerCase().startsWith("virtual") ? "Virtual" : "Ordinária";
}

function formatDate(day: string, monthName: string, year: string): string {
  const month = MONTHS[monthName.toLowerCase()];
  if (!month) {
    throw new Error(`Mes nao reconhecido no header: ${monthName}`);
  }

  return `${day.padStart(2, "0")}/${month}/${year}`;
}
