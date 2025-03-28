import os
  import logging
  from dotenv import load_dotenv
  from telegram.ext import Updater, MessageHandler, Filters

  # تحميل المتغيرات من ملف .env
  load_dotenv()

  # إعدادات البوت
  TOKEN = os.getenv("TELEGRAM_TOKEN")
  TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

  # إعدادات اللوغز
  logging.basicConfig(
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      level=logging.INFO
  )
  logger = logging.getLogger(__name__)

  def forward_message(update, context):
      try:
          update.message.forward(chat_id=TARGET_CHAT_ID)
          logger.info(f"تم إعادة توجيه رسالة من {update.message.chat.id}")
      except Exception as e:
          logger.error(f"خطأ: {e}")

  def main():
      updater = Updater(TOKEN, use_context=True)
      dp = updater.dispatcher
      
      # معالجة جميع الرسائل (نص، صور، ملفات)
      dp.add_handler(MessageHandler(
          Filters.all & ~Filters.command,
          forward_message
      ))
      
      updater.start_polling()
      logger.info("✅ البوت يعمل الآن!")
      updater.idle()

  if __name__ == "__main__":
      main()
