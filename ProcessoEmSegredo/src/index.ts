import path from "node:path";
import { exportPautaJson } from "./exporter/jsonExporter.js";
import { parsePautaPdf } from "./parser/pautaParser.js";

async function main(): Promise<void> {
  const pdfArg = process.argv[2];

  if (!pdfArg) {
    console.error("Uso: npm run parse exemplos/pauta1.pdf");
    process.exitCode = 1;
    return;
  }

  const pdfPath = path.resolve(process.cwd(), pdfArg);
  const result = await parsePautaPdf(pdfPath);

  console.log(`Tipo da sessão: ${result.metadata.tipoSessao}`);
  console.log(`Data da pauta: ${result.metadata.dataPauta}`);
  console.log(`Quantidade de processos encontrados: ${result.processos.length}`);
  console.log("");

  result.processos.slice(0, 5).forEach((processo, index) => {
    console.log(`Processo ${index + 1}:`);
    console.log(`Título: ${processo.tituloCompleto}`);
    console.log(`Número: ${processo.numeroProcesso}`);
    console.log(`UF: ${processo.uf}`);
    console.log(`Registro: ${processo.numeroRegistro}`);
    console.log(`Relator: ${processo.relator}`);
    console.log(`Tipo da sessão: ${processo.tipoSessao}`);
    console.log(`Data da pauta: ${processo.dataPauta}`);
    console.log("");
  });

  const exported = await exportPautaJson({
    arquivoOrigem: pdfPath,
    metadata: result.metadata,
    processos: result.processos
  });

  console.log(`JSON gerado em: ${path.relative(process.cwd(), exported.outputPath)}`);
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Erro ao processar pauta: ${message}`);
  process.exitCode = 1;
});
