import telebot
import openai

bot = telebot.TeleBot("5854203921:AAGk3aRe-ExjoE0w9ETAwXEbCs1QnXt11tA")
openai.api_key = "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"
@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()
