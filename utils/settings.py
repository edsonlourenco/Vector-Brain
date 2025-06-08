"""Module to hold session settings for the LLM assistant."""

import os


class Session:
     """Class to hold session settings for the LLM assistant."""
     def __init__(self):
         self.PDF_PATH = "docs/Databricks_LLM_guide_ptbr.pdf"
         self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")