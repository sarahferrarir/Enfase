import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import type { ProcessoPauta } from "../models/ProcessoPauta.js";
import type { PautaMetadata } from "../models/PautaMetadata.js";

export interface ExportJsonInput {
  arquivoOrigem: string;
  metadata: PautaMetadata;
  processos: ProcessoPauta[];
}

export interface ExportJsonResult {
  outputPath: string;
}

interface JsonOutput {
  metadata: {
    arquivoOrigem: string;
    tipoSessao: PautaMetadata["tipoSessao"];
    dataPauta: string;
    quantidadeProcessos: number;
    dataExtracao: string;
  };
  processos: ProcessoPauta[];
}

export async function exportPautaJson(input: ExportJsonInput): Promise<ExportJsonResult> {
  const outputDir = path.resolve(process.cwd(), "outputs");
  await mkdir(outputDir, { recursive: true });

  const baseName = path.parse(input.arquivoOrigem).name;
  const outputPath = path.join(outputDir, `${baseName}.json`);

  const output: JsonOutput = {
    metadata: {
      arquivoOrigem: path.basename(input.arquivoOrigem),
      tipoSessao: input.metadata.tipoSessao,
      dataPauta: input.metadata.dataPauta,
      quantidadeProcessos: input.processos.length,
      dataExtracao: new Date().toISOString()
    },
    processos: input.processos
  };

  await writeFile(outputPath, `${JSON.stringify(output, null, 2)}\n`, "utf8");

  return { outputPath };
}
