from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    gemini_api_key: str

    cloudflare_account_id: str
    cloudflare_api_token: str

    hunter_model: str = "gemini-2.5-flash"
    designer_model: str = "gemini-3.8-flash"
    closer_model: str = "gemini-3.8-flash"
    translator_model: str = "gemini-3.5-live-translate-preview"
    image_model: str = "@cf/black-forest-labs/flux-1-schnell"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()