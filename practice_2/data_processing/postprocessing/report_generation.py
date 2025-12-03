# data_processing/postprocessing/report_generation.py

from typing import Dict, List


def generate_text_report(cleaned_values: List[float], stats: Dict[str, float]) -> str:
    """Генерирует простой текстовый отчет по данным и статистикам."""
    lines = []
    lines.append("ОТЧЕТ ПО ДАННЫМ")
    lines.append("-" * 30)
    lines.append(f"Число наблюдений: {len(cleaned_values)}")
    lines.append(f"Минимум: {stats['min']}")
    lines.append(f"Максимум: {stats['max']}")
    lines.append(f"Среднее: {stats['mean']}")
    lines.append("")
    lines.append("Значения после очистки:")
    lines.append(", ".join(str(v) for v in cleaned_values))

    return "\n".join(lines)

