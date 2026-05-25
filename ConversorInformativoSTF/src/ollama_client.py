import json
import time
from typing import Optional, Dict, Any
import requests


class OllamaClient:
    """
    Cliente centralizado para Ollama.
    Gerencia conexão, temperatura, retry, timeout.
    """

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "qwen2.5:14b",
        temperature: float = 0.1,
        timeout: int = 300,
        max_retries: int = 3,
    ):
        """
        Args:
            base_url: URL do Ollama (localhost por padrão)
            model: modelo a usar (qwen2.5:14b ou llama3.1:8b recomendado)
            temperature: 0.1 = determinístico, 1.0 = criativo
            timeout: timeout em segundos
            max_retries: número de tentativas se falhar
        """
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.temperature = temperature
        self.timeout = timeout
        self.max_retries = max_retries

    def _health_check(self) -> bool:
        """Verifica se Ollama está rodando."""
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5,
            )
            return response.status_code == 200
        except Exception:
            return False

    def generate(
        self,
        prompt: str,
        json_mode: bool = False,
        system: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Envia prompt para Ollama e aguarda resposta.

        Args:
            prompt: prompt do usuário
            json_mode: se True, instrui para retornar JSON puro
            system: prompt do sistema (contexto)

        Returns:
            Dict com 'text' e 'success' (bool)

        Raises:
            RuntimeError: se Ollama não estiver disponível ou falhar após retries
        """
        if not self._health_check():
            raise RuntimeError(
                f"Ollama não está disponível em {self.base_url}\n"
                "Inicie com: ollama serve"
            )

        # Adiciona instrução de JSON se solicitado
        full_prompt = prompt
        if json_mode:
            full_prompt += (
                "\n\nRetorne APENAS JSON válido, nenhum texto adicional. "
                "Não invente dados, não resuma, preserve texto original."
            )

        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": full_prompt,
                        "system": system,
                        "temperature": self.temperature,
                        "stream": False,
                    },
                    timeout=self.timeout,
                )

                if response.status_code != 200:
                    if attempt < self.max_retries - 1:
                        wait = 2 ** attempt
                        print(f"⏳ Erro {response.status_code}. Tentando novamente em {wait}s...")
                        time.sleep(wait)
                        continue
                    raise RuntimeError(
                        f"Ollama retornou {response.status_code}: {response.text}"
                    )

                data = response.json()
                text = data.get("response", "").strip()

                return {
                    "text": text,
                    "success": True,
                    "model": self.model,
                }

            except requests.Timeout:
                if attempt < self.max_retries - 1:
                    print(f"⏳ Timeout. Tentando novamente ({attempt + 1}/{self.max_retries})...")
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError(
                    f"Ollama timeout após {self.timeout}s e {self.max_retries} tentativas"
                )
            except Exception as e:
                if attempt < self.max_retries - 1:
                    wait = 2 ** attempt
                    print(f"⚠️ Erro: {str(e)}. Tentando em {wait}s...")
                    time.sleep(wait)
                    continue
                raise RuntimeError(f"Erro ao chamar Ollama: {str(e)}")

        raise RuntimeError("Falha após todas as tentativas")

    def generate_json(
        self,
        prompt: str,
        system: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Wrapper que garante resposta JSON.

        Args:
            prompt: prompt do usuário
            system: prompt do sistema

        Returns:
            Dict com 'data' (parsed JSON) e 'success'

        Raises:
            ValueError: se LLM não retornar JSON válido
        """
        response = self.generate(prompt, json_mode=True, system=system)

        try:
            # Tenta extrair JSON do texto
            text = response["text"]

            # Se começa com markdown code block, remove
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]

            text = text.strip()

            data = json.loads(text)
            return {
                "data": data,
                "success": True,
                "raw": text,
            }
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Ollama não retornou JSON válido.\n"
                f"Erro: {str(e)}\n"
                f"Texto: {response['text'][:200]}"
            )
