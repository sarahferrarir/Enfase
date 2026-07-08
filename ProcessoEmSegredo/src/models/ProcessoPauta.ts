import type { PautaMetadata } from "./PautaMetadata.js";

export interface ProcessoPauta extends PautaMetadata {
  tituloCompleto: string;
  classeProcesso: string;
  numeroProcesso: string;
  uf: string;
  numeroRegistro: string;
  relator: string;
  textoCompleto: string;
}
