export type TipoSessao = "Ordinária" | "Virtual";

export interface PautaMetadata {
  tipoSessao: TipoSessao;
  dataPauta: string;
}
