from pathlib import Path
import yaml


class PromptLoader:
    PROMPTS_DIR = "prompts"
    PROMPT_FILE = "prompt_template.yaml"

    def _load_templates(self) -> dict[str, str]:
        prompt_path = (
            Path(__file__).parent.parent.parent / self.PROMPTS_DIR / self.PROMPT_FILE
        )

        data = yaml.safe_load(prompt_path.read_text(encoding="utf-8"))

        return data["prompt"]

    def load_prompts(self, input: str, philosopher_name: str) -> dict[str, str]:
        template_configs = self._load_templates()
        format_args = {"input": input, "philosopher": philosopher_name}

        for key in template_configs.keys():
            template_configs[key] = template_configs[key].format(**format_args)

        return template_configs
