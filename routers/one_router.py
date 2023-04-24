from models import ApplicationForm
from fastapi import APIRouter
from bot import bot
import os

api_router = APIRouter()

@api_router.post("/bot/form_sub")
async def form_sub(appForm: ApplicationForm):   
    await bot.send_message(chat_id=os.getenv("CHAT_ID"),text="""
                                Поступило новое обращение!\n\nФИО - %s\nПочта - %s\nНомер - %s\nКомментарий - %s
                                """ % (appForm.username, appForm.email, appForm.phone, appForm.comments))