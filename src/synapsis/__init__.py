from pathlib import Path
from dotenv import load_dotenv

__version__ = "1.0.0"

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
