from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", # Chỉ định đọc từ tệp .env
        extra="ignore"   # Bỏ qua các biến môi trường thừa
    )

# Tạo một instance để sử dụng trong toàn bộ ứng dụng
Config = Settings() # type: ignore