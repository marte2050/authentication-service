import yaml
from pathlib import Path

from main import app


def generate_openapi() -> None:
    """Generate OpenAPI specification and save it to src/docs/openapi.yaml"""

    src_dir = Path(__file__).resolve().parents[2]
    output_dir = src_dir / "docs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "openapi.yaml"

    with output_path.open("w") as file:
        yaml.dump(app.openapi(), file, sort_keys=False)

if __name__ == "__main__":
    generate_openapi()
