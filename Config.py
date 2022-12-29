import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28617319"))
    API_HASH = os.environ.get("API_HASH", "15e0d554ea25e629d21b9d9d7457d3ff")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5797465545:AAH6wNmJH3Tu7CYx5QYBevTmGlObUcwJYmI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQCv0Xqn_gtJXRwGxcQ8FujEjQw3R_Yfk2u7mWpemiBye7FemZOMhqRUp_wNkRKdqya2zFc6-M68dmOVI2p6uVMzbpV4KZtPK-wsEszrOj4TP_GYiBB0bQKKbqbP_rpfM9jW7cgA_NjQvVqemZxCgbTOuANw6qOlUW7D2-G5W4m0RVFQkLpUp6Mbf1s8n-tv9jSleKcujWJY67ShUX6HnOIsTioGKhhEjaepKyOEyXARd6NrnzC6aztHjzXP_RW87gCf6ZS5gMjMg30AQ2CsBopBk2KGl3jrx5XSx5_pevAY-2FPeaUUv_hv9sI7lqawQfdnrrvRs57Tv-o1lKyc6eyfAAAAAV67g1oA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "x_eternal_love_musicbot")
    SUPPORT = os.environ.get("SUPPORT", "freemason_ry") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "eternalkaguya") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph//file/a58113c16e19abc463bbe.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5921146976")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
