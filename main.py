"""
MIS Commentary Agent - Main Script

This script provides a starter API-based workflow for generating financial MIS commentary
using LLM APIs (OpenAI, Anthropic, or Perplexity).

For the no-code route, simply copy prompts/system-prompt.md into ChatGPT/Claude/Perplexity
and upload your P&L CSV data.
"""

import os
import csv
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MISCommentaryAgent:
    """Main agent class for generating MIS commentary"""

    def __init__(self, provider: str = "openai"):
        """
        Initialize the agent with the specified provider.

        Args:
            provider: AI provider to use ('openai', 'anthropic', or 'perplexity')
        """
        self.provider = provider
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        """Load the system prompt from prompts/system-prompt.md"""
        prompt_path = Path("prompts/system-prompt.md")
        if not prompt_path.exists():
            raise FileNotFoundError(f"System prompt not found at {prompt_path}")
        return prompt_path.read_text()

    def load_mis_data(self, csv_path: str) -> list:
        """Load MIS data from a CSV file"""
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def generate_commentary(self, data: list) -> str:
        """
        Generate MIS commentary using the specified AI provider.

        Args:
            data: List of dictionaries containing MIS data

        Returns:
            Generated commentary string
        """
        # Format data for the prompt
        data_str = json.dumps(data, indent=2)

        if self.provider == "openai":
            return self._call_openai(data_str)
        elif self.provider == "anthropic":
            return self._call_anthropic(data_str)
        elif self.provider == "perplexity":
            return self._call_perplexity(data_str)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def _call_openai(self, data_str: str) -> str:
        """Call OpenAI API"""
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("Run: pip install openai")

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model=os.getenv("DEFAULT_MODEL", "gpt-4o"),
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Here is the MIS data:\n{data_str}"}
            ],
            temperature=float(os.getenv("TEMPERATURE", "0.3")),
            max_tokens=int(os.getenv("MAX_TOKENS", "4000"))
        )
        return response.choices[0].message.content

    def _call_anthropic(self, data_str: str) -> str:
        """Call Anthropic (Claude) API"""
        try:
            import anthropic
        except ImportError:
            raise ImportError("Run: pip install anthropic")

        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        message = client.messages.create(
            model="claude-sonnet-4-0",
            max_tokens=int(os.getenv("MAX_TOKENS", "4000")),
            system=self.system_prompt,
            messages=[
                {"role": "user", "content": f"Here is the MIS data:\n{data_str}"}
            ]
        )
        return message.content[0].text

    def _call_perplexity(self, data_str: str) -> str:
        """Call Perplexity API"""
        try:
            import requests
        except ImportError:
            raise ImportError("Run: pip install requests")

        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Here is the MIS data:\n{data_str}"}
            ],
            "temperature": float(os.getenv("TEMPERATURE", "0.3")),
            "max_tokens": int(os.getenv("MAX_TOKENS", "4000"))
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def save_commentary(self, commentary: str, output_path: str = "report.md"):
        """Save the generated commentary to a file"""
        output_dir = Path(os.getenv("OUTPUT_DIR", "./reports"))
        output_dir.mkdir(exist_ok=True)

        full_path = output_dir / output_path
        full_path.write_text(commentary)
        print(f"Commentary saved to {full_path}")


def main():
    """Main entry point"""
    print("=" * 60)
    print("MIS Commentary Agent")
    print("AI-powered financial MIS commentary generator")
    print("=" * 60)

    # Initialize agent
    provider = os.getenv("DEFAULT_PROVIDER", "openai")
    agent = MISCommentaryAgent(provider=provider)
    print(f"Using provider: {provider}")

    # Load sample data
    sample_data_path = "examples/sample-input.csv"
    if not Path(sample_data_path).exists():
        print(f"Error: Sample data not found at {sample_data_path}")
        print("Please copy .env.example to .env and add your API keys first.")
        return

    data = agent.load_mis_data(sample_data_path)
    print(f"Loaded {len(data)} rows of MIS data")

    # Generate commentary
    print("\nGenerating commentary...")
    try:
        commentary = agent.generate_commentary(data)
        print("Commentary generated successfully!")

        # Save output
        agent.save_commentary(commentary)

        print("\n" + "=" * 60)
        print("NEXT STEP: Review the generated commentary against")
        print("prompts/review-checklist.md before distribution")
        print("=" * 60)

    except Exception as e:
        print(f"Error generating commentary: {e}")
        print("Please check your API keys in .env file")


if __name__ == "__main__":
    main()
